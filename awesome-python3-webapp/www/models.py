#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
模块：model
版本：V1.0
日期: 2018/1/29
功能：V1.0 定义三个使用的实体类
       User类
       Blog类
       Comment类
"""

import logging
import time
import uuid
from orm import Model, StringField, BooleanField, FloatField, TextField

__author__ = 'JackLee'

def next_id():
    """
    生成ID
    """
    re = '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)
    logging.info('生成的ID号: %s', re)
    return re

class User(Model):
    """
    用户实体类
    """
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    admin = BooleanField()
    created_at = FloatField(default=time.time)

class Blog(Model):
    """
    Blog实体类
    """
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    """
    留言实体类
    """
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)

def exportsql():
    """
    1. 从models模块中搜索实体类
    2. 根据实体类的定义生成创建表的SQL语句
    """
    module = __import__(__name__)
    attrs = dir(module)
    # print(attrs)
    with open('tableschema.sql', mode='w', encoding='utf-8') as f:
        for clsName in attrs:
            if clsName.startswith('_'):
                continue
            cls = getattr(module, clsName)
            if getattr(cls, '__table__', None):
                sql = []
                for k, v in cls.__mappings__.items():
                    sql.append('`%s` %s not null' % (k, v.column_type))
                if cls.__primary_key__:
                    sql.append('primary key (`%s`)' % cls.__primary_key__)
                out = 'create table %s (\n' % cls.__table__ + ',\n'.join(sql) + '\n) engine=innodb default charset=utf8;\n\n'
                f.write(out)

if __name__ == '__main__':
    exportsql()