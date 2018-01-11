# -*- coding: utf-8 -*-

# 高阶函数
# Map/Reduce

# reduce()
# reduce(function, iterable[, initializer])
# 将迭代器依据function的规则进行求和运算

from functools import reduce
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Map()函数
## 实现f(x)=x<sup>2</sup>
def f(m):
	return m ** 2

R = map(f, L)
print('Map(f, L)的结果是Iterator: ', R)
print('Map(f, L)的列表是: ', list(R))

## 将数字转为字符串
print('将', L, '转为: ', list(map(str, L)))


# Reduce()函数

## 求和add(x, y)

def _add(x, y):
	return x + y

print('计算', L, '求和: ', reduce(_add, L))

## 将L列表转换为整数
def _fn(x, y):
	return x * 10 + y

print('将', L, '转换为: ', reduce(_fn, L))

# 利用map()和reduce()实现str2int
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

# 思路: 先将字符串转变为整数列表，再对整数列表进行求和运算
def str2int(s):
	def strtonum(ch):
		return DIGITS[ch]
	def _add(x, y):
		return x * 10 + y
	return reduce(_add, map(strtonum, s))

print('将8629转为整数: ', str2int('8629'))

# 可以使用lambda函数进一步优化
def str2int(s):
	def strtonum(ch):
		return DIGITS[ch]
	return reduce(lambda x, y: x * 10 + y, map(strtonum, s))
print('将3396815转为整数: ', str2int('3396815'))

#### 练习
# 将名字转换为标准写法: 首字母大写，其他字母小写
def normalize(name):
	return name[:1].upper() + name[1:].lower()

L = ['adam', 'LISA', 'barT']
print('将名称', L, '转换为标准样式: ', list(map(normalize, L)))	


# 计算list中元素的乘积

def prod(L):
	return reduce(lambda x, y: x * y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 将字符串转换为浮点数
def str2float(s):
	def nopoint(s):
		return [ch for ch in s if ch != '.']
	def pointpos(s):
		pos = s.find('.')
		return len(s) - pos - 1
	def strtonum(ch):
		return DIGITS[ch]
	return reduce(lambda x, y: x * 10 + y, map(strtonum, nopoint(s))) / (10 ** pointpos(s))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')