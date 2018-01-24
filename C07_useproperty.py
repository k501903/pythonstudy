#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'@property的练习'

__author__ = 'Jacklee'

# 导入模块
#import types

# 装饰器@property
class Student(object):
	__slots__ = ('name', '_birth', '_age', '_score')
	def Test():
		pass

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('成绩必须是整数！')
		if (value < 0) or (value > 100):
			raise ValueError('成绩必须在0 - 100之间！')
		self._score = value

	@property 
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self, value):
		self._birth = value

	@property
	def age(self):
		return 2017 - self._birth

s = Student()
s.birth = 1976
print(s.age)

#练习
##请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
	@property 
	def width(self):
		return self._width
	
	@width.setter
	def width(self, value):
		self._width = value

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, value):
		self._height = value

	@property
	def resolution(self):
		return self._width * self._height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

