#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
模块：Web App
版本：V1.0
模式：异步HTTP
架构：使用aiohttp库中的web模块
功能：V1.0 创建一个简单的Web应用, 访问127.0.0.1:6789，返回一个Hello World!的页面
        1. 首先创建一个Application对象. 使用web.Application()函数
        2. 向Application对象中添加路由信息. GET方法, PATH='\', 处理函数为index
        3. 运行Application.web.run_app()函数. 执行服务器的IP地址和端口号
        注: 并没有使用自建的消息循环队列(Loop). 队列由Application对象自建
"""

import logging
from aiohttp import web

__author__ = 'Jacklee'

async def index(request):
    '''
    响应'/'的请求
    '''
    logging.info(request)
    return web.Response(body=b'<h1>Hello world!</h1>', content_type='text/html', charset='utf-8')

APP = web.Application()
APP.router.add_get('/', index)

web.run_app(APP, host='127.0.0.1', port=6789)
