# -*- coding: utf-8 -*-

# 返回函数
# 

## 函数作为返回值
## 1. 变参的求和函数
def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax

print('(1, 3, 5, 7 ,9)求和: ', calc_sum(1, 3, 5, 7, 9))

### 2. 采用返回函数方式
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

### f变量保存了返回的函数以及args参数
f = lazy_sum(1, 3, 5, 7, 9)

### 调用f()时计算结果
print('(1, 3, 5, 7 ,9)求和: ', f()) 


### 练习
### 利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
	x = [0]
	def counter():
		x[0] = x[0] + 1
		return x[0]
	return counter

### 测试
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


## 闭包Closure

