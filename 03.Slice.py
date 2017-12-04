# -*- coding: utf-8 -*-

# 切片
import math

# 列表
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#取前三个
print('取前三个')
print(L[0:3])
#取第一个
print('取第一个')
print(L[:1])

#取后两个
print('取后两个')
print(L[-2:])
#取最后一个
print('取最后一个')
print(L[-1:])

#取1、3、5
print('取第1、3、5个')
print(L[::2])

# tuple
T = ('Michael', 'Sarah', 'Tracy', 'Bob', 'Jack')
#取前三个
print(T[0:3])
print(T[:3])

#取后两个
print(T[-2:])

#取1、3、5
print(T[::2])

# 字符串
S = 'ABCDE'
#取前三个
print(S[0:3])
print(S[:3])

#取后两个
print(S[-2:])

#取1、3、5
print(S[::2])

# 练习
# 去除字符串首尾的空格
def trim(s):
	if s == '':
		return s
	elif s[0] == ' ':
		return trim(s[1:])
	elif s[-1:] == ' ':
		return trim(s[:-1])
	else:
		return s

if trim('hello   ') != 'hello':
	print('测试失败!')
elif trim('  hello') != 'hello':
	print('测试失败!')
elif trim('  hello  ') != 'hello':
	print('测试失败!')
elif trim('    ') != '':
	print('测试失败!')
elif trim('') != '':
	print('测试失败!')
else:
	print('测试成功!')
