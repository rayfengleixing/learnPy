'''
装饰器, 就是一个参数是函数的函数, 在其内部把参数函数的功能, 修饰加强一番,
再返回这个加强版的函数
'''


# 装饰器的基本写法
# def outer(func):

#	def inner(*args, **kwargs):
#		# 添加修饰的功能
#		pass
#		func(*args, **kwargs)

#	return inner


# 装饰器的基本应用
def outer(func):
	def inner(*args, **kwargs):
		if age > 0:
			func(*args, **kwargs)
		else:
			print("Is's not a age num!")
	return inner


@outer	# 相当于 say = outer(say)
def say(age):
	print("Ray is %d years old"%age)


#say = outer(say)
say(4)
