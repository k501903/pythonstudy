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


import poplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr

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
		self.server.set_debuglevel(1)
		# welcome()返回邮件服务器的欢迎文字
		print(self.server.getwelcome().decode('utf-8'))

		# 进行身份认证
		self.server.user(self.email)
		self.server.pass_(password)

		# stat()返回邮件数量和占用空间
		print('Messages: %s. Size: %s' % self.server.stat())

		# list()返回所有邮件的编号
		resp, mails, octets = self.server.list()

		# 可以查看返回的列表类型
		print(mails)

		# 获取最新的一封邮件，注意索引从1开始
		index = len(mails)
		resp, lines, octets = server.retr(index)

		# lines存储了邮件的原始文本的每一行
		# 可以获得整个邮件的原始文本
		msg_content = b'\r\n'.join(lines).decode('utf-8')
		# 稍后解析出邮件
		self.msg = Parser().parsestr(msg_content)

		# 可以根据邮件索引号直接从服务器删除邮件
		# self.server.dele(index)

		# 关闭连接
		self.server.quit()


	def make_simple_mail(self):
		'''
			最简单的邮件，不带头信息
		'''
		self.msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')


	def make_text_mail(self):
		'''
			正常的文本邮件，带头信息
		'''
		self.msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
		# formataddr 对字符串进行编码
		# 不建议直接放入字符串，可能会出现中文字符的编码问题
		self.msg['From'] = formataddr((Header('Python爱好者', 'utf-8').encode(), self.from_addr))
		self.msg['To'] = formataddr((Header('我', 'utf-8').encode(), self.to_addr))
		# Header(s=None, charset=None, maxlinelen=None, header_name=None, continuation_ws=' ', errors='strict')
		# * s 初始化Header的值，可以不在创建时指定，而是在后面使用append()方法添加
		# * charset 初始化的字符集，可以不在创建时指定，而是在后面使用append()方法添加
		self.msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()


	def make_html_mail(self):
		'''
			HTML格式的邮件，带头信息
		'''
		# 创建邮件正文(html类型)
		self.msg = MIMEText('<html><body><h1>Hello</h1>' +
    		'<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    		'</body></html>', 'html', 'utf-8')
		self.msg['From'] = formataddr((Header('Python爱好者', 'utf-8').encode(), self.from_addr))
		self.msg['To'] = formataddr((Header('我', 'utf-8').encode(), self.to_addr))
		self.msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()


	def make_attd_mail(self):
		'''
			添加附件的邮件，带头信息
		'''
		# MIMEMultipart 对象
		# 可以包含若干内容的邮件
		self.msg = MIMEMultipart()
		# 添加头信息
		self.msg['From'] = formataddr((Header('Python爱好者', 'utf-8').encode(), self.from_addr))
		self.msg['To'] = formataddr((Header('我', 'utf-8').encode(), self.to_addr))
		self.msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()
		
		# 添加邮件正文(plain类型)
		self.msg.attach(MIMEText('Send with file...', 'plain', 'utf-8'))

		# 添加邮件附件
		with open('test.png', 'rb') as f:
			# 设置附件的MIME和文件名
			mime = MIMEBase('image', 'png', filename = 'test.png')
			mime.add_header('Content-Disposition', 'attachment', filename = 'test.png')
			mime.add_header('Content-ID', '<0>')
			mime.add_header('X-Attachment-Id', '0')
			mime.set_payload(f.read())
			encoders.encode_base64(mime)
			self.msg.attach(mime)


if __name__ == "__main__":
	msm = MySendMail()
	msm._get_mail_param()
	msm.make_simple_mail()
	mt = input('发送邮件(1-文本; 2-HTML; 3-附件):')
	if mt == '1':
		msm.make_text_mail()
	elif mt == '2':
		msm.make_html_mail()
	elif mt == '3':
		msm.make_attd_mail()
	msm._send_mail()
