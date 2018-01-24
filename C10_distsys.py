#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'分布式进程的练习'

__author__ = 'Jacklee'


# 将进程分布到不同的计算主体，通过网络进行通信
# Python提供了相应的模块managers

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()

# 接收任务的队列
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
	pass

# 把两个Queue都注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable = lambda: task_queue)
QueueManager.register('get_result_queue', callable = lambda: result_queue)

# 绑定端口5000，设置验证码abc
manager = QueueManager(address=('', 5000), authkey=b'abc')

# 启动Queue
manager.start()

# 获得通过网络访问的Queue对象
# 注册的名字，这里变成了方法接口
task = manager.get_task_queue()
result = manager.get_result_queue()

# 放几个任务进去
for i in range(10):
	n = random.randint(0, 10000)
	print('Put task %d...' % n)
	task.put(n)

# 从result队列读取结果
print('Try get results...')
for i in range(10):
	try:
		r = result.get(timeout=10)
		print('Result: %s' % r)
	except queue.Empty:
		print('result queue is empty.')

# 关闭
manager.shutdown()
print('master exit.')
