#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'单元测试的练习'

__author__ = 'Jacklee'

# 导入模块
#import logging

class Dict(dict):
    '''
        命名字典类型
        可以使用字典
    '''
    def __init__(self, **dw):
        super().__init__(**dw)

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError('Dict对象没有属性: %s' % attr)

    def __setattr__(self, attr, value):
        self[attr] = value


MYDICT = Dict(a=1, b=2)
print(MYDICT['a'])
print(MYDICT.a)
