#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'操作文件和目录的练习'

__author__ = 'Jacklee'

import sys
# 在os模块中
import os

# 1. 查看操作系统名称os.name
print(os.name)
# 2. 查看系统详细信息os.uname()
# Windows不支持
print(os.uname())
# 3. 环境变量os.environ
print(os.environ)
# 获取某个变量的值
print('Path:', os.environ.get('PATH'))

# 操作文件和目录
# 一部分在os一部分在os.path中
# 1. 查看当前目录的绝对路径
d = os.path.abspath('.')
print('当前目录:', d)
# 2. 拼接新目录
d = os.path.join(d, 'testdir')
print('创建新目录')
# 3. 创建目录
if os.path.exists(d):
	print('目录存在:', d)
	os.rmdir(d)
try:
	print('创建目录:', d)
	os.mkdir(d)
	os.chdir(d)
	print('当前目录:', os.path.abspath('.'))
	os.chdir('..')
finally:
	os.rmdir(d)

# 4. 当前目录下的所有内容
d = os.path.abspath('.')
l = os.listdir(d)
print('当前目录:', d, '中的内容: ', l)

# 5. 拆分目录split
if __name__ == '__main__':
	c = os.path.realpath(sys.argv[0])
	print('当前目录:', c)
# 拆分目录和文件
	d = os.path.split(c)
	print(d)
# 拆分目录
	e = os.path.split(d[0])
	print(e)

# 文件操作
# 1. 重命名文件rename
try:
	os.rename('test.txt', 'test.py')
	os.remove('test.py')
except FileNotFoundError as e:
	print(e)

# 2. 列出所有目录
ds = [x for x in os.listdir('.') if os.path.isdir(x)]
print('列出当前目录下的子目录:', ds)

# 3. 列出所有文件
fs = [x for x in os.listdir('.') if os.path.isfile(x)]
print('列出当前目录下的文件:', fs)

# 4. 列出所有指定后缀文件
es = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print('列出当前目录下的.py文件:', es)


# 练习：查找指定目录下的所有子目录和文件，找出文件名中包含指定字符串的文件以及其相对目录
# 解决相对路径的问题
# 判断目录是否存在, 存在则切换目录到查找目录下
def searchAll(path, str):
	if not os.path.exists(path):
		print('目录:', path, '不存在!')
	print('查找', path, '中所有包含', str, '的文件')
	print('==================================')
	os.chdir(path)
	searchFiles('.', str)

def searchFiles(path, str):
	# 首先进入当前目录
	# 首先列出所有的文件和目录
	files = os.listdir(path)
	#print('listdir', files)
	# 逐一筛选
	for file in files:
		# 生成子目录的相对路径
		p = os.path.join(path, file)
		#print('join', p)
		# 如果是目录，则继续查找. 查找前必须将目录替换成相对目录
		if os.path.isdir(p): 
			# 递归调用
			searchFiles(p, str)
		# 如果是文件
		else:
			# 判断是否包含str
			if str in p:
				print('相对目录:', path, '文件名:', file)

searchAll('/Users/lijie/Work', '.py')


