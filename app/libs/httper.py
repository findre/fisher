"""
@Author   : Johnny Leaf
@Time     : 2019/5/15 11:32
@Software : PyCharm
@File     : http.py.py 
"""
import requests


class HTTP:
    """
    获取请求API后的结果
    """
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)

        if r.status_code != 200:
            return {} if return_json else ''

        return r.json() if return_json else r.text