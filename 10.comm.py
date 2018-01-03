#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'多进程的练习'

__author__ = 'Jacklee'


# 进程间通讯
# 使用Queue Pipes等方式交换数据

### 在Windows下的执行结果是如下内容，并没有读取的任何执行结果
# Process to write: 1572
# Put A to queue...
# Put B to queue...
# Put C to queue...
###
from multiprocessing import Process, Queue
import os, time, random

# 第一个进程执行的代码
def write(q):
	print('Process to write: %s' % os.getpid())
	for va in ['A', 'B', 'C']:
		print('Put %s to queue...' % va)
		q.put(va)
		time.sleep(random.random())


# 第二个进程执行的代码
def read(q):
	print('Process to read %s' % os.getpid())
	while True:
		val = q.get()
		print('Get %s from queue.' % val)


if __name__ == '__main__':
	# 父进程创建队列
	q1 = Queue()
	pw = Process(target=write, args=(q1,))
	pr = Process(target=read, args=(q1,))
	# 先启动写入进程
	pw.start()
	# 再启动读取进程
	pr.start()
	# 等待pw结束
	pw.join()
	# 强行终止pr
	pr.terminate()
