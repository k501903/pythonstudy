#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'继承和多态的练习'

__author__ = 'Jacklee'

# 导入模块
#import collections, types, sys

# 基类
class Animal(object):
	def run(self):
		print('Animal is running...')

# 子类
class Dog(Animal):
	def run(self):
		print('Dog is running...') 

# 子类
class Cat(Animal):
	def run(self):
		print('Cat is running...')

animal = Animal()
dog = Dog()
cat = Cat()

## 继承关系
## 通过isinstance查看
print('dog is a Dog.', isinstance(dog, Dog))
print('dog is a Animal.', isinstance(dog, Animal))

print('animal is a Animal.', isinstance(animal, Animal))
print('animal is a Dog.', isinstance(animal, Dog))


## 多态
def run_twice(animal):
	animal.run()
	animal.run()

## 传入对象不同，执行结果不同
run_twice(animal)
run_twice(dog)
run_twice(cat)


## 鸭子类型
class Car(object):
	def run(self):
		print('Car is running...')

car = Car()
run_twice(car)