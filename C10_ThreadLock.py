#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'多线程的练习'

__author__ = 'Jacklee'


# threading模块
# 多个线程公用一个内存变量，存在访问冲突
# 因此需要一种锁机制，保证在一个线程执行中不会因为时间片的切换导致，其他线程访问到脏数据
# 使用Lock

# 先看看不加锁会出现什么问题
import time, threading

# 假定这是银行存款
balance = 0

def change_it(n):
	#先存后取，结果应该为0
	global balance
	balance = balance + n
	balance = balance - n

# 线程的执行体，运行300000次
def run_thread(n):
	for i in range(3000000):
		change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# 运行结果显示，balance的结果不为0
# 这是因为+n 和-n的操作，有可能不在一个执行时间片中
# 而两个线程公用一个变量，一个操作后另一个有可能就修改了其正常的值，导致出现偏差

# 使用加锁机制
# Lock
balance = 0
lock = threading.Lock()

def lock_thread(n):
	for i in range(3000000):
		lock.acquire()
		try:
			change_it(n)
		finally:
			lock.release()


t1 = threading.Thread(target=lock_thread, args=(5,))
t2 = threading.Thread(target=lock_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

