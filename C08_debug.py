#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'调试的练习'

__author__ = 'Jacklee'

# 导入模块
import logging
logging.basicConfig(level = logging.INFO)

# 使用print()
def _do():
	s = 0
	n = 1
	print('s=',s, 'n=', n)
	print('END')

_do()

# 使用断言
def _do():
	s = 0
	n = 1
	assert s == 0, 's的值%d错误.' % s  #抛出异常
	print('END')

_do()

# 使用logging
def _do():
	s = 0
	n = 1
	logging.info('s=%d. n=%d' % (s, n))
	print('END')

_do()