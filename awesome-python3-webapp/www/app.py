#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'WEB编程的练习'

__author__ = 'Jacklee'

"""
    使用flask框架

    处理3个URL
    1. GET / 首页 返回HOME
    2. GET /signin 登录页，显示登录表单
    3. POST /signin 处理登录表单，显示登录结果

    对于不同的路由flask使用装饰器进行关联
"""

from aiohttp import web

async def hello(request):
    return web.Response(body=b'<h1>Hello world!</h1>', content_type='text/html', charset='utf-8')

app = web.Application()
app.router.add_get('/', hello)

web.run_app(app)

