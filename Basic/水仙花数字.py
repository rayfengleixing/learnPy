# -*- coding:utf-8 -*-

'''
输入一个最大范围, 求取其中所有的水仙花数字
水仙花数字: 	一个三位数的每一位数的3次幂之和, 等于这个数本身.
四叶玫瑰花数字: 一个四位数的每一位数的4次幂之和, 等于这个数本身.
五角星数:		一个五位数的每一位数的5次幂之和, 等于这个数本身.
六合数:		一个六位数的每一位数的6次幂之和, 等于这个数本身.
北斗七星数:	一个七位数的每一位数的7次幂之和, 等于这个数本身.
八仙数:		一个八位数的每一位数的8次幂之和, 等于这个数本身.
九九重阳数:	一个九位数的每一位数的9次幂之和, 等于这个数本身.
十全十美数:	一个十位数的每一位数的10次幂之和, 等于这个数本身.
......
'''

max_num = int(input("please input the max_num(the smallest one is 153):"))

for num in range(153, max_num):
	summ = 0
	length = len(str(num))
	temp = num
	if length >= 3:
		for i in range(length):
			summ += (temp % 10) ** length
			temp //= 10
		if summ == num:
			print(num)