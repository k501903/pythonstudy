#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'base64内建模块的练习'

__author__ = 'Jacklee'


# base64模块
# 采用64个字符表示任意二进制数据的方法
# 用途:
# 在URL、Cookie、网页中传输少量二进制数据
# 数据没有采用任何加密措施, 尽量不要用于保存密码
# 64个字符包括: A-Z a-z 0-9 + /
# 原理: 
# 1. 对二进制数据进行处理：三个字节一组共24bit
# 2. 将24bit划分为4组每组6bit，正好表示0-63
# 3. 以四个数值0-63为索引，从字符表中查找对应的字符
# 如果二进制数据不是3的倍数，使用\x00字节在末尾补足
# 编码后的字符串的长度是4的倍数，如果不够在编码的末尾补足`=`号
# 编码中补足的`=`不参与解码

# URL安全的base64编码
# URL中`+`和`/`有特殊的含义，因此使用`-`和`_`替换
# `=`在URL和Cookie中容易造成歧义，所以很多编码将`=`去掉
# 在解码时补足`=`即可

import base64
# base64对象
# 编码: b64encode()
# 解码: b64decode()
en = base64.b64encode(b'binary\x00string')
print(r'binary\x00string编码为base64为:', en)

de = base64.b64decode(en)
print(en, '解码为:', de)

# url安全的编解码
# 编码: urlsafe_b64encode()
# 解码: urlsafe_b64decode()
en = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(r'i\xb7\x1d\xfb\xef\xff编码为urlsafe-base64为:', en)

de = base64.urlsafe_b64decode(en)
print(en, '解码为:', de)

# 练习
# 写一个能处理掉`=`的base64解码函数

def safe_base64_decode(s):
	s = s + b'='*(4 - len(s) % 4) 
	return base64.b64decode(s)

## 测试
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')

