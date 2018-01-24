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

# TCP协议实现
import socket
import threading, time

# socket对象
# socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
# : family 协议族，默认IPv4
# : type 类型，默认流

# 创建一个socket
tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('创建了一个socket...')

# 绑定IP地址和端口号
# 1. 有可能有多块网卡，需要指定
# 2. 需要指定端口号
# bind(address)
# :address 是一个地址对
tcpserver.bind(('127.0.0.1', 6789))
print('socket绑定到本机的6789端口....')

# 等待接收客户端的连接
# listen([backlog])
# :backlog 最大连接数
tcpserver.listen(5)
print('socket允许最大5个连接...')
print('等待客户端连接...')

def tcplink(sock, addr):
	print('接收了一个新的客户端连接. %s:%s...' % addr)
	sock.send('欢迎!'.encode('utf-8'))
	while True:

# 从socket读取数据
# 该函数属于阻塞函数
# 如果没有读取到数据，则一直等待不返回

		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('你好, %s!' % data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('来自%s:%s的连接关闭.' % addr)

# 循环等待客户端的连接
# 如果有连接则创建一个新的线程执行读写操作
# (conn, addr) = accept()
# :conn 返回一个socket对象，可以进行读写操作
# :addr 返回连接的地址对
# 是阻塞函数，当没有接收到新的连接时，一直等待不返回

while True:
	sock, addr = tcpserver.accept()
	trd = threading.Thread(target=tcplink, args=(sock, addr))
	trd.start()




