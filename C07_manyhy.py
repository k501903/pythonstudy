#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'多重继承的练习'

__author__ = 'Jacklee'

# 导入模块
#import types

# 继承关系
class D(object):
	pass
class E(object):
	pass
class F(object):
	pass
class C(D, F):
	pass
class B(E, D):
	pass
class A(B, C):
	pass

print(A.__mro__)