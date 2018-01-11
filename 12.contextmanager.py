#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'contextlib内建模块的练习'

__author__ = 'Jacklee'


# contextlib模块
# 提供上下文管理器

# 1. with语句
# 2. 上下文管理器
# 3. contextlib.contextmanager
# 4. closing

## with语句
# 从Python2.6开始，可以使用with语句，实现对资源的有效管理（打开和关闭）
# 等同于使用try ... finally语句
# 语法如下:
# with expression [as variable]:
# 		with-block
# :expression 是上下文管理器
# :[as variable] 是可选项，如果指定了变量，则expression调用__enter__()函数返回的对象
# : with-block 是执行语句
# with-block执行完后，with语句会自动进行资源清理

# 举例
# 使用try ... finally语句
f = open('test.txt', 'rb')
try:
	for line in f.readlines():
		print(line.decode('utf-8'))
finally:
	f.close()

# 使用with语句
with open('test.txt', 'rb') as f:
	for line in f.readlines():
		print(line.decode('utf-8'))


## 上下文管理器
# 实现了上下文协议的类
# 即实现了__enter__()和__exit__()两个函数的类
# 只要实现了上面的两个函数，就可以使用with语句进行上下文管理
# 执行顺序
# 1. 生成一个上下文管理器expressioin
# 2. 执行expression.__enter__()函数。如果指定了[as variable]则将__enter__()函数的返回值赋值
# 3. 执行with-block语句块
# 4. 执行expression.__exit__()函数，进行资源清理工作

# 举例
# 一个正常的数据库操作代码
# 1. 创建一个数据库链接
# 2. 获取数据库操作的句柄
# 3. 执行SQL语句
# 4. 事务提交
# 5. 异常则回滚
def test_write():
	con = MySQLdb.connection()
	cursor = con.cursor()
	sql = ''
	try:
		cursor.execute(sql)
		...
		con.commit()
	except Exception as ex:
		con.rollback()

# 如果用上下文管理器如何实现呢
# 首先实现上下文管理器
class DBConnection(object):
	def __init__(self):
		pass
	def cursor(self):
		pass
	def commit(self):
		pass
	def rollback(self):
		pass
	def __enter__(self):
		cursor = self.cursor()
		return cursor
	def __exit__(self, type, value, tb):
		if tb is None:
			self.commit()
		else:
			self.rollback

# 再实现上面的函数
def test_write():
	sql = ''
	con = DBConnection()
	with con as cursor:
		cursor.execute(sql)
		...


## contextlib.contextmanager对象
# 如果通过添加__enter__和__exit__函数的方式来定义上下文管理器，不是非常方便
# 需要创建一个新的类型
# contextmanager通过装饰器decorator方式进行添加
# 在定义expression前加入@contextmanager即可
# 定义一个生成器generator
# @contextmanager
# def some_generator(<arguments>):
# 	<setup> 这段代码等同于上下文管理器中的__enter__函数
# 	try:
# 		yield <value>  返回值等同于__enter__函数的返回值
# 	finally:
# 		<cleanup> 这段代码等同于上下文管理器的__exit__函数

# 然后就可以用with语句调用contextmanager生成的上下文管理器了
# with some_generator(<arguments>) as <variable>:
# 	<body>

# 举例说明
# 锁资源自动获取和释放的例子
@contextmanager
def locked(lock):
	lock.acquire()
	try:
		yield
	finally:
		lock.release()

with locked(mylock):
	pass

@contextmanager
def myopen(filename, mode='r'):
	f = open(filename, mode)
	try:
		yield f
	finally:
		f.close()

with myopen('test.txt') as f:
	for line in f:
		print(line)

## contextmanager.closing对象
# 只有__exit__函数
# 适用于具有close()方法的资源对象
import urllib, sys
from contextlib import closing

with closing(urllib.urlopen('http://www.baidu.com')) as f:
	for line in f:
		sys.stdout.write(line)


