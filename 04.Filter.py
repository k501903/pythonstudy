# -*- coding: utf-8 -*-

# 高阶函数
# Filter

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Filter()函数
## 实现过滤掉偶数

def is_odd(n):
	return n % 2 == 1
print('过滤列表', L, '中的偶数: ', list(filter(is_odd, L)))


# 求素数(从2开始)
def primes():
	def _init():
		n = 1
		while True:
			n = n + 1
			yield n

	def _div(n):
		return lambda x: x % n > 0

	it = _init() #初始化序列
	while True:
		n = next(it)
		yield n
		it = filter(_div(n), it)

for n in primes():
	if n < 1000:
		print(n)
	else:
		break

# 筛选回数
def is_palindrome(n):
	return str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
