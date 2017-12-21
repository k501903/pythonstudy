#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'内存读写的练习'

__author__ = 'Jacklee'


# StringIO和BytesIO
# 是file-like 对象
# 可以像操作文件一样操作内存中的字符串和字节列表

# StringIO
from io import StringIO

# 创建一个空的对象
f = StringIO()
# 写入内容
f.write('Hello')
f.write(' ')
f.write('world!')
# 获得所有内容
# 不用考虑指针的位置
print(f.getvalue())
# 移动指针位置
f.seek(0, 0)
# 读取所有内容
print(f.read())

# 创建一个有初始字符串的对象
f = StringIO('Hello world!')
# 写入内容
f.write('Hi Jack!')
# 当前的内容是什么呢？
# Hi Jack!rld!
# 创建该对象后, 读写操作的指针在开始的位置: 0
# 如果这时候写入, 会覆盖已有的内容, 最神奇的是, 之前的内容并没有全部被覆盖(清空)
print(f.getvalue())

# 如果有初始字符串, 需要在后面添加, 就需要一开始就移动指针位置
f = StringIO('Hello world!')
# 移动到结尾处
f.seek(0, 2)
f.write('Hi Jack!')
print(f.getvalue())

