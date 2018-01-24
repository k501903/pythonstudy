#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'异步IO的练习'

__author__ = 'Jacklee'

"""
	本单元学习异步IO的第一个知识点"协程"
	1. 是一种子程序
	2. 一般的子程序是层级调用. 通过栈实现
	3. 协程不同点在于: 在子程序内部可以中断, 然后转而执行别的子程序, 在适当的时候再返回执行
	4. 有些类似与CPU的中断
	5. 有些类似于多线程模式. 但它比多线程的执行效率高, 原因有两个: 
	其一: 没有线程切换的开销, 在线程数量很多时效果更明显
	其二: 不需要多线程的锁机制
	6. 在多核CPU环境中, 建议使用多进程+协程的模式

	通过以上的叙述, 给我的第一感觉就是: 
	协程是通过generator实现的, yield语句实现调用的中断
	yield不但可以返回一个值，还可以接收调用者发出的参数
	
	******************
	划重点:
	生成器函数最大的特点是可以接受外部传入的一个变量，并根据变量内容计算结果后返回 
	这一切都是靠生成器内部的send()函数实现的. 生成器处理完成后调用close()函数关闭
		receive			= yield 	value
		传入参数						返回值
		调用send(param)函数传入		调用re = g.send()函数获得返回值re
		这句话包含了三个步骤:
		1. 向函数外抛出(返回)value
		2. 暂停, 等待next()或send()恢复
		3. 赋值receive = MockGetValue(). 这个MockGetValue()是假想函数，用来接收send()发送进来的值

		举例: 
		生成器函数
		def gen():
			value = 0
			while True:
				receive = yield value
				if receive == 'e':
					break
				value = 'got: %s' % receive

		获得生成器
		g = gen()
		# 发送send(None)启动
		print(g.send(None))
		# 消费生成器
		print(g.send('hello'))
		# 关闭生成器
		g.close()

		执行步骤:
		1. 通过g.send(None)或者next(g)启动生成器函数
		   执行到第一个yield语句结束的位置. 只执行了yield语句的前两个步骤, 并没有给receive赋值
		2. 通过g.send('hello')传入'hello', 从上次暂停的位置继续执行, 执行yield的第三步:将receive赋值为hello.
		   继续执行计算出value = 'got: hello'. 回到while True循环. 执行yield前两步, 将value值返回

"""
# 消费者
def consumer():
	a = ''
	while True:
		print('before yield')
		b = yield a
		print(b, a)
		# if not n:
		# 	return
		print('[CONSUMER] Consuming %s...' % b)
		a = '200 OK'

# 生产者
def produce(c):
	c.send(None)
	n = 0
	while n < 5:
		n = n + 1
		print('[PRODUCE] producing %s...' % n)
		r = c.send(n)
		print('[PRODUCE] Consumer return: %s' % r)
	c.close()

c = consumer()
produce(c)

"""
	以上代码的注释
	1. consumer()函数是一个生成器(generator)
	2. 把consumer传入produce
	3. 调用c.send(None)启动生成器
	4. 调用c.close()关闭生成器
"""