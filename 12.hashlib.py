#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'hashlib内建模块的练习'

__author__ = 'Jacklee'


# hashlib模块
# 提供摘要算法，如MD5、SHA1等等
# 摘要算法: 又称哈希算法、散列算法。通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）
# 重点: 将任意长度数据(data) 计算出固定长度摘要(digest)
# 用途: 
# 防止指定的数据被篡改
# 单向函数，难于逆推

# MD5算法
# 常用函数
# update()将进行摘要处理的数据传入，可以多次调用
# hexdigest()16进制显示的摘要结果
import hashlib

# 创建一个MD5实例
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
va = md5.hexdigest()
print('计算的MD5摘要为:', va)

# 创建一个SHA1实例
sha1 = hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
va = sha1.hexdigest()
print('计算的SHA1摘要是:', va)

## 用途
# 对用户名/密码进行加密存储
# 如果存储的是明文, 则容易泄露

# 练习 
