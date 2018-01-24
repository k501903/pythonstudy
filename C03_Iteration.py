# -*- coding: utf-8 -*-

# 迭代器

# 迭代对象Iterable                         
from collections import Iterable
print('[]是Iterable吗? ', isinstance([], Iterable))
print('{}是Iterable吗? ', isinstance({}, Iterable))
print('abc是Iterable吗? ', isinstance('abc', Iterable))
print('(x for x in range(10))是Iterable吗? ', isinstance((x for x in range(10)), Iterable))
print('100是Iterable吗? ', isinstance(100, Iterable))

# 迭代器Iterator
from collections import Iterator
print('[]是Iterator吗? ', isinstance([], Iterator))
print('{}是Iterator吗? ', isinstance({}, Iterator))
print('abc是Iterator吗? ', isinstance('abc', Iterator))
print('(x for x in range(10)是Iterator吗? ', isinstance((x for x in range(10)), Iterator))

# 迭代器转化
print('iter([])是Iterator吗? ', isinstance(iter([]), Iterator))