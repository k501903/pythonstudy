# -*- coding: utf-8 -*-

# 调用函数
import math

# 必选参数
def power(x):
	return x * x
print(power(5)) # 显示：25

# 如果扩展该函数，以支持X的3次4次方，就需要增加参数 
def power(x, n):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

# 可选参数，以上两个函数如果要做到兼容
# 使用了n=2的默认参数，默认参数可以不用传入，但必须在必选参数后面
def power(x, n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
print(power(5))

# 多个可选参数，如果要设置其中的一个，必须使用参数名
def login(name, gender, age=6, city='Beijing'):
	print('name: %s, gender: %s, age:%d, city:%s' % (name, gender, age, city))
login('Sarah', 'F')
login('Sarah', 'F', city='Tianjin')

# 可选参数必须是: 不可变对象
# 否则就会像本例一样，调用的结果不随人愿
def add_end(L=[]):
	L.append('END')
	return L
print(add_end())
print(add_end())

# 修正如下，将默认值由[]列表改为不可变对象None
def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L

# 可变参数
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
nums = (1, 2, 3)
print(calc(nums))
# 对于不确定多个数据计算，可以使用如上的方法，但是必须传入一个list/tuple
# 如果使用可变参数，可以不用传入list/tuple，而是传入多个参数
def calc(*args):
	sum = 0
	for n in args:
		sum = sum + n * n
	return sum
print(calc(1, 2, 3))
# 也可以在tuple前面加入*，将tuple转换为可变参数
nums = (1, 2, 3)
print(calc(*nums))

# 关键字参数
# 传入的参数是一个dict
def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)
# 常用的调用方法
person('Michael', 30)
person('Michael', 30, city='Beijing', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Michael', 30, **extra)

# 命名关键字参数
# 没有可变参数的情况定义
def person(name, age, *, city, job):
	print('name:', name, 'age:', age, 'city:', city, 'job:', job)
person('Jack', 24, city='Beijing', job='Engineer')

# 有可变参数的情况定义
def person(name, age, *args, city, job):
	print('name:', name, 'age:', age, 'args:', args, 'city:', city, 'job:', job)
person('Jack', 24, city='Beijing', job='Engineer')

# 参数组合
# 参数顺序：位置参数、可选参数、可变参数、命名关键字参数、关键字参数
def func1(a, b, c = 0, *args, **kw):
	print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)
def func2(a, b, c = 0, *, d=0, **kw):
	print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)
func1(1, 2)
func1(1, 2, 3)
func1(1, 2, 3, 4)
func1(1, 2, 3, 4, 5)
func1(1, 2, 3, 4, 5, x=99)
func1(1, 2, 3, ext=None)
func2(1, 2)
func2(1, 2, d=99, ext='Beijing')

def func3(a, b, *, c=0):
	pass
func3(1, 2)
def func4(a, b, **kw):
	pass
func4(1, 2)

# 错误定义
# error1: 关键字参数(**kw)只能作为最后一个参数出现
# def error1(a, b, **kw, d):
#	pass
# error2: 可变参数(*args)不能出现在命名关键字参数后面
# def error2(a, b, *, d, *args):
#	pass

# 练习
def product(x, *args):
	re = x
	for n in args:
		re = re * n
	return re

print(product(1))
print(product(1, 2, 3))
