#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Mysql数据库编程的练习'

__author__ = 'Jacklee'

"""
	需要安装sqlalchemy库
	1. pip3 install sqlalchemy
	主要的几个对象
	1. 对象基类
	用法: sqlalchemy.ext.declarative.declarative_base()
	含义: 定义ORM对象的基类. 通过调用该方法获得
	举例: Base = declarative_base()

	2. 定义实体类
	用法: class User(Base):
		  __tablename__ = 'tablename' 该变量定义表名

		  id = Column(String(20), primary_key=True) 定义字段类型
		  name = .....
		  .....

	3. sqlalchemy.engine.base.Engine对象
	用法: engine = create_engine('数据库连接字符串')
	格式: 数据库类型+数据库驱动名称://用户名:密码@机器地址:端口号/数据库名
	含义: 数据库连接

	4. sqlalchemy.orm.session.Session对象
	用法: DBSession = sessionmaker(bind=engine)
	      session = DBSession()
	含义: 数据库操作的类型. 注意是类型不是实体
	常用: session.add(实体对象) 插入表的对象
	      session.commit() 将对数据的操作提交到数据库保存
	      session.query(实体对象).filter(条件).one()/all() 检索
	      实体对象表示查询哪个表, filter表示where条件. one()返回一条. all()返回所有

"""
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义User对象
class User(Base):
	# 表的名字:
	__tablename__ = 'user'

	# 表的结构
	id = Column(String(20), primary_key=True)
	name = Column(String(20))

# 初始化数据库连接
# 使用连接字符串
# 格式如下：
# 数据库类型+数据库驱动名称://用户名:密码@机器地址:端口号/数据库名
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test')

# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 创建session对象
session = DBSession()

# 创建User对象
user1 = User(id='8', name='Bob')

# 添加到session
session.add(user1)

# 提交保存到数据库
session.commit()

# 关闭session
session.close()


## 查询
session = DBSession()

# 参数User表示检索user表
# filter()函数表示检索的条件，使用对象的属性判断
# one()表示返回一条记录
# all()表示返回所有记录
user = session.query(User).filter(User.id == '5').one()

# 打印输出
print('type:', type(user))
print('name:', user.name)

session.close()


