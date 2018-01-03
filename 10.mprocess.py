#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'多进程的练习'

__author__ = 'Jacklee'

#
# 实现多进程的几种方式
# 如何创建外部进程
# 如何在进程间通讯
#

# 1.使用fork()实现多进程
# 注意：仅限于Unix/Linux内核的系统
import os
# os.getpid()读取当前进程的PID
# print('Process (%s) start...' % os.getpid())
# 使用os.fork()复制当前进程, 该进程是当前进程的子进程
# 注意: fork()调用一次返回两次，第一次是父进程返回子进程的ID，第二次是子进程返回0
# pid = os.fork()
# if pid == 0:
# 	print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
# 	print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# 2. 使用multiprocessing模块
# 可以实现跨平台使用
from multiprocessing import Process
import os

# 定义子进程执行的代码
def run_proc(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))

# Process类创建进程
if __name__ != '__main__':
	print('Parent process %s.' % os.getpid())
	# 创建一个子进程
	# Process是一个类继承自BaseProcess
	# group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None
	p = Process(target=run_proc, args=('test',))
	print('Child process will start.')
	p.start()
	# join()方法等待子进程结束后再继续往下运行, 通常用于进程间的同步
	p.join()
	print('Child process End.')

# 进程池创建进程
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print('Run task %s (%s).' % (name, os.getpid()))
	start = time.time()
	# time.sleep()挂起一段时间
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ != '__main__':
	print('Parent process %s.' % os.getpid())
	# 创建多个子进程
	# Pool是一个方法
	# Pool(processes=None, initializer=None, initargs=(), maxtasksperchild=None)
	p = Pool(2)
	for i in range(1):
		p.apply_async(long_time_task, args=(i,))
	print('waiting for all subprocesses done...')
	# close()方法，不再允许添加新的进程了
	p.close()
	# join()方法等待子进程结束后再继续往下运行, 通常用于进程间的同步
	p.join()
	print('All subprocesses done.')


# 创建一个外部进程的子进程
# 使用subprocess模块

import subprocess

if __name__ != '__main__':
	print('$ nslookup www.python.org')
	r = subprocess.call(['nslookup', 'www.python.org'])
	print('Exit code:', r)


# 进程间通讯
# 使用Queue Pipes等方式交换数据

from multiprocessing import Process, Queue
import os, time, random

# 第一个进程执行的代码
def writeq(q):
	print('Process to write: %s' % os.getpid())
	for value in ['A', 'B', 'C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())

# 第二个进程执行的代码
def readq(q):
	print('Process to read %s' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.' % value)

if __name__ == '__main__':
	# 父进程创建队列
	q = Queue()
	pw = Process(target=writeq, args=(q,))
	#pr = Process(target=readq, args=(q,))
	# 先启动写入进程
	pw.start()
	# 再启动读取进程
	#pr.start()
	# 等待pw结束
	#pw.join()
	# 强行终止pr
	#pr.terminate()
