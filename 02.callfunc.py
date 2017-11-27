# -*- coding: utf-8 -*-

# 调用函数
import math

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

x, y = move(100, 100, 60, math.pi / 6)

# 直接输出 x, y 与 %f格式输出，显示的结果不同
print('%f, %f' % (x, y))
# %f默认输出为小数点后6位
# 输出151.961524, 70.000000
print(x, y)
# 输出151.96152422706632 70.0

# 也可以用一个值接收多个返回值
r = move(100, 100, 60, math.pi / 6)
print(r)
# 返回一个tuple值
# (151.96152422706632, 70.0)

