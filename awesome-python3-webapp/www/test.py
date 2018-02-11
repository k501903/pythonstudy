#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
模块：test
版本：V1.0
日期: 2018/1/29
功能：V1.0 测试User类
"""

import orm
import asyncio
from models import User
import models

async def test(lp):
    # 创建数据库异步缓冲池
    await orm.create_pool(lp, user='www-data', password='www-data', db='awesome')

    usr = User(name='Maggie', email='maggie@gmail.com', passwd='123456', image='about:blank')

    await usr.save()

if __name__ == '__main1__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    #loop.close()
