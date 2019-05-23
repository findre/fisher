"""
@Author   : Johnny Leaf
@Time     : 2019/5/20 15:50
@Software : PyCharm
@File     : test3.py 
"""
import threading
import time
from werkzeug.local import Local


class A:
    b = 1


my_job = Local()
my_job.b = 1


def worker():
    my_job.b = 2
    print("in new thread b is " + str(my_job.b))


new_t = threading.Thread(target=worker, name='johnny leaf')
new_t.start()
time.sleep(1)
print("the mainthread b is " + str(my_job.b))
