# -*- coding: utf-8 -*-

# 列表生成式
# 适用于List / Tuple
                         
# 使用range函数
L = list(range(1, 11))
print('L:', L)


# 生成1-10的乘积列表
L = [x * x for x in range(1, 11)]
print('乘积列表:', L)

L = list(x * x for x in range(1, 11))
print('乘积列表:', L)

# 生成1-10的偶数乘积
L = list(x * x for x in range(1, 11) if x % 2 == 0)
print('偶数乘积列表:', L)

# 嵌套循环（一般不会大于两层）
L = list(m + n for m in 'ABC' for n in 'XYZ')
print('嵌套循环列表:', L)

# 多个变量的Dict
d = {'x': 'A', 'y': 'B', 'z': 'C'}
L = list(k + '=' + v for k, v in d.items())
print('循环字典列表:', L)

# 字符串转为小写
L = ['Hello', 'World', 'IBM', 'Apple']
S = list(s.lower() for s in L)
print('字符串列表: ', L, '转为小写: ', S)

## 练习 如果列表中含有非字符串，则转换为小写会出错
L = ['Hello', 'World', 18, 'Apple', None]
S = list(s.lower() for s in L if isinstance(s, str))
print('列表: ', L, '字符串转为小写: ', S)