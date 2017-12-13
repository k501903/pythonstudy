#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'模块的学习代码'

__author__ = 'JackLee'

def _printAuthor():
	print(__author__)

def _printTest():
	print(__doc__) #模块的注释文档，也就是第一个字符串

if __name__ == '__main__':
	_printTest()
else:
	_printAuthor()

