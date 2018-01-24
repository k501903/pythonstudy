#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'文件读写的练习'

__author__ = 'Jacklee'


# BIF: open() 打开文件
# 原生操作文件的函数
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# file: 文件名称(相对目录/绝对目录)
# mode: 
# 		r - 以读取方式打开(默认)
#		w - 以写入方式打开, 操作指针在文件开头
#		x - 以写入方式打开, 文件必须不存在
#		a - 以写入方式打开, 操作指针在文件结尾
#		b - 以二进制模式操作文件
#		t - 以文本模式操作文件(默认)
#		+ - 以更新模式打开, 可以读、写

txtfile = r'00.py'
binfile = r'menu.png'
writefile = r'test.txt'

# <_io.TextIOWrapper =name'00.py' mode='r' encoding='US-ASCII'>
try:
	f = open(txtfile, 'r')
	print(f)
finally:
	f.close()

# with语句. 自动调用f.close. 简化代码
# mode参数默认为rt
with open(txtfile) as f:
	print(f)

# 操作二进制文件
# mode = rb
# <_io.BufferedReader name='menu.png'>
with open(binfile, 'rb') as f:
	print(f)

# 读取文件
# 使用编码设置读取文件
# 对于文本文件，如果不指定编码格式，默认为ASCII，如果出现中文等会报错
with open(txtfile, 'r', encoding='UTF-8') as f:
	s = f.read()
	print('读取的字符长度为: ', len(s))

# 对于配置文件/文本文件等
# 可以使用readline / readlines进行读取
with open(txtfile, encoding='UTF-8') as f:
	s = f.readline()
	print('第一行内容: ', s)
# f.tell()返回当前文件的位置
	print('当前指针位置: ', f.tell())
# f.seek(0, 0)设置文件当前位置
# 第一个参数: 表示偏移量.
# 第二个参数: 表示从哪儿开始(0-文件开始; 1-当前位置; 2-文件末尾). 默认为0
# f.seek(0, 0) 表示设置文件当前位置为文件开始
	f.seek(0, 0)
	print('f.seek(0, 0) 指针返回文件开头')
	s = f.readline()
	print('第一行内容: ', s)
	print('当前指针位置: ', f.tell())

# str.strip(rm)函数
# 删除字符串(str)中开头或结尾处的rm(字符)
# 如果rm为空，则删除开头或结尾处的空白符('\n', '\r', '\t', '')
	for line in f.readlines():
		print(line.strip())

# 读取二进制文件
# 如果文件大小不确定，考虑到性能和内存容量，每次仅读取一定长度的数据
with open(binfile, 'rb') as f:
	s = f.read(1024)
	print(s)

# 写文件
# 如果写入特定编码的文本文件, 需要传入encoding参数, 将字符串自动转换成指定编码
with open(writefile, 'w', encoding = 'UTF-8') as f:
	f.write('Hello, world!')

# 如果是二进制文件
# 写入的是一个字节对象. "a bytes-like object is required"
with open(writefile, 'wb') as f:
	f.write('Hello, world!'.encode('ASCII'))
