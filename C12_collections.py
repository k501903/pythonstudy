#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'collections内建模块的练习'

__author__ = 'Jacklee'


# collections模块
# 集合类的使用
# namedtuple: 像对象一样访问tuple
# deque: 高性能的双向列表
# defaultdict: 当访问的key不存在时返回默认值
# ordereddict: 保持key的顺序
# Counter: 简单的计数器


# namedtuple
# 可以创建一个自定义的tuple对象
# 可以规定个数
# 可以使用属性而不是下标访问其元素

# 常规的tuple
# 鼠标指针的位置
print('======= 常规的tuple')
p = (1, 2)
print('P指针的长度:', len(p))
print('P[0]第一个:', p[0])
print('P[-1]最后一个:', p[-1])

# namedtuple
# namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)
# typename: 类型名称，如Point
# field_names: 字段名称，可以分开写['x', 'y']，也可以用符号分隔'x y' 或者'x,y'
# 返回一个类型type
# 注意: namedtuple类型的实例没有实例字典

from collections import namedtuple

print('======= namedtuple')
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('p的类型:', type(p))
print('p.x的值:', p.x)
print('p.y的值:', p.y)

# deque
# deque([iterable[, maxlen]])
# 可以从前后插入append() appendleft()
# 可以从前后去除pop() popleft()
from collections import deque
de = deque((1, 2, 3, 4))
print('deque双向队列:', de)
de.append(5)
de.appendleft(0)
print('deque双向队列:', de)
i = de.pop()
print('pop取出最后一个:', i)
i = de.popleft()
print('popleft取出第一个:', i)
print('deque双向队列:', de)

# defaultdict
# defaultdict([default_factory[, ...]])
# 1. 创建时，传入一个返回默认值的函数
# 2. 创建时，指定value的类型

# 先看一下如何指定一个默认值
from collections import defaultdict
# 传入一个返回默认值的函数, 返回值可以使用字符串和数字，其他没有进行验证
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print('存在的key1:', dd['key1'])
print('不存在的key2:', dd['key2'])

# 看看指定Value类型的例子
l = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# 创建时指定Value的类型为list
dd = defaultdict(list)
for k, v in l:
	# 因为Value类型为list，因此加入元素的方法使用append()
	dd[k].append(v)
print('list类型的defaultdict: ', dd)

# 如果创建时指定Value的类型是set
dd = defaultdict(set)
for k, v in l:
	# 因为Value类型为set，因此加入元素的方法使用add()
	dd[k].add(v)
print('set类型的defaultdict: ', dd)

# ordereddict
# OrderedDict([items])
from collections import OrderedDict

# 先创建一个dict
# 这里实际显示的与案例不符
d = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print('dict的存放顺序:', d)

# 再创建一个OrderedDict
od = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print('OrderdDict的存放顺序:', od)

# 再说说OrderdDict的一个用法
# move_to_end(key, last=True)
# 将一个存在的键值移动到最后，如果last=False则移动到最开始
od = OrderedDict.fromkeys('abcde')
od.move_to_end('b')
print('将b键值移动到最后:', od)
od.move_to_end('b', last = False)
print('将b键值移动到开头:', od)

# 内容排序sorted(items, key)
# key指定排序的规则
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

od = OrderedDict(sorted(d.items(), key=lambda x: x[0]))
print('按键排序:', od)
od = sorted(od.items(), key=lambda t: t[1])
print('按值排序', od)

# Counter计数器
# Counter([iterable-or-mapping])
# 是一种特殊的dict
# 其键值对中的Value是一个整数，记录着键值出现的次数
from collections import Counter
# 创建一个空白计数器
c = Counter()
# 添加成员
for ch in 'programming':
	c[ch] = c[ch] + 1
# 显示统计结果
print('计数器Counter:', c)
# 显示全部成员信息
print('计数器成员elements:', list(c.elements()))

# 取出成员统计值最多的
mc = c.most_common(3)
print('成员统计值最多的三个:', mc)
# 这个方法可以用来对一段文字/一篇文章中的文字/词汇进行统计

# 对计数器进行运算
# + - & | 运算符
# 进行运算后，只保留大于0的键值对
# 如果要保留0或负值，做减法时使用subtract()函数
c = Counter(a=4, b=3, c=2, d=-2)
d = Counter(a=1, b=4, c=2, d=4)
print('Counter(a=4, b=3, c=2, d=-2) + Counter(a=1, b=4, c=2, d=4):', c + d)
print('Counter(a=4, b=3, c=2, d=-2) - Counter(a=1, b=4, c=2, d=4):', c - d)
print('Counter(a=4, b=3, c=2, d=-2) & Counter(a=1, b=4, c=2, d=4):', c & d)
print('Counter(a=4, b=3, c=2, d=-2) | Counter(a=1, b=4, c=2, d=4):', c | d)
