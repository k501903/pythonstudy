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

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
	return '''<form action="/signin" method="post">
				<p><input name="username"></p>
				<p><input name="password" type="password"></p>
				<p><button type="submit">Sign In</button></p>
				</form>'''

@app.route('/signin', methods=['POST'])
def signin():
	#需要从request对象读取表单内容
	if request.form['username'] == 'admin' and request.form['password'] == 'password':
		return '<h3>Hello, admin!</h3>'
	return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
	app.run()
