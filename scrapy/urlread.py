#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'hashlib内建模块的练习'

__author__ = 'Jacklee'


# hashlib模块
import urllib.request
 
response = urllib.request.urlopen("http://www.baidu.com")
print(response.read())