# -*- coding: utf-8 -*-

# 生成器

# 定义样式一                         
L = (x * x for x in range(10))

# 定义样式二
def abc():
	print('返回1')
	yield 1
	print('返回2')
	yield 2
	print('返回3')
	yield 3
	return '结束了'

# 调用样式一，使用for迭代
# 显示为generator对象
print(L)
for n in L:
	print('L的元素: ', n)

# 调用样式二，使用next(g)函数
# 显示为generator对象
L = abc()
try:
	print('L的元素: ', next(L))
	print('L的元素: ', next(L))
	print('L的元素: ', next(L))
	print('L的元素: ', next(L))
except StopIteration as e:
# 一旦到达函数尾部，或者return返回结果，则抛出异常，在异常对象中能够取得return的返回结果
	print('生成器返回值: ', e.value)


# 斐波拉切数列
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return '完成'
# a, b = b, a + b
# 等同于 t = (b, a + b)		a = t[0]	b = t[1]
# 因此不会出现变量b的值被覆盖的情况，因为会有一个临时表量t作为中间值

# 判断哪个类型是迭代
from collections import Iterable
print('fib函数是迭代类型吗? ', isinstance(fib, Iterable))
print('fib(6)调用是迭代类型吗? ', isinstance(fib(6), Iterable))

# 判断哪个类型是生成器
import types
print('fib函数是生成器类型吗? ', isinstance(fib, types.GeneratorType))
print('fib(6)调用是生成器类型吗? ', isinstance(fib(6), types.GeneratorType))

### 练习(杨辉三角)
def triangles():
	re = []
	while True:
		if len(re) < 2:
			re.append(1)
		else:
			re = [x + re[i] for i, x in enumerate(re[1:])]
			re.insert(0, 1)
			re.append(1)
		yield list(re)
## 注意：函数中，每次都重新生成re，是为了解决程序上的一个BUG
## 情况是这样的，如果只定义一个中间对象re，第一次返回[1]没有问题
## 第二次返回[1, 1]也没有问题，可是当第二次返回[1, 1]时，results中的[1]却变成了[1, 1]
## 也就是说，第二次修改了re的值，这个值传导到了results中。也就是说results中保存的是re的地址
## 这个地址在第二次调用的时候内容被修改了，
## 对代码进行了修改，yield re 修改为 yield list(re)就可以了，返回一个新的对象

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
	print('测试通过!')
else:
	print('测试失败!')
	print(results)


## 网上大神的答案
def triangles(n):
	L = [1]
	while len(L) < n:
		yield list(L)
		L.append(0)
		L = [L[i - 1] + L[i] for i in range(len(L))]


n = 0
results = []
for t in triangles(100):
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
	print('测试通过!')
else:
	print('测试失败!')
	print(results)