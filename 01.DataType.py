# -*- coding: utf-8 -*-

# 对基本数据类型和变量规则进行了说明

# 整数
a1 = 100 #整数
a2 = -100 #复数
a3 = 0xff00 #十六进制

# 浮点数
f1 = 1.23
f2 = -2.34
f3 = 1.23e9
f4 = 1.23e-5

# Python的整数和浮点数，没有大小限制

#字符串
s1 = 'abc' #使用''
s2 = "abc" #使用""
s3 = 'I\'m \"OK\"!' #使用\转义
s4 = r'\\\t\\' #使用r''取消转义
#使用'''...'''多行字符串
s5 = '''First Line 
Second Line
Three Line'''
#使用'''...'''多行字符串和r取消转义
s6 = r'''hello, \s 
world!'''

#布尔值 (注意大小写)
b1 = True
b2 = False

#空值 (注意大小写)
n1 = None

#无限大
n2 = inf

#变量 (Python 是动态语言，不需要声明变量类型，而是根据赋值来确定类型)
a = 'abc' #a是字符型
a = 100 #a变为整形

#常量 (Python 没有机制保障常量不被修改，而是使用大写的方式表示为常量)
PI = 3.1415926

#运算符
x = 10
x = x + 10
x = x - 10
x = x * 10
x = 10 / 3 #10除以3，计算结果是浮点数
x = 10 // 3 #10整除3，计算结果是整数
x = 10 % 3 #10整除3的余数，计算结果为整数

y = True
y = y and True
y = y or False
y = not y

