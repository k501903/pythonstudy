#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'异常的练习'

__author__ = 'Jacklee'

# 导入模块
from functools import reduce

# 查找以下代码的错误


def str2num(s):
	try:
		return int(s)
	except ValueError as e:
		try:
			return float(s)
		except ValueError as e:
			raise e



def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()