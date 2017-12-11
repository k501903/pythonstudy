# -*- coding: utf-8 -*-

# 偏函数 Partial
# 通过固定函数中的某些参数，从而达到简化调用的目的

import functools

print('十进制256: ', int('256'))
print('八进制256: ', int('256', 8))
print('十六进制256: ', int('256', 16))

# 固定参数为2，这样默认就是二进制了
int2 = functools.partial(int, base = 2)

print(int2('00001'))