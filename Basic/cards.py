print("cards manager V9.0")
print("1.append a name:\n2.remove a name:\n3.update a name:\n4.find a name:\n5.quit:")

cards = []

while True:
	
	num = int(input("please input your choice:"))

	if num == 0:
		print(cards)
	elif num == 1:
		info = {}
		newName = input("please input the name you want to append:")
		newAge = int(input("please input the age:"))
		newPhone = input("please input the phone number:")
		info['name'] = newName
		info['age'] = newAge
		info['phone'] = newPhone
		cards.append(info)
		print(cards)
	elif num == 2:
		delName = input("please input the name you want to remove:")
		findFlag = 0
		for p in cards:
			if p.get("name") == delName:
				del cards[cards.index(p)]
				print(cards)
				findFlag = 1
		if findFlag == 0:
			print("he/she is not here!")
	elif num == 3:
		modifyName = input("please input the name you want to modify:")
		newOne = input("please input the new name you want:")
		findFlag = 0
		for p in cards:
			if p.get("name") == modifyName:
				p['name'] = newOne
				print(cards)
				findFlag = 1
		if findFlag == 0:
			print("he/she is not here!")
	elif num == 4:
		findName = input("please input the name you want to find:")
		findFlag = 0
		for p in cards:
			if p.get("name") == findName:
				print("%s\t%d\t%s"%(p.get('name'),p.get('age'),p.get('phone')))
				findFlag = 1
		if findFlag == 0:
			print("he/she is not here!")
	elif num == 5:
		break
	else:
		print("input error,please input a right num!")

	print("")	