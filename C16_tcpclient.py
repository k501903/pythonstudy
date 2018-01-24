#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'TCP网络编程的练习'

__author__ = 'Jacklee'


# socket模块
# 网络编程的基础是Internet协议族
# 协议族中最长用的是HTTP协议
# HTTP协议的网络层是TCP协议
# TCP协议是一种面向连接的通讯协议
# 由一个Server端和多个Client端组成
# 客户端与服务端建立连接后，可以双向进行数据的传输

# 当socket服务端没有准备好时
# socket客户端多次调用connect
# 第一次提示error no 61
# 之后提示error no 22 Invalid argument
# 如果释放该客户端，再创建一个新的socket则没有问题
# 不知道是因为什么？

# TCP协议实现
import socket
import time

# socket对象
# socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
# : family 协议族，默认IPv4
# : type 类型，默认流

# 创建一个socket
while True:

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcpclient:
		print('创建了一个socket...')

# 客户端不需要绑定
# connect(address)
# :address 是一个地址对
		try:
			tcpclient.connect(('127.0.0.1', 6789))
			print('连接服务器的6789端口....')
# 从tcpclient读取数据
			data = tcpclient.recv(1024)
			print('从服务器接收到数据:', data.decode('utf-8'))
			for data in [b'Michael', b'Tracy', b'Sarah']:
				tcpclient.send(data)
				print(tcpclient.recv(1024).decode('utf-8'))
			tcpclient.send(b'exit')		
			break
		except Exception as e:
			time.sleep(0.5)
			print('没有连接成功:', e)

