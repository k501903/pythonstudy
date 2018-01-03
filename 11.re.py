#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'正则表达式的练习'

__author__ = 'Jacklee'


# re模块

# 需要了解正则表达式字符规则
# 这里就不表了

# 使用re模块
import re
# 以3个数字开头，后跟-，以3-8个数字结尾
# 调用re.match方法，如果匹配，则返回一个match对象，否则返回None
if re.match(r'^\d{3}\-\d{3,8}$', '010-12345'):
	print('OK')
else:
	print('Failed')

# 切分字符串
# 可以识别多个连续空格
r = re.split(r'\s+', 'a b   c')
print(r)

r = re.split(r'[\s\,\;]+', 'a,b,;c  , d')
print(r)

# 分组
# 使用()规则
# 将字符串按照分组进行分割,便于提取
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
if m:
	print(m.groups())

# 贪婪匹配
# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
# 使用?就可以让\d+采用非贪婪匹配
# 对比一下代码就可以看出区别
print(re.match(r'^(\d+)(0*)$', '102300').groups())

print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# 编译
# 如果表达式需要执行很多遍，出于效率的考虑，可以先行编译

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())

# 练习
# 验证email地址

def is_valid_email(addr):
	rule = r'^[a-zA-z\.]+\@[a-zA-z]+(\.com|\.cn)$'
	if re.match(rule, addr):
		return True
	else:
		return False

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

# 练习
# 提取出邮件中的名称

def name_of_email(addr):
	print(re.split(r'[\<\>\@]+', addr))
	return re.split(r'[\<\>\@]+', addr)[0]
	
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')


