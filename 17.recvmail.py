#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'电子邮件编程的练习'

__author__ = 'Jacklee'

"""
	电子邮件的运作
	定义: 
		MUA (Mail User Agent) 客户端软件, 例如: Outlook
		MTA (Mail Transfer Agent) 服务器软件, 负责发送 例如: qq邮件服务器
		MDA (Mail Delivery Agent) 服务器软件, 负责接收 根据投递账户区分 
	流程:
	发件人 -> MUA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人 
	协议:
		发送邮件使用SMTP (Simple Mail Transfer Protocal)
		接收邮件使用POP3 (Post Offfice Protocol 版本3) / IMAP (Internet Message Access Protocol)

"""
# 模块
# poplib 负责接收邮件
# email 负责构造邮件
# 邮件分为: 纯文本邮件、HTML邮件、带附件的邮件三种
# 邮件接收分两个步骤
# 1. 从MDA接收邮件
# 2. 对邮件进行分析
#    1. 是multipart还是单个message
#    2. 对message的内容进行解析

## 一些常用对象和方法/属性的解释

# class POP3(host, port=POP3_PORT[, timeout])
# 创建一个Pop对象
# * host POP服务器的地址，字符串
# * port 默认是POP3_PORT

# class POP3_SSL(host, port=POP3_SSL_PORT, keyfile=None, certfile=None, timeout=None, context=None)
# 创建一个SSL连接的POP对象

# set_debuglevel()方法
# 设置DEBUG级别
# 0-不显示(默认)；1-显示；2-显示所有信息

# getwelcome()方法
# 获取POP服务器的欢迎字符串
# 例如：OK Hermes POP service () is ready.

# user(username)方法
# 发送user命令给服务器
# * username EMAIL地址串
# 正常返回b'+OK',这一步不进行user的验证工作

# pass_(password)方法
# 发送password给服务器，并对用户名和密码进行验证
# * password 密码串
# 返回b'+OK'
# 触发异常，如poplib.error_proto: b'-ERR User not exist' 

# stat()方法
# 获取邮箱Mailbox的状态
# 返回一个tuple类型 (message count, mailbox size).

# list([which])方法
# 请求邮件列表
# * which 邮件序号
# 不使用which. 返回值是一个tuple，格式为 (邮件数量, ['邮件序号 octets', ...], octets).
# 其中[]列表中存放的是字节bytes
# 使用which. 返回值是该message的['mesg_num octets', ...]

# retr(which)方法
# 根据which取得整个邮件
# * which参数. 邮件序号从1开始
# 返回值的格式 (response, ['line', ...], octets).
# 其中[]列表中存放的是邮件的内容的字节bytes

# class email.parser.Parser(_class=None, *, policy=policy.compat32)
# 该类型是专门处理将字符串解析为message类型的
# parsestr从字符串参数读取数据并解析
# parsestr(text, headersonly=False)
# parse从fp对象(file-like)中读取数据(text-mode)并解析
# parse(fp, headersonly=False)
# 以上两个均返回message对象

# class email.parser.BytesParser(_class=None, *, policy=policy.compat32)
# 该类型是专门处理字节解析为message类型的
# parsebytes从字节参数读取数据并解析
# parsebytes(bytes, headersonly=False)
# parse从fp对象(file-like)中读取数据(bianry-mode)并解析
# parse(fp, headersonly=False)
# 以上两个均返回message对象 <class 'email.message.Message'>


# email.header.decode_header(header)函数
import poplib, base64
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
from datetime import datetime

class MyRecvMail(object):
	def __init__(self):
		pass

	def _get_mail_param(self):
		'''
			通过输入获取接收邮件所需的参数
		'''
		# 邮箱地址
		self.email = 'lijie@boco.com.cn'
		# 邮箱密码
		self.password = input('Password:')
		# POP服务器地址
		self.pop_server = 'pop.boco.com.cn'


	def _recv_mail(self):
		'''
			从MDA将邮件接收下来
		'''
		self.server = poplib.POP3(self.pop_server)
		# 设置DEBUG级别
		self.server.set_debuglevel(1)
		# welcome()返回邮件服务器的欢迎文字
		print(self.server.getwelcome().decode('utf-8'))

		# 进行身份认证
		print('user:', self.server.user(self.email))
		print('pwd:', self.server.pass_(self.password))

		# stat()返回邮件数量和占用空间
		print('Messages: %s. Size: %s' % self.server.stat())

		# list()返回所有邮件的编号
		resp, mails, octets = self.server.list()

		# 可以查看返回的邮件列表
		print(mails)

		# 获取最新的一封邮件，注意索引从1开始
		index = len(mails)
		resp, lines, octets = self.server.retr(index)

		# lines存储了邮件的原始文本的每一行
		# 可以获得整个邮件的原始文本
		msg_content = b'\r\n'.join(lines).decode('utf-8')
		# 稍后解析出邮件
		self.msg = Parser().parsestr(msg_content)

		# 可以根据邮件索引号直接从服务器删除邮件
		# self.server.dele(index)

		# 关闭连接
		self.server.quit()
		self._print_info(self.msg)

	def decode_str(self, s):
		try:
			value, charset = decode_header(s)[0]
			if charset:
				value = value.decode(charset)
			return value
		except Exception:
			return '错误的解析'


	def guess_charset(self, msg):
		charset = msg.get_charset()
		if charset is None:
			content_type = msg.get('Content-Type', '').lower()
			pos = content_type.find('charset=')
			if pos >= 0:
				charset = content_type[pos + 8:].strip()
		return charset


	def _print_info(self, msg, indent=0):
		'''
			将邮件内容按缩进方式打印出来
		'''
		if indent == 0:
			# 如果是第一层级，则提取头部信息
			# 只提取From To Subject三项
			for header in ['From', 'To', 'Subject']:
				value = msg.get(header, '')
				if value:
					if header == 'Subject':
						value = self.decode_str(value)
					else:
						hdr, addr = parseaddr(value)
						if hdr != '':
							name = self.decode_str(hdr)
						else:
							name = ''
						value = '%s <%s>' % (name, addr)
				print('%s%s: %s' % ('  ' * indent, header, value))
		if (msg.is_multipart()):
			parts = msg.get_payload()
			for n, part in enumerate(parts):
				print('%spart %s' % ('  ' * indent, n))
				print('%s----------------------' % ('  ' * indent))
				printinfo(part, indent + 1)
		else:
			content_type = msg.get_content_type()
			if content_type == 'text/plain' or content_type == 'text/html':
				content = msg.get_payload(decode = True)
				charset = self.guess_charset(msg)
				if charset:
					content = content.decode(charset)
				print('%sText: %s' % ('  ' * indent, content + '...'))
			else:
				print('%sAttachment: %s' * ('  ' * indent, content_type))


	def parse_mail(self):
		'''
			解析邮件内容
			将结果打印出来
		'''
		_print_info(self.msg)


if __name__ == "__main__":
	print(dir(MyRecvMail))
	msm = MyRecvMail()
	msm._get_mail_param()
	msm._recv_mail()
