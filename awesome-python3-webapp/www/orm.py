#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
模块：orm
版本：V1.0
模式：异步MySQL
架构：使用aiomysql库
功能：V1.0 创建一个简单的异步数据库操作的封装. 实现连接池、对Select、Insert、Update、Delete操作进行了封装
        1. 首先创建一个Application对象. 使用web.Application()函数
        2. 向Application对象中添加路由信息. GET方法, PATH='\', 处理函数为index
        3. 运行Application. web.run_app()函数. 执行服务器的IP地址和端口号
        注: 并没有使用自建的消息循环队列(Loop). 队列由Application对象自建
"""

import logging
import asyncio
import aiomysql

__author__ = 'JackLee'

async def create_pool(loop, **kw):
    '''
    创建数据库连接池
    :param loop 循环队列
    :param **kw 数据库连接参数
    '''

    logging.info('创建数据库连接池...')
    # 定义全局变量__POOL为数据库连接池
    global __POOL
    # 对于数据库连接这种耗时的操作，采用异步方式，加入await
    # 在使用参数较多的函数时，可以采用多行的书写方式，更便于阅读
    __POOL = await aiomysql.create_pool(
        # 使用.get()方法, 如果Key值不存在时，可以有一个默认值，且不会报错
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf-8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

async def select(sql, args, size=None):
    '''
    对数据库进行Select操作
    :param sql 查询语句 str. 查询语句中的参数使用?占位符
    :param args 查询语句中的参数变量 tuple
    :param size 设置返回查询结果集的数量 int 默认为None表示返回全部结果集
    :return 查询结果 list(dict) 返回查询结果列表, 列表中存放记录的dict
    '''
    logging.info('查询语句: %s, 查询参数: %s', sql, args)
    with await __POOL as conn:
        # 创建一个返回DICT类型的游标
        cursor = await conn.cursor(aiomysql.DictCursor)
        # 将占位符由?替换为%s
        await cursor.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = await cursor.fetchmany(size)
        else:
            rs = await cursor.fetachall()
        # 执行完查询语句后, 关闭游标
        await cursor.close()
        logging.info('查询结果: %s行', len(rs))
        return rs

async def execute(sql, args):
    '''
    对数据库进行Insert、Update、Delete等操作
    :param sql 执行上述SQL语句 str, SQL语句中的参数使用?占位符
    :param args SQL语句中的参数变量 tuple
    :return 影响的记录数 int
    '''
    logging.info('SQL语句: %s, 查询参数: %s', sql, args)
    with await __POOL as conn:
        try:
            # 创建一个普通类型的游标
            cursor = await conn.cursor()
            # 将占位符由?替换为%s
            await cursor.execute(sql.replace('?', '%s'), args or ())
            num = cursor.rowcount
            #执行完SQL语句后, 关闭游标
            await cursor.close()
            logging.info('执行结果: %s', num)
        except Exception:
            raise
        return num

class Field(object):
    '''
    字段类
    所有字段类型的基类
    '''
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)

class StringField(Field):
    '''
    字符串字段类
    '''
    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)

class ModalMetaClass(type):
    '''
    Modal类的元类
    负责将子类(实体类)的映射信息读取出来
    '''
    def __new__(mcs, name, bases, attrs):
        # 排除Model类本身
        if name == 'Model':
            return type.__new__(mcs, name, bases, attrs)
        # 获取table名称
        tablename = attrs.get('__table__', None) or name
        # 记录日志
        logging.info('找到了Modal: %s (表名: %s)', name, tablename)
        # 获取所有的Field和主键名
        mappings = dict()
        fields = []
        primarykey = None
        for k, v in attrs.items():
            if isinstance(v, Field):
                logging.info('找到了映射: %s ==> %s', k, v)
                mappings[k] = v
                if v.primary_key:
                    # 找到主键
                    if primarykey:
                        raise RuntimeError('主键重复: %s' % k)
                    primarykey = k
                else:
                    fields.append(k)
        if not primarykey:
            raise RuntimeError('没有主键.')
        # 从属性中将字段名移除
        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = tablename
        attrs['__primary_key__'] = primarykey # 主键属性名
        attrs['__fields__'] = fields # 除主键外的属性名
        # 构造默认的SELECT, INSERT, UPDATE和DELETE语句:
        attrs['__select__'] = 'select `%s`, %s from `%s`' % (primarykey, ', '.join(escaped_fields), tablename)
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tablename, ', '.join(escaped_fields), primarykey, create_args_string(len(escaped_fields) + 1))
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (tablename, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primarykey)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tablename, primarykey)
        return type.__new__(mcs, name, bases, attrs)

class Model(dict, metaclass=ModelMetaClass):
    '''
    Modal类
    是所有ORM实体类的基类
    通过指定元类metaclass对目标类进行修改
    '''
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model'对象没有属性 '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def getvalue(self, key):
        '''
        读取属性值
        :param key 属性名
        :return 属性值
        '''
        return getattr(self, key, None)

    def getvalueordefault(self, key):
        '''
        读取属性值或者默认值
        :param key 属性名
        :return 属性值 或者 默认值
        '''
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                logging.debug('使用默认值 %s: %s', key, str(value))
                setattr(self, key, value)
        return value

    @classmethod
    async def find(cls, pk):
        '''
        通过主键找到类
        '''
        rs = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])

    async def save(self):
        '''
        将实体对象保存到数据库中
        '''
        args = list(map(self.getvalueordefault, self.__fields__))
        args.append(self.getvalueordefault(self.__primary_key__))
        rows = await execute(self.__insert__, args)
        if rows != 1:
            logging.warn('插入数据失败: 影响行数: %s', rows)
