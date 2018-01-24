#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'struct内建模块的练习'

__author__ = 'Jacklee'


# struct模块
# 用途: 
# 处理bytes和其他二进制数据类型的转换
# 使用格式化串进行转换。
# 1. 第一个字符表示字节顺序、尺寸和对齐方式
# 2. 后面的字符表示格式化

# 第一个字节
# 字符			字节顺序					尺寸			对齐方式
# @				native					native		native
# =				native					standard	none
# <				little-endian			standard	none
# >				big-endian				standard	none
# !				network (= big-endian)	standard	none

# 格式化串
# 格式		C类型				Python类型			标准大小			注释
# x			pad byte			no value	 	 
# c			char				bytes of length 1	1	 
# b			signed char			integer				1				(1),(3)
# B			unsigned char		integer				1				(3)
# ?			_Bool				bool				1				(1)
# h			short				integer				2				(3)
# H			unsigned short		integer				2				(3)
# i			int					integer				4				(3)
# I			unsigned int		integer				4				(3)
# l			long				integer				4				(3)
# L			unsigned long		integer				4				(3)
# q			long long			integer				8				(2), (3)
# Q			unsigned long long	integer				8				(2), (3)
# n			ssize_t				integer	 							(4)
# N			size_t				integer	 							(4)
# e			(7)					float				2				(5)
# f			float				float				4				(5)
# d			double				float				8				(5)
# s			char[]				bytes	 	 
# p			char[]				bytes	 	 
# P			void *				integer	 							(6)

# pack()函数将其他类型转换为bytes类型
# pack(fmt, v1, v2, ...)
import struct

# 将整数转换成字节数组
# 格式串 一定 要和后面的参数对应
# > 表示按big-endian顺序
# I 表示4字节无符号整数
bs = struct.pack('>I', 10240099)
print(r'10240099转换为bytes(>I):', bs)

# > 表示按big-endian顺序
# I 表示4字节无符号整数
# H 表示2字节无符号整数
# 格式串需要6个字节，所以后面的参数必须是6字节数组
# 否则会报错: struct.error: unpack requires a buffer of 6 bytes
re = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(re)

# h 表示2字节整数
# l 表示4字节整数
# 格式串hhl表示，需要三个整数
# 注意: 在MacOS中，加不加`>`符号结果差别很大
bs = struct.pack('>hhl', 1, 2, 3)
print(bs)

# 看一个具体的案例
# 使用struct来分析位图(.bmp)文件的格式
# BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
# 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
# 一个4字节整数：表示位图大小；
# 一个4字节整数：保留位，始终为0；
# 一个4字节整数：实际图像的偏移量；
# 一个4字节整数：Header的字节数；
# 一个4字节整数：图像宽度；
# 一个4字节整数：图像高度；
# 一个2字节整数：始终为1；
# 一个2字节整数：颜色数。

# 按照字节的格式就能够组合出格式化串

fmt = '<ccIIIIIIHH'
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

head = struct.unpack(fmt, s)
print('BMP文件头的格式:', head)

# 练习
# 编写一个函数, 检查任意文件是否位图文件，如果是，打印出图片大小和颜色数

import base64, struct
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

def bmp_info(data):
	# 首先取出头部的30个字节
	s = data[:30]
	# 使用格式化串转换
	fmt = '<ccIIIIIIHH'
	head = struct.unpack(fmt, s)
	# 判断是否是BMP文件
	if (head[0] == b'B') and (head[1] in (b'M', b'A')):
		return {
			'width': head[6],
			'height': head[7],
			'color': head[9]
		}
	else:
		return '不是一个BMP文件'

## 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')

