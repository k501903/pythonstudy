# -*- coding: utf-8 -*-

# 字符串的编码问题

#字符串类型
s = 'Python-中文'
print(s)
print(type(s))

#字节数组类型
b = s.encode('utf-8')
print(b)
print(type(b))

print(b.decode('utf-8'))


#格式化
s1 = 72
s2 = 85

r = (s2 - s1) / 72
print('小明的成绩提升了: %.1f%%' % r)
print('小明的成绩提升了: {0:.1f}%'.format(r))
