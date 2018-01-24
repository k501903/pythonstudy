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
# smtplib 负责发送邮件
# email 负责构造邮件
# 邮件分为: 纯文本邮件、HTML邮件、带附件的邮件三种

# 纯文本邮件
# MIMEText(_text, _subtype='plain', _charset=None, *, policy=compat32)
# * _text 邮件正文
# * _subtype 默认为plain，表示纯文本
# * _charset 字符集，使用utf-8兼容

# MIMEBase(_maintype, _subtype, *, policy=compat32, **_params)
# * _maintype 邮件类型(如: image)
# * _subtype 子类型(如: png)


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr

class MySendMail(object):
	def __init__(self):
		pass

	def _get_mail_param(self):
		'''
			通过输入获取发送邮件所需的参数
		'''
		# 邮箱地址
		self.from_addr = 'lijie@boco.com.cn'
		# 邮箱密码
		self.password = input('Password:')
		# 收件人地址
		self.to_addr = 'lijie@boco.com.cn'
		# SMTP服务器地址
		self.smtp_server = 'smtp.boco.com.cn'
		# SMTP服务器端口号
		self.smtp_port = eval(input('SMTP port:'))
		# 是否使用SSL加密传输
		self.usessl = input('Use SSL(Y/N):') == 'Y' 


	def _send_mail(self):
		'''
			将构建好的邮件msg发送出去
		'''
		# SMTP(host='', port=0, local_hostname=None, [timeout, ]source_address=None)
		# * host SMTP服务器地址
		# * port 端口号，默认25
		print(self.smtp_server, self.smtp_port)
		self.server = smtplib.SMTP(self.smtp_server, self.smtp_port)
		# 使用加密传输
		if self.usessl:
			self.server.starttls()
		self.server.set_debuglevel(1)
		# login(user, password, *, initial_response_ok=True)
		# * user email用户名,也就是自己的Email地址
		# * password 邮箱密码
		self.server.login(self.from_addr, self.password)
		# sendmail(from_addr, to_addrs, msg, mail_options=[], rcpt_options=[])
		# * from_addr 自己的Email地址
		# * to_addrs 是一个list，可以发送给多个人
		# * msg 发送的邮件正文
		self.server.sendmail(self.from_addr, [self.to_addr], self.msg.as_string())
		# quit()
		# 中断与服务器的连接
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
