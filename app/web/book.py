"""
@Author   : Johnny Leaf
@Time     : 2019/5/15 15:21
@Software : PyCharm
@File     : book.py 
"""
from flask import jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook
from fisher import app


@app.route("/book/search/<q>/<page>")
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)

    return jsonify(result)