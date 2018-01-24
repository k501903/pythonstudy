# -*- coding: utf-8 -*-

# 字典dict

grades = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(grades['Tracy'])

# 添加
grades['Adam'] = 67
print(grades['Adam'])

# 修改
grades['Adam'] = 66
print(grades['Adam'])

# 删除
grades.pop('Adam')
print(grades)

# 判断是否存在
if 'Thomas' in grades:
	print(grades['Thomas'])
else:
	grades['Thomas'] = 90

print(grades.get('Thomas'))

# key值是不可变变量(list是可变对象，tuple是不可变对象)
# grades[[1, 2]] = 78
grades[(1, 2)] = 78
print(grades)

# 集合set
grades = set([1, 2, 3])
print(grades)

grades = set((4, 5, 6))
print(grades)

grades.add(10)
print(grades)

grades.remove(10)
print(grades)

grades.add(4)
print(grades)

a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
s = a & b
print(s)
p = a | b
print(p)