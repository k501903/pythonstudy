#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'itertools内建模块的练习'

__author__ = 'Jacklee'


# itertools模块
# 提供多个“无限”迭代器
# count()
# cycle()
# repeat()
# chain()
# groupby()

import itertools, time

# count()
# count(start=0, step=1)
# 创建一个无限迭代器，打印出自然数序列
# 会一直循环下去
na = itertools.count(2, 2)
# for n in na:
# 	time.sleep(0.1)
# 	print(n)


# cycle()
# cycle(iterable)
# 把一个序列无限重复下去
# 会一直循环下去
cs = itertools.cycle('ABC')
# for c in cs:
# 	time.sleep(0.1)
# 	print(c)

# takewhile()
# takewhile(predicate, iterable)
# 将无限循环的迭代器截取出一个有限序列
tw = itertools.takewhile(lambda x: x < 100, na)
print(list(tw))

# repeat()
# repeat(object[, times])
# 把一个元素无限重复下去
# 可以设定重复次数
ns = itertools.repeat('A', 3)
for n in ns:
	print(n)

## 其他一些迭代函数

# chain()
# chain(*iterables)
# 将一组迭代器串联起来，形成一个更大的迭代器
cc = itertools.chain('abc', 'def', 'ghi')
for c in cc:
	print(c)

# groupby()
# groupby(iterable, key=None)
# 把迭代器中相邻的重复元素挑出来分组放在一起
for key, group in itertools.groupby('aabbccabc'):
	print(key, list(group))



## 练习
## 计算圆周率
## 
from functools import reduce

def f(x):
	return 4 / x if (x + 1) % 4 != 0 else 0 - 4 / x 

def _add(x, y):
	return x + y 

def pi(N):
	'''
	计算pi的值
	1. 创建一个奇数序列: 1,3,5,7...
	2. 取该序列的前N项: 1, 3, 5, 7....
	3. 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7 ...
	4. 求和
	'''
	# 方法1: 
	# js = itertools.count(1, 2)
	# jsn = itertools.takewhile(lambda x: x < N * 2, js)
	# return reduce(_add, map(f, jsn))
	# 方法2
	# 使用cycle()的特性
	a = itertools.cycle([4, -4])
	b = itertools.count(1, 2)
	return sum(next(a) / next(b) for i in range(N))

## 测试
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')




