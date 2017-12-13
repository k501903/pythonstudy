#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'__slots__绑定限制的练习'

__author__ = 'Jacklee'

# 导入模块
#import types

# 绑定限制
class Student(object):
	__slots__ = ('name', 'age')

s = Student()
#s.score = 99
Student.score = 99

class A(object):
	__slots__ = ()
	pass

class B(A):
	#__slots__ = ('x', 'y')
	pass

class C(B):
	__slots__ = ('z')
	pass

a = A()
b = B()
c = C()

b.x = 1