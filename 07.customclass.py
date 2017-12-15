#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'定制类的练习'

__author__ = 'Jacklee'

# 导入模块
#import types

# 定制长度__len__
class CustomLen(object):
	def __len__(self):
		return 100

# 测试长度 == 100
if len(CustomLen()) == 100:
	print('长度测试成功')
else:
	print('长度测试失败')

# 定制打印实例返回结果
class NormalPrint(object):
	pass
class CustomPrint(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'CustomPrint object (name: %s)' % self.name

# 测试打印实例
print(NormalPrint())
print(CustomPrint('Bob'))


# 迭代
class CustomIter(object):
	def __init__(self):
		self.a, self.b = 0, 1
	def __iter__(self):
		return self
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100000:
			raise StopIteration()
		return self.a

# 测试
for i in CustomIter():
	print(i)

# TypeError: 'CustomIter' object does not support indexing	
# print(CustomIter()[0])

# 迭代，按下标访问
class CustomItem(object):
	def __getitem__(object, n):
		a, b = 1, 1
		for x in range(n):
			a, b = b, a + b
		return a

# 测试下标访问
print(CustomItem()[5])

# 迭代，按下标访问，支持切片[start:stop]
class CustomSlice(object):
	def __getitem__(object, n):
		if isinstance(n, int): #下标访问
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice): #切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L

# 测试切片访问
print(CustomSlice()[0:5])


# 自定义属性
class CustomAttr(object):
	def __init__(self):
		self.name = 'Michael'
	def __getattr__(self, attr):
		if attr == 'score':
			return 99
		raise AttributeError('\'CustomAttr\' object has no attribute \' %s \'' % attr)

cus = CustomAttr()
print(cus.score)

# 
class Chain(object):
	def __init__(self, path = ''):
		self._path = path
	def __getattr__(self, attr):
		return Chain('%s/%s' % (self._path, attr))
	def __str__(self):
		return self._path
	# __repr__ = __str__

print(Chain().status.user.timeline.list)


# 自定义类
class Chain(object):
	def __init__(self, ch = ''):
	    self._ch = ch
	def __getattr__(self, ch = ''):
	    return Chain('%s/%s' % (self._ch, ch))
	def __call__(self, *c):
	    s = ''
	    for i in c: 
	    	s += ':' + i
	    return self.__getattr__(s)
	def __str__(self):
	    return self._ch
	__repr__=__str__

Chain().status.user.timeline.list
print('++++华丽丽的分割符号++++')
print(Chain().status.user.timeline.list)
print('++++华丽丽的分割符号++++')
print(Chain().users('michael').repos)
print('++++华丽丽的分割符号++++')
print(Chain().users('michael', 'zhangsan').repos.lession('math').teacher('qin'))