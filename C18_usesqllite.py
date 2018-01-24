#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'数据库编程的练习'

__author__ = 'Jacklee'

"""
	使用内置的SQLLITE 
	主要的几个对象
	1. Connection(class sqlite3.Connection)
	用法: sqlite3.connect(database[, timeout, detect_types, isolation_level, check_same_thread, factory, cached_statements, uri])
		  database参数. 数据库文件名称('test.db')或者为内存数据库(':memory:') 
	含义: 数据库连接对象. 连接到指定的数据库.
	常用: close() 关闭连接 
		 commit() 对数据库的写操作的提交 
		 rollback() 对数据库写操作的回滚

	2. cursor (class sqlite3.cursor)
	用法: cursor = conn.cursor()
	含义: 数据库游标. 对数据库的操作是通过游标实现的
	常用: execute(sql[, parameters]). 执行SQL语句.
		  executemany(sql, seq_of_parameters). 执行SQL语句. 参数是一个序列化的多个参数. 可以理解为循环执行多次SQL
		  executescript(sql_script). 执行SQL脚本. 脚本间使用;分隔
		  fetchone() 从查询结果中取出一条记录
		  fetchmany(size=cursor.arraysize) 返回剩下的多行
		  fetchall()返回所有的记录
		  rowcount. 返回最后一次execute...操作的影响记录数
		  close(). 关闭游标
	参数化: SQL语句支持参数化. 一种是?，一种是命名:name

	3. Row对象
	用法: 使用cursor对象的fetch...返回的记录集
	      在创建Connection对象后, 调用: conn.row_factory = sqlite3.Row
	含义: 记录对象. 记录可以转换为tuple类型. 可以使用tuple对字段值进行访问(序号/列名)
	常用: keys()返回字段名的列表

"""

import sqlite3

with sqlite3.connect(':memory:') as conn:

	conn.row_factory = sqlite3.Row

	cursor = conn.cursor()

	cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')

	cursor.execute('insert into user(id, name) values(?,?)', ('1', 'micheal'))

	cursor.executemany('insert into user(id, name) values(?,?)', (('2', 'jackey'), ('3', 'mick')))

	conn.commit()

	cursor.execute('select * from user')

	rows = cursor.fetchall()

	print('一共有%s笔记录' % cursor.rowcount)
	for row in rows:
		print(row.keys())
		print('%s, %s' % (tuple(row)))

	cursor.close()

# conn.close()



## 练习
import os

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    re = []
    for row in cursor.execute('select * from user where score between ? and ? order by score', (low, high)):
    	re.append(row[1])
    cursor.close()
    conn.close()
    print(re)
    return re 

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
