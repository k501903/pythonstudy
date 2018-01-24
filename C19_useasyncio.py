#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'异步IO的练习'

__author__ = 'Jacklee'

"""
	本单元学习异步IO的第二个知识点asyncio
	1. Python3.4版本引入的标准库
	2. 编程模型是一个消息循环.
	   从asyncio模块获取一个EventLoop引用. 把需要执行的协程放到EventLoop中执行

	3. yield from用法
	   yield 后跟直接输出的值
	   yield from 后跟Iterable对象, 返回其中的一个元素

	4. 在异步函数内, 需要使用yield from asyncio.sleep(n)中断当前的协程
	   asyncio.sleep()函数也是一个协程, 返回一个Iterable对象

	5. yield from 后面通常会跟一个耗时的操作
"""

import asyncio

@asyncio.coroutine
def hello():
	print('Hello world!')
	# 异步调用asyncio.sleep(1)
	r = yield from asyncio.sleep(1)
	print('Hello again!')

if __name__ == '__userasyncio__':
	# 获取EventLoop
	loop = asyncio.get_event_loop()

	# 执行coroutine
	loop.run_until_complete(hello())
	loop.close()


# 第二个例子
import random

@asyncio.coroutine
def smart_fib(n):
	index = 0
	a = 0
	b = 1
	while index < n:
		sleep_secs = random.uniform(0, 0.2)
		yield from asyncio.sleep(sleep_secs)
		print('Smart one think {} secs to get {}'.format(sleep_secs, b))
		a, b = b, a + b
		index += 1

@asyncio.coroutine
def stupid_fib(n):
	index = 0
	a = 0
	b = 1
	while index < n:
		sleep_secs = random.uniform(0, 0.4)
		yield from asyncio.sleep(sleep_secs)
		print('Stupid one think {} secs to get {}'.format(sleep_secs, b))
		a, b = b, a + b
		index += 1


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	tasks = [smart_fib(10), stupid_fib(10)]
	loop.run_until_complete(asyncio.wait(tasks))
	print('All fib finished.')
	loop.close()












