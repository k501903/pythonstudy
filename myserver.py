#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'WEB编程的练习'

__author__ = 'Jacklee'

"""
	负责启动WSGI服务器
	wsgiref是Python内置的一个WSGI服务器
"""

from wsgiref.simple_server import make_server

from hello import application1

# 创建一个服务器，IP地址为空，端口号为6789， 处理函数为application
httpd = make_server('', 6789, application1)
print('Serving HTTP on port 6789...')
# 监听HTTP请求
httpd.serve_forever()