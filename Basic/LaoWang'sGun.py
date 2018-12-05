class Person(object):
	"""Person"""
	def __init__(self, name):
		super(Person, self).__init__()
		self.name = name
		self.gun = None
		self.hp = 100

	def anZhuang_ziDan(self, danJia, ziDan):
		danJia.baoCun_ziDan(ziDan)

	def anZhuang_danJia(self, gun, danJia):
		gun.zhuang_danJia(danJia)

	def naGun(self, gun):
		self.gun = gun

	def shoot(self, diren):
		self.gun.fire(diren)

	def diaoXue(self, shaShangLi):
		self.hp -= shaShangLi

	def __str__(self):
		if self.gun:
			# return "%s take the %s"%(self.name, self.gun.name)
			return "%s's hp is %d, and %s"%(self.name, self.hp, self.gun)
		else:
			if self.hp > 0:
				return "%s's hp is %d (without gun!)"%(self.name, self.hp)
			else:
				return "%s is dead!"%self.name
class Gun(object):
	"""Gun"""
	def __init__(self, name):
		super(Gun, self).__init__()
		self.name = name
		self.danJia = None

	def zhuang_danJia(self, danJia):
		self.danJia = danJia

	def fire(self, diren):
		ziDan = self.danJia.tanChu_ziDan()

		if ziDan:
			ziDan.daZhong(diren)
		else:
			print("danJia is empty!")

	def __str__(self):
		if self.danJia:
			return "the danJia's info is %d/%d in %s"%(len(self.danJia.ziDan_list), self.danJia.rongLiang, self.name)
			# return "Gun is %s,\t %s"%(self.name, self.danJia)#also right
		else:
			return "There is no danJia in %s"%self.name

class DanJia(object):
	"""DanJia"""
	def __init__(self, rongLiang):
		super(DanJia, self).__init__()
		self.rongLiang = rongLiang
		self.ziDan_list = []
		
	def baoCun_ziDan(self, ziDan):
		self.ziDan_list.append(ziDan)

	def tanChu_ziDan(self):
		if self.ziDan_list:
			return self.ziDan_list.pop()
		else:
			return None

	def __str__(self):
		return "ziDan's info:\t%d/%d"%(len(self.ziDan_list), self.rongLiang)

class ZiDan(object):
	"""ZiDan"""
	def __init__(self, shaShangLi):
		super(ZiDan, self).__init__()
		self.shaShangLi = shaShangLi
		
	def daZhong(self, diren):
		diren.diaoXue(self.shaShangLi)



def main():
	#create laowang
	laoWang = Person("Wang")
	laoGao = Person("Gao")

	#create gun
	ak47 = Gun("AK47")

	#create danjia
	danJia = DanJia(30)

	for x in range(20):
		#create zidan
		ziDan = ZiDan(10)

		#laowang zhuang zidan
		laoWang.anZhuang_ziDan(danJia, ziDan)

	#laowang zhuang danjia
	laoWang.anZhuang_danJia(ak47, danJia)

	laoWang.naGun(ak47)
	for x in range(21):
		laoWang.shoot(laoGao)	
		print(laoGao)
	#test
	# print(danJia)
	# print(ak47)
	print(laoWang)
	print(laoGao)

	# create diren

if __name__ == '__main__':
	main()
