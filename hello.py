#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'WEB编程的练习'

__author__ = 'Jacklee'

"""
    application函数是一个符合WSGI标准的HTTP处理函数
    1. 主要是接收两个参数
    environ: 包含所有HTTP请求信息的dict对象
    start_response: 发送HTTP响应的函数
    2. 返回值
    返回值作为HTTP响应的Body发送给浏览器

    案例中的注意事项
    1. 响应头中加入字符编码utf-8，否则对于中文编码会出现乱码
    2. 对于中文PATH_INFO需要进行解码
    3. 中文-->UTF-8-->UTF-8字符串-->UTF-8字节数组-->中文
    4. 关键点是将编码后的字符串转为字节数组，在这里使用了map(ord, ...)，并通过bytes()将结果转变为字节数组
"""

def application(environ, start_response):
    '''
        服务端响应函数
    '''
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']



def application1(environ, start_response):
    '''
        服务端响应函数V2.0
        加入了对中文编码的支持
    '''
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    path = bytes(map(ord, environ['PATH_INFO'][1:])).decode('utf-8')
    body = '<h1>Hello, %s!</h1>' % (path or 'web')
    return [body.encode('utf-8')]
