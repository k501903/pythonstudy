#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'枚举类的练习'

__author__ = 'Jacklee'

# 导入模块
#import types

# 月份常量
JAN = 1
FEB = 2
MAR = 3

# 枚举类
from enum import Enum, unique

## 第一种定义方式
@unique
class Month(Enum):
	JAN = 0
	FEB = 1
	MAR = 2

## 第二种定义方式
WeekDay = Enum('WeekDay', ('Mon', 'Tue', 'Wed', 'Tru', 'Fri', 'Sat', 'Sun'))

## 类的组成，JAN ... 是一个类成员
print('Month类的成员: ', dir(Month))

m = Month(0)
print(m.name, m.value)
print('Month对象实例的成员: ', dir(m))

m = Month(1)
print(m.name, m.value)

m = Month(2)
print(m.name, m.value)

