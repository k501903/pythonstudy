#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'文件读写的练习'

__author__ = 'Jacklee'

# 导入模块
# import unittest

# BIF: open() 打开文件
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

try:
	f = open(r'c:\windows\system.ini', 'r')
	s = f.read()
	print(s)
finally:
	f.close()

# with语句. 自动调用f.close. 简化代码
with open(r'C:\Windows\System.ini', 'r') as f:
	s = f.read()
	print(s)


# 操作二进制文件
# mode = rb
with open(r'c:\桌面.png', 'rb') as f:
	s = f.read(100)
	print(s)

# 读取文件
# 一次读取所有文件
with open(r'c:\桌面.png', 'rb') as f:
	s = f.read(1024)
	print(s)
