#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'urllib内建模块的练习'

__author__ = 'Jacklee'


# urllib模块
# 提供操作URL的一系列功能
# request对象 发送请求
# urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
#            *, cafile=None, capath=None, cadefault=False, context=None)
# :url 可以是一个URL字符串也可以是一个request对象

## Get
# 使用Get请求一个页面
# 使用request对象


from urllib import request

with request.urlopen('https://www.baidu.com') as f:
	data = f.read()
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
	print('Data:', data.decode('utf-8'))

# 有些网站需要判断请求的头部信息，只有认定合格的header才会给出回馈
# 主要是避免爬虫/非法的访问
# 但是可以通过模拟header信息，绕过

req = request.Request('http://www.douban.com')
# 模拟iPhone6的请求
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
	print('Status', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
	print('Data:', f.read().decode('utf-8'))

## Post
# 使用Data参数把数据提交给服务器
