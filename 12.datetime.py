#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'datetime内建模块的练习'

__author__ = 'Jacklee'


# datetime模块

from datetime import datetime

# 获取当前时间
# 返回的是datetime类型
now = datetime.now()
print(now)
print(type(now))

# 获取指定时间
dt = datetime(2018, 1, 3, 15, 24, 00)
print(dt)

