#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'模块的学习代码'

__author__ = 'JackLee'

# 模块的使用

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print('Hello, world!')
	elif len(args) == 2:
		print('Hello, %s!' % args[1])
	else:
		print('Too many arguments!')

# __name__ 当前模块的名称，如果是入口模块，则为__main__
# 可以使用这个属性，用来进行单元测试，单元测试的代码不影响其被其他模块引用
if __name__ == '__main__':
	test()


print('命令行参数如下:')
for i in sys.argv:
	print(i)

# sys.path 包含了Python解释器自动查找所需模块的路径的列表
print('\n\nPython 路径为: ', sys.path, '\n')


import numpy

print(dir(numpy))