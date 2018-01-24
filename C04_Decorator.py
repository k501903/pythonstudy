# -*- coding: utf-8 -*-

# 装饰器 Decorator
# 不改变函数本身，扩展函数的功能

## __name__、闭包、@保留字、functools

import functools
import time
import types

## 定义一个函数调用日志装饰器
## 是一个闭包 两层嵌套
def log(fn): #fn即为扩展的函数名
	@functools.wraps(fn) #将函数的名称设置为原函数名，否则函数名就替换为wrapper
	def wrapper(*args, **kw): #两个参数可以覆盖所有类型的参数
		print('%s():' % fn.__name__)
		return fn(*args, **kw) #调用原函数
	return wrapper

@log # 等同于now = log(now)
def now():
	print('2017-12-11')

now()
print('now的名称: ', now.__name__)

## 定义一个可传入参数的装饰器
## 是一个闭包 三层嵌套
def log(text): #text是传入参数
	def decorator(fn): #fn是函数名
		@functools.wraps(fn) #将函数的名称设置为原函数名，否则函数名就替换为wrapper
		def wrapper(*args, **kw): #两个参数可以覆盖所有类型的参数
			print('%s %s():' % (text, fn.__name__))
			return fn(*args, **kw) #调用原函数
		return wrapper
	return decorator

@log('执行') # 等同于now = log('执行')(now)
def now():
	print('2017-12-11')

now()
print('now的名称: ', now.__name__)

## 作业
## 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
def metric(fn):
	@functools.wraps(fn)
	def wrapper(*args, **kw):
		s = time.time()
		re = fn(*args, **kw)
		e = time.time()
		print('%s executed in %s ms' % (fn.__name__, (e - s) * 1000 ))
		return re
	return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('f测试失败!')
elif s != 7986:
    print('s测试失败!')


## 作业
## 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
## 再思考一下能否写出一个@log的decorator，使它既支持@log 也支持 @log('execute')：
def log(arg): #arg是传入参数
	if isinstance(arg, str):
		def decorator(fn): #fn是函数名
			@functools.wraps(fn) #将函数的名称设置为原函数名，否则函数名就替换为wrapper
			def wrapper(*args, **kw): #两个参数可以覆盖所有类型的参数
				print('%s %s() begin call' % (arg, fn.__name__))
				re = fn(*args, **kw) #调用原函数
				print('%s %s() end call' % (arg, fn.__name__))
				return re
			return wrapper
		return decorator
	else:
		@functools.wraps(arg) #将函数的名称设置为原函数名，否则函数名就替换为wrapper
		def wrapper(*args, **kw): #两个参数可以覆盖所有类型的参数
			print('%s() begin call' % arg.__name__)
			re = arg(*args, **kw) #调用原函数
			print('%s() end call' % arg.__name__)
			return re
		return wrapper

@log('执行2') # 等同于now = log('执行')(now)
def now():
	print(time.time())

now()
print('now的名称: ', now.__name__)

@log # 等同于now = log(now)
def now():
	print(time.time())

now()
print('now的名称: ', now.__name__)

