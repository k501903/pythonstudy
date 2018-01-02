#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'序列化的练习'

__author__ = 'Jacklee'

# 把变量从内存编程可存储或传输的过程称之为”序列化“
# Python提供pickle模块实现序列化
# pickle模块将对象序列化成Python特有的格式，不同语言间是不兼容的
# 也就是说，用Python序列化的对象，只能用Python反序列化
import pickle

d = dict(name='Bob', age=20, score=88)
# dumps方法可以把任意对象序列化成一个bytes
p = pickle.dumps(d)
print('Python序列化:', p)

# 可以将序列化的字节列表写入文件中
# open一个文件，设置为w写入b二进制
with open('dump.txt', 'wb') as f:
	# dump方法，将一个对象写入文件
	pickle.dump(d, f)

# 将一个序列化的文件反序列化成一个对象
with open('dump.txt', 'rb') as f:
	d = pickle.load(f)
print('从文件反序列化对象:', d)

# JSON
# 使用json内置模块
# 为了将一个对象序列化成标准格式，能够被多种不同语言兼容
# JSON类型				Python类型
# {}					dict
# []					list
# "string"				str
# 1234.56				int或float
# true/false			True/False
# null					None

# dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, 
# allow_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', 
# default=None, sort_keys=False, **kw)

# loads(s[, encoding[, cls[, object_hook[, parse_float[, parse_int[, 
# parse_constant[, object_pairs_hook[, **kw]]]]]]]])

import json
# dumps序列化
d = dict(name='Bob', age=20, score=88)
j = json.dumps(d)
print('Json序列化:', j)

# loads反序列化
p = json.loads(j)
print('从JSON反序列化对象:', p)

# 要把一个类序列化成JSON
class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

s = Student('Bob', 20, 88)
# print(json.dumps(s))
# 直接序列化会报错，Student' is not JSON serializable
# 这是因为类不知道如何序列化，需要指定一个转换函数
def student2dict(stu):
	return {
		'name': stu.name,
		'age': stu.age,
		'score': stu.score
	}
json_str = json.dumps(s, default=student2dict)
print('将Student类序列化成JSON:', json_str)

# 反序列化
# 同样得需要一个转换函数
def dict2student(d):
	return Student(d['name'], d['age'], d['score'])
# 使用loads反序列化
s = json.loads(json_str, object_hook=dict2student)
print('反序列化Student类:', s)
print('Student类', s.name, s.age, s.score)

# 在序列化中，如何处理中文呢
# 使用dumps函数中的ensure_ascii参数
# 默认ensure_ascii参数为True, 当遇到中文时编码为unicode字符
# 如果要使中文可见，需要设置ensure_ascii为False
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)








