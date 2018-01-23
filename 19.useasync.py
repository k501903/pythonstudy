#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'异步IO的练习'

__author__ = 'Jacklee'

"""
	本单元学习异步IO的第二个知识点async/await
	1. Python3.5版本引入的标准库
	2. 完美替代3.4版本中的asyncio/yield from

	1. event_loop 事件循环: 程序开启一个无限的循环，程序会把一些函数注册到事件循环上。
	   当满足事件发生的时候，调用相应的协程函数。
	   获得循环对象: loop = asyncio.get_event_loop()
	   注册协程: loop.run_until_complete(coroutine)
	2. coroutine 协程: 协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。
	   协程对象需要注册到事件循环，由事件循环调用。
	3. task 任务: 一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。
	   创建: task = loop.create_task(coroutine)
	4. future: 代表将来执行或没有执行的任务的结果。它和task上没有本质的区别
	5. async/await 关键字: python3.5 用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。
"""

import asyncio

async def hello():
	print('Hello world!')
	# 异步调用asyncio.sleep(1)
	await asyncio.sleep(1)
	print('Hello again!')

if __name__ == '__userasync__':
	# 获取EventLoop
	loop = asyncio.get_event_loop()

	# 执行coroutine
	loop.run_until_complete(hello())
	loop.close()


# 第二个例子
import random

async def smart_fib(n):
	index = 0
	a = 0
	b = 1
	while index < n:
		sleep_secs = random.uniform(0, 0.2)
		await asyncio.sleep(sleep_secs)
		print('Smart one think {} secs to get {}'.format(sleep_secs, b))
		a, b = b, a + b
		index += 1

async def stupid_fib(n):
	index = 0
	a = 0
	b = 1
	while index < n:
		sleep_secs = random.uniform(0, 0.4)
		await asyncio.sleep(sleep_secs)
		print('Stupid one think {} secs to get {}'.format(sleep_secs, b))
		a, b = b, a + b
		index += 1


if __name__ == '__main1__':
	loop = asyncio.get_event_loop()
	tasks = [smart_fib(10), stupid_fib(10)]
	loop.run_until_complete(asyncio.wait(tasks))
	print('All fib finished.')
	loop.close()

# 继续

import time

now = lambda: time.time()

async def do_some_work(x):
	print('Waiting: ', x)
	return 10

start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = loop.create_task(coroutine)
print(task)
# <Task pending coro=<do_some_work() running at 19.useasync.py:81>>
loop.run_until_complete(task)
print(task)
# <Task finished coro=<do_some_work() done, defined at 19.useasync.py:81> result=10>
print('TIME: ', now() - start)












