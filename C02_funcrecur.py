# -*- coding: utf-8 -*-

# 调用函数
import math

# 递归函数
def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)

print(fact(100))

# 尾递归优化
def fact(n):
	return fact_iter(n, 1)

# 符合两个条件：调用自身本身、返回不包含表达式
def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)

print(fact(3))

# 练习--汉诺塔
# 没有想明白
def move(n, a, b, c):
	if n == 1:
		print(a, ' --> ', c)
	else:
		move(n - 1, a, c, b)
		move(1, a, b, c)
		move(n - 1, b, a, c)

move(5, 'A', 'B', 'C')
