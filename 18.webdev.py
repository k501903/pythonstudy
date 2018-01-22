#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'WEB编程的练习'

__author__ = 'Jacklee'

"""
	WSGI(Web Server Gateway Interface)
	是一个接口规范
	包括了Server端、Middleware中间件、Applicatioin客户端

	1. 使用WSGI规范开发的简单的WEB处理程序
	hello.py
	myserver.py

	2. Web App
	就是一个WSGI的处理函数，针对每种HTTP请求进行响应
	A. 对不同HTTP请求(GET、PUT、POST、DELETE)进行处理
	B. 对不同的请求路径PATH_INFO进行处理
	而且随着页面数量和请求类型的增多，该函数难于维护

	3. 使用框架
	从大量的HTTP处理工作中解脱出来
	一般的框架都是使用注入模式JAVA/装饰器模式Python
	本案例中使用flask
	安装: pip3 install flask

	4. 使用模板
	简化生成HTML页面的处理
	使用带有变量和指令的HTML,后台根据这些变量和指令,将相关的数据和内容填充进去
	避免了大量的字符串的拼接工作，提高了工作效率，降低了出错的概率
	常用的模式MVC就是使用模板进行页面的渲染render
"""