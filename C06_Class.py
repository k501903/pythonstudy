#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'类和实例的练习'

__author__ = 'Jacklee'

# 导入模块
#import collections, types, sys

class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s: %s' % (self.name, self.score))

tom = Student('Tom', 90)
Lisa = Student('Lisa', 80)
tom.print_score()
Lisa.print_score()
print('%s: %s' % (tom.name, tom.score))

## 动态绑定属性
tom.age = 20

# 加入访问限制
class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))

tom = Student('Tom', 90)
Lisa = Student('Lisa', 80)
tom.print_score()
Lisa.print_score()

# 下面这句会报错,因为没有name属性了
#print('%s: %s' % (tom.name, tom.score))
# 下面这句会报错,也没有__name属性了
#print('%s: %s' % (tom.__name, tom.__score))
# 下面这句可以直接访问,但强烈不建议
print('%s: %s' % (tom._Student__name, tom._Student__score))

## 练习
## 把Student对象中的gender对外隐藏
class Student(object):
	def __init__(self, name, gender):
		self.__name = name
		self.__gender = gender
	def get_gender(self):
		return self.__gender
	def set_gender(self, gender):
		self.__gender = gender

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')