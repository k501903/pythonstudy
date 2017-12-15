#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'元类的练习'

__author__ = 'Jacklee'

# 导入模块
#import types

# 静态定义的类
# 定义了Hello类，有一个方法hello，传入一个名称参数，打印输入'Hello, ' & name
class Hello(object):
	def hello(self, name = 'world'):
		print('Hello, %s' % name)

# type()函数动态创建

# 先定义方法函数
def fn(self, name = 'world'):
	print('Hello, %s' % name)

# 动态创建Hello类
Hello = type('Hello', (object, ), dict(hello = fn))

h = Hello()
h.hello('Bob')

Hello = type('Hello', (object, ), dict(name = 'world'))

h = Hello()
print(h.name)

# metaclass元类动态创建

## 定义元类
class ListMetaClass(type):
	def __new__(cls, name, bases, attrs):
		# print(cls, name, bases, attrs)
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass = ListMetaClass):
	pass

mylist = MyList()
mylist.add(1)
print(mylist)

# print(dir(ListMetaClass))
# print(dir(MyList))

## 自定义一个ORM架构

# 将类的定义 修改为 对数据库的操作

# 第一步: 定义Field类
class Field(object):
	def __init__(self, name, column_type):
		self.name = name
		self.column_type = column_type
	def __str__(self):
		return '<%s:%s>' % (self.__class__.__name__, self.column_type)

# 第二步: 定义各种类型Field类
class StringField(Field):
	def __init__(self, name):
		super().__init__(name, 'varchar(100)')

class IntegerField(Field):
	def __init__(self, name):
		super().__init__(name, 'bigint')


# 第三步: 定义元类
class ModelMetaClass(type):
	def __new__(cls, name, bases, attrs):
		print(cls, name, bases, attrs)
		if name == 'Model':
			return type.__new__(cls, name, bases, attrs)
		print('Found model: %s.' % name)

		mappings = dict()

		for k, v in attrs.items():
			if isinstance(v, Field):
				print('Found mapping: %s ==> %s' % (k, v))
				mappings[k] = v

		for k in mappings.keys():
			attrs.pop(k)

		attrs['__mappings__'] = mappings
		attrs['__table__'] = name

		return type.__new__(cls, name, bases, attrs)

# 定义Model类
class Model(dict, metaclass = ModelMetaClass):
	def __init__(self, **kw):
		super(Model, self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError('Model object no attribute %s' % key)

	def __setattr__(self, key, value):
		self[key] = value

	def save(self):
		fields = []
		params = []
		args = []
		for k, v in self.__mappings__.items():
			fields.append(v.name)
			params.append('?')
			args.append(getattr(self, k, None))
		sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
		print('SQL: %s' % sql)
		print('ARGS: %s' % args)

# 定义用户类
class User(Model):
	id = IntegerField('id')
	name = StringField('name')
	#email = StringField('email')
	password = StringField('password')


user = User(id = 12345, name = 'Michael', email = 'test@orm.org', password = 'my-pwd')
user.save()