# -*- coding: utf-8 -*-

# 可以维护的有序集合
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print('集合classmates的元素个数为: %d' % len(classmates))

print('集合中的第一个元素: %s' % classmates[0])
print('集合中的最后一个元素: %s' % classmates[-1])

classmates.append('Adam')
classmates.insert(1, 'Jack')
print(classmates)

classmates.pop()
classmates.pop(1)
print(classmates)

classmates[1] = 'Sarah'
print(classmates)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)
print('显示asp: %s' % s[2][0])

s = []

# 不可维护的有序元组
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
# 空的元组
s = ()
# 一个元素的元组，必须带一个,
s = (1,)
print(s)

# 练习
L = [
	['Apple', 'Google', 'Microsoft'],
	['Java', 'Python', 'Ruby', 'PHP'],
	['Adam', 'Bart', 'Lisa']
]
# 打印出Apple
print(L[0][0])
# 打印出Python
print(L[1][1])
# 打印出Lisa
print(L[-1][-1])
