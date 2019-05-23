"""
@Author   : Johnny Leaf
@Time     : 2019/5/20 12:59
@Software : PyCharm
@File     : test2.py 
"""
import threading
import time

request = None


def worker():

    print('i am thread')
    t = threading.current_thread()
    time.sleep(8)
    print(t.getName())


new_t = threading.Thread(target=worker, name="A thread")
new_t.start()
new_t = threading.Thread(target=worker, name="B thread")
new_t.start()
new_t = threading.Thread(target=worker, name="C thread")
new_t.start()

t = threading.current_thread()
print(t.getName())


