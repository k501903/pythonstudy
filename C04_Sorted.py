# -*- coding: utf-8 -*-

# 高阶函数
# sorted

## 翻转字符串
s = '12345'
d = sorted(s, reverse=True)
print(''.join(d))

s = '12345'
d = s[::-1]
print(d)

## 列表元素排序
L = [36, 5, -12, 9, -21]
print('列表', L, '排序: ', sorted(L))
## 按元素的绝对值排序
print('列表', L, '绝对值排序: ', sorted(L, key=abs))

## 字符串排序
L = ['bob', 'about', 'Zoo', 'Credit']
print('列表', L, '排序: ', sorted(L))
## 取消大小写
print('列表', L, '取消大小写排序: ', sorted(L, key=str.lower))

### 练习
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
### 按名称排序
print(sorted(L, key=lambda x:x[0]))

def by_name(t):
	return t[0]
print(sorted(L, key=by_name))

### 按成绩排序
print(sorted(L, key=lambda x:x[1]))

def by_score(t):
	return t[1]
print(sorted(L, key=by_score))

