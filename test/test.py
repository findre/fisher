"""
@Author   : Johnny Leaf
@Time     : 2019/5/17 13:24
@Software : PyCharm
@File     : test.py 
"""
from flask import Flask
from flask import current_app
from flask import request

app = Flask(__name__)

# ctx = app.app_context()
# ctx.push()
# a = current_app
# print(current_app.config['DEBUG'])
# ctx.pop()

# with app.app_context():
#     a = current_app
#     print(current_app.config['DEBUG'])

class MyResource:

    def __enter__(self):
        print("connect to resource")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print('process exception')
        else:
            print("close resouce connection")
        return False

    def query(self):
        print("query data")

try:
    with MyResource() as resource:
        1/0
        resource.query()
except Exception as error:
    pass


