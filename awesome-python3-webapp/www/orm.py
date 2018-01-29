#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
模块：orm
版本：V1.0
日期: 2018/1/25
模式：异步MySQL
架构：使用aiomysql库
功能：V1.0 简单的ORM模块. 支持对实体对象实例的操作实现对数据库的同步操作
       1. 定义实体类. 设置表名称和字段信息
       2. 通过实体对象实例的方法, 实现对数据库的增删改操作
       3. 通过实体对象实例的方法, 实现对数据库的查询操作
     使用示例:
       1. 定义实体类(Modal的子类)
        class User(Model):
            # 定义对应的表名称
            # 如果不设置表名属性__table__，则默认使用类名User作为表名
            __table__ = 'users'

            # 定义每个字段的信息
            # id - 字段名
            # IntegerField() 字段的属性对象
            id = IntegerField(name='id', primary_key=True)
            name = StringField(name='name', ddl='varchar(20)')
       2. 实例化实体对象
        # 创建实例
        user = User(id=123, name='Michael')
        # 存入数据库
        user.insert()
        # 查询所有User对象
        users = User.findAll()
"""

import logging
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
        #charset=kw.get('charset', 'utf-8'),
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
            records = await cursor.fetchmany(size)
        else:
            records = await cursor.fetachall()
        # 执行完查询语句后, 关闭游标
        await cursor.close()
        logging.info('查询结果: %s行', len(records))
        return records

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

def create_args_string(num):
    '''
    根据参数数量创建SQL语句中的参数占位符
    '''
    lst = []
    for n in range(num):
        lst.append('?')
    return ', '.join(lst)

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
    # 字符串类型需要设置长度，因此需要ddl参数
    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)

class IntegerField(Field):
    '''
    整数字段类
    '''
    # 类型是固定的
    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)

class BooleanField(Field):
    '''
    布尔字段类
    '''
    # 类型是固定的 不可能作为主键
    def __init__(self, name=None, default=False):
        super().__init__(name, 'bool', False, default)

class FloatField(Field):
    '''
    浮点字段类
    '''
    # 类型是固定的
    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)

class TextField(Field):
    '''
    长字符字段类
    '''
    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)

class ModelMetaClass(type):
    '''
    Modal类的元类
    负责将子类(实体类)的映射信息读取出来
    然后创建新的实体类
    替换所有Field类型的对象为字段实际类型
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
        attrs['__select__'] = 'select `%s`, %s from `%s`' % \
            (primarykey, ', '.join(escaped_fields), tablename)
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tablename, \
            ', '.join(escaped_fields), primarykey, create_args_string(len(escaped_fields) + 1))
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (tablename, \
            ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primarykey)
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

    def getValue(self, key):
        '''
        读取属性值
        :param key 属性名
        :return 属性值
        '''
        return getattr(self, key, None)

    def getValueOrDefault(self, key):
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
    async def findAll(cls, where=None, args=None, **kw):
        '''
        根据查询条件，返回查询结果\n
        :param where 查询条件, 条件的值使用?占位符 str\n
        :param args 查询条件的值，tuple\n
        :param **kw 其他条件(仅支持orderby limit)\n
        :result [user实例] user实例的列表，如果没有查询结果，则返回[]空列表
        '''
        # 1. 取出select语句。该语句并没有where条件
        sql = [cls.__select__]
        # 2. 添加where条件
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        # 3. 添加orderby limit条件
        orderby = kw.get('orderby', None)
        if orderby:
            sql.append('order by')
            sql.append(orderby)
        limit = kw.get('limit', None)
        if limit:
            sql.append('limit')
            if isinstance(limit, int):
                sql.append('?')
                args.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append('?, ?')
                args.extend(limit)
            else:
                raise ValueError('无效的limit值: %s' % str(limit))
        results = await select(' '.join(sql), args)
        return [cls(**re) for re in results]

    @classmethod
    async def findNumber(cls, selectField, where=None, args=None):
        '''
        根据查询条件，返回数量结果\n
        :param selectField 检索的数值型字段 str\n
        :param where 查询条件, 条件的值使用?占位符 str\n
        :param args 查询条件的值，tuple\n
        :result 查询结果 数值，如果没有查询到，则返回None
        '''
        # 1. 生成SQL主语句
        sql = ['select %s _num_ from %s' % (selectField, cls.__table__)]
        # 2. 添加where条件
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        results = await select(' '.join(sql), args, 1)
        return results[0]['_num_']

    @classmethod
    async def find(cls, pkey):
        '''
        通过主键找到类\n
        :param pkey 主键值\n
        :result user实例 或者 None
        '''
        results = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pkey], 1)
        if results is None:
            return None
        return cls(**results[0])

    async def save(self):
        '''
        将实体对象保存到数据库中
        '''
        args = list(map(self.getValueOrDefault, self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows = await execute(self.__insert__, args)
        if rows != 1:
            logging.warning('插入数据失败: 影响行数: %s', rows)

    async def update(self):
        '''
        将实体对象更新到数据库中
        '''
        args = list(map(self.getValue, self.__fields__))
        args.append(self.getValue(self.__primary_key__))
        rows = await execute(self.__update__, args)
        if rows != 1:
            logging.warning('更新数据失败: 影响行数: %s', rows)

    async def remove(self):
        '''
        将实体对象从数据库中删除
        '''
        args = list(map(self.getValue, self.__primary_key__))
        rows = await execute(self.__delete__, args)
        if rows != 1:
            logging.warning('删除数据失败: 影响行数: %s', rows)
