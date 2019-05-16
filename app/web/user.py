"""
@Author   : Johnny Leaf
@Time     : 2019/5/16 11:58
@Software : PyCharm
@File     : user.py 
"""
from . import web


@web.route('/user/')
def login():
    return "johnny leaf"
