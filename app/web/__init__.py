"""
@Author   : Johnny Leaf
@Time     : 2019/5/16 11:41
@Software : PyCharm
@File     : __init__.py 
"""
from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book
from app.web import user
