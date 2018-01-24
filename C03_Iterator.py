# -*- coding: utf-8 -*-

# 迭代
import math
import collections
                         
# 列表
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#迭代显示
for name in L:
	print(name)

# tuple
L = ('Michael', 'Sarah', 'Tracy', 'Bob', 'Jack')
#迭代显示
for name in L:
	print(name)

# 字典
D = {'a':1, 'b':2, 'c':3}
#迭代显示key
for key in D:
	print('key:', key)

#迭代显示value
for value in D.values():
	print('value:', value)

#迭代显示key, value
for key, value in D.items():
	print('key:', key, ' value:', value)

#字符串
S = 'ABCD'
for ch in S:
	print(ch)

#判断是否是迭代
print('ABC 是迭代对象吗？', isinstance('ABC', collections.Iterable))


#循环下标
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)

for i, value in enumerate(['A', 'B', 'C'], start=1):
	print(i, value)

#练习(使用迭代查找一个list中的最小和最大值)
def findMinAndMax(L):
	if (L == []) or (L == None):
		return (None, None)
	else:
		mini = L[0]
		maxi = L[0]
		for i in L:
			if i > maxi:
				maxi = i
			if i < mini:
				mini = i
		return (mini, maxi)

if findMinAndMax([]) != (None, None):
	print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
	print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
	print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
	print('测试失败!')
else:
	print('测试成功!') 


