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
	案例中使用jinja2模板进行页面的渲染
	需要安装jinja2
	pip3 install jinja2
"""

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
	return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
	#需要从request对象读取表单内容
	username = request.form['username']
	if username == 'admin' and request.form['password'] == 'password':
		return render_template('signin-ok.html', username=username)
	return render_template('form.html', message='Bad username or password.', username=username)

if __name__ == '__main__':
	app.run()
