"""
@Author   : Johnny Leaf
@Time     : 2019/5/14 10:25
@Software : PyCharm
@File     : fisher.py 
"""
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

import app.web.book

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
