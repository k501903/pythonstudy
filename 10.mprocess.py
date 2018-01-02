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
print('Process (%s) start...' % os.getpid())
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
if __name__ == '__main__':
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

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	# 创建一个子进程
	# Pool是一个方法
	# Pool(processes=None, initializer=None, initargs=(), maxtasksperchild=None)
	p = Pool(4)
	print(type(p))
	# for i in range(5):
	# 	p.apply_async(long_time_task, args=(i,))
	# print('Child process will start.')
	# p.start()
	# # join()方法等待子进程结束后再继续往下运行, 通常用于进程间的同步
	# p.join()
	# print('Child process End.')
