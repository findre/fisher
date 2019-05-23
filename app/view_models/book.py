"""
@Author   : Johnny Leaf
@Time     : 2019/5/22 10:55
@Software : PyCharm
@File     : book.py 
"""


class BookViewModel(object):

    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['title']
        self.author = book['title']
        self.image = book['title']
        self.price = book['price']
        self.summary = book['title']
        self.pages = book['title']


class BookCollection(object):

    def __init__(self):
        self.total = 0
        self.books = []
        self.keywrod = ""

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.books = [BookViewModel(book) for book in yushu_book.books]
        self.keywrod = keyword



class BookViewModel(object):
    """
    给search视图函数做数据处理。
    单项处理函数，多项处理函数服用单项思维。
    """

    @classmethod
    def pacage_single(cls, data, keyword):

        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword,
        }

        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]

        return returned

    @classmethod
    def pacage_collection(cls, data, keyword):

        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword,
        }

        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]

        return returned

    @classmethod
    def __cut_book_data(cls, data):

        book = {
            'title': data['title'],
            'author': '、'.join(data['author']),
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image'],
        }

        return book
