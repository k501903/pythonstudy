#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'分布式进程的练习'

__author__ = 'Jacklee'


# 将进程分布到不同的计算主体，通过网络进行通信
# Python提供了相应的模块managers

import sys, time, queue
from multiprocessing.managers import BaseManager

# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
	pass

# 由于这个Queuemanager只从网络上获取Queue， 所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 链接服务器
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)

# 注意端口和验证码保持与task_master设置的一致
manager = QueueManager(address=(server_addr, 5000), authkey=b'abc')

# 从网络链接
try:
	manager.connect()
except:
	print('queue is not exists.')

# 获取Queue的对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 从task_queue队列取出任务，把结果写入result队列中
for i in range(10):
	try:
		n = task.get(timeout=1)
		print('run task %d * %d...' % (n, n))
		r = '%d * %d = %d' % (n, n, n * n)
		time.sleep(1)
		result.put(r)
	except queue.Empty:
		print('task queue is empty.')
	except:
		print('queue is closed.')
print('worker exit.')