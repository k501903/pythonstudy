#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'获取对象信息的练习'

__author__ = 'Jacklee'

# 导入模块
import types

class T(object):
	def __len__(self):
		return 100
def fn():
	pass
t = T()
# type(obj, bases, dict)函数
# 返回对象的类型
print(type(12))
print(type('12'))
print(type(None))
print(type(types))
print(type(abs))
print(type(T))
print(type(t))
print(type(fn))

print(type(t) == T)
print(type(12) == int)

# 类型
# types.FunctionType, types.BuiltinFunctionType, types.LambdaType, types.GeneratorType
print('fn is FunctionType? ', type(fn) == types.FunctionType)
print('abs is BuiltinFunctionType? ', type(abs) == types.BuiltinFunctionType)
print('lambda x: x is LambdaType? ', type(lambda x: x) == types.LambdaType)
print('(x for x in range(10)) is GeneratorType? ', type((x for x in range(10))) == types.GeneratorType)


# isinstance(obj, classinfo)函数
## classinfo是元组时，只要有obj的类型就为真, 顺序没有影响
print('isinstance(12, (int, object))', isinstance(12, (int, str)))
print('isinstance(abs, (int, types.BuiltinFunctionType))', isinstance(abs, (int, types.BuiltinFunctionType)))

# dir([obj])
#返回
#['T', '__annotations__', '__author__', '__builtins__', '__cached__', '__doc__', 
#'__file__', '__loader__', '__name__', '__package__', '__spec__', 'fn', 't', 'types']
print(dir())

print(dir(t))
print('t的长度: ', len(t))

# hasattr(obj, prop)
print('对象t有x属性吗? ', hasattr(t, 'x'))
# setattr(obj, prop, value)
setattr(t, 'x', 10)
# getattr(obj, prop[, default])
print('t对象的x属性值: ', getattr(t, 'x'))
# getattr, 没有属性值时，返回404，不报错
print('t对象的y属性值: ', getattr(t, 'y', 404))

print('现在, 对象t有x属性吗? ', hasattr(t, 'x'))

# 最好的方式
if hasattr(t, 'x'):
	print(getattr(t, 'x'))


