#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'datetime内建模块的练习'

__author__ = 'Jacklee'


# datetime模块
# 日期时间类型datetime 
# datetime类是在date和time类的基础上的增强类
# timestamp是一个与时区值无关的浮点数
# 日期时间类型与字符串的相互转换与格式化
# 时区转换

from datetime import datetime, timedelta, timezone

# 获取当前时间
# 返回的是datetime类型
now = datetime.now()
print(now)
print(type(now))

# datetime类型有很多只读属性
now.year
now.month
now.day
now.hour
now.minute
now.second
now.weekday

# 获取指定时间
dt = datetime(2018, 1, 3, 15, 24, 00)
print(dt)

# datetime类型在实例化时，可以指定日期和时间
# 但至少需要指定年、月、日

# 获取timestamp
# timestamp是一个浮点数，整数部分表示秒
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
# timestamp与时区无关，全球的计算机timestamp是一样的
t = datetime.now().timestamp()
print(t)

# 从timestamp转为datetime
print(datetime.fromtimestamp(t))

# 字符串转换为日期时间
# strptime
# 参数1: 日期字符串
# 参数2: 转换格式串(https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)
cday = datetime.strptime('2018-1-4 11:50:00', '%Y-%m-%d %H:%M:%S')
print(cday)

# 日期时间转换为字符串
# strftime
cstr = datetime.now().strftime('%Y-%m-%d %a %H:%M:%S')
print(cstr)

# datetime进行加减运算
# 使用 + - 运算符
# datetime +/- timedelta
# timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

sday = datetime(2018, 1, 4, 0, 0, 0)
dday = sday + timedelta(days=1)
print('timedelta:', dday)

# timezone时区
# datetime.tzinfo
tz = timezone(timedelta(hours=8))
now = datetime.now()
# 一般情况下datetime类型不含时区信息
# 2018-01-04 12:04:06.395779
print('本地当前时间:', now)

# 可以使用replace替换时区
bj = now.replace(tzinfo=tz)
print('UTC+8时间:', bj)
# 2018-01-04 12:04:06.395778+08:00
# 这就有了时区信息+08:00

# 如何切换时区呢
# 使用astimezone函数
# 参数为timezone对象
# 巴黎时区为UTC+1
bl = now.astimezone(timezone(timedelta(hours=1)))
print('巴黎时间:', bl)

# 虽然三个时间的显示不同，但是其timestamp是一样的
print('本地时间的timestamp:', now.timestamp())
print('北京时间的timestamp:', bj.timestamp())
print('巴黎时间的timestamp:', bl.timestamp())

## 练习
## 引入re就是建议使用正则表达式对字符串进行拆分
import re

def to_timestamp(dt_str, tz_str):
	#解析tz_str, 得到UTC值
	m = re.match(r'^UTC([\+|\-]\d+)\:(\d{2})', tz_str)
	if m:
		dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
		dt = dt.replace(tzinfo=timezone(timedelta(hours=int(m.group(1)))))
		return dt.timestamp()
	

# 测试
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
