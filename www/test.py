# -*- coding:utf-8 -*-
import asyncio

import sys

from www import orm
from www.model import User

__author__ = 'Won'
__date__ = '2017/12/26 16:51'


@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop=loop, user='root', password='3687014', db='awesome')
    u = User(name='Won', email='wenjunnan1994@gmail.com', passwd='1234567890', image='about:blank')
    yield from u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)
