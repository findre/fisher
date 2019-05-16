"""
@Author   : Johnny Leaf
@Time     : 2019/5/16 15:09
@Software : PyCharm
@File     : book.py.py 
"""
from wtforms import Form
from wtforms import StringField
from wtforms import IntegerField

from wtforms.validators import DataRequired
from wtforms.validators import length
from wtforms.validators import NumberRange


class SearchForm(Form):

    q = StringField(validators=[length(min=1, max=30), DataRequired()])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)