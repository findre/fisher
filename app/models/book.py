"""
@Author   : Johnny Leaf
@Time     : 2019/5/16 17:48
@Software : PyCharm
@File     : book.py 
"""
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from flask_sqlalchemy import  SQLAlchemy
db = SQLAlchemy()


class Book(db.Model):

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass