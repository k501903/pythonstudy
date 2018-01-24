# -*- coding: utf-8 -*-

# 循环

# for循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
	print(name)

# 计算1+2+...+100
# 利用range()函数
sum = 0
for x in range(101):
	sum = sum + x
print(sum)

# while循环
n = 0 
while n < 10:
	n = n + 1
	print(n)

n = 0 
while n < 10:
	n = n + 1
	if n % 2 == 0:
		continue
	print(n)

