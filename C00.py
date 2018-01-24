#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习用的模块'

__author__ = 'Jacklee'

# 导入模块
import collections, types, sys

L = list(filter(lambda x: x % 2 == 1, range(1, 20)))


print(L)

L = list(n for n in range(1, 20) if n % 2 == 1)

print(L)

def now():
	print('aaaa')

print(now.__name__)


print(isinstance(now, types.FunctionType))


print(__name__)


print(sys.argv)

class Test(object):
	pass

Test.name = 'aafadf'

print(Test.name)

class A(object):
	pass

class B(A):
	pass

print(B.__mro__)

