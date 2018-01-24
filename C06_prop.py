#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'实例属性和类属性的练习'

__author__ = 'Jacklee'

# 导入模块
#import types

# 实例属性，通过self绑定
class Student(object):
	def __init__(self, name):
		self.name = name

s = Student('Bob')
print('通过self变量绑定name: ', s.name)


# 实例属性，通过实例变量绑定
s.score = 90
print('通过实例变量绑定score: ', s.score)


# 类属性
class Student(object):
	name = '123'

print('类属性，直接访问类Student.name:', Student.name)
s = Student()
print('类属性，通过实例变量s.name:', s.name)

s.name = '345'
print('s.name = 345, 实例变量s绑定name属性后')
print('s.name: ', s.name, ' Student.name: ', Student.name)
del(s.name)
print('del(s.name)删除了实例s的属性name后')
print('s.name: ', s.name, ' Student.name: ', Student.name)

## 练习
## 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加

class Student(object):
	count = 0
	def __init__(self, name):
		self.name = name
		Student.count += 1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')