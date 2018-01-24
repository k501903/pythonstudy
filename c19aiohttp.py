#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    TCP网络编程的练习
    asyncio模块实现了异步模型。实现了对TCP、UDP、SSL等协议
    aiohttp是基于asyncio实现的HTTP框架

'''
__author__ = 'Jacklee'


import asyncio
from aiohttp import web

async def index(request):
    '''
        处理请求'/'的函数
    '''
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html', charset='utf-8')

async def hello(request):
    '''
        处理请求'/hello'的函数
    '''
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html', charset='utf-8')

async def init(loop):
    '''
        服务器处理函数
    '''
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 6789)
    print('Server started at http://127.0.0.1:6789...')
    return srv

if __name__ == '__main__':
    LOOP = asyncio.get_event_loop()
    LOOP.run_until_complete(init(LOOP))
    LOOP.run_forever()
