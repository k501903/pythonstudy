# -*- coding: utf-8 -*-

# 定义函数

def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x
	print('end.') #永远也不会执行

print(my_abs(-10))

def nop():
	pass

def my_opt_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type for my_opt_abs(): %s' % type(x))
	if x >= 0:
		return x
	else:
		return -x
print(my_opt_abs((1, 2, 3)))


