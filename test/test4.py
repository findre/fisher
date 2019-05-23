"""
@Author   : Johnny Leaf
@Time     : 2019/5/21 15:24
@Software : PyCharm
@File     : test4.py 
"""
import time

from werkzeug.local import LocalStack
from werkzeug.local import Local
import threading

my_stack = LocalStack()
my_stack.push(1)
print('in main thread after push , value is ' + str(my_stack.top))


def worker():
    print('in new thread before push, value is ' + str(my_stack.top))
    my_stack.push(2)
    print('in new thread after push, value is ' + str(my_stack.top))


new_t = threading.Thread(target=worker, name='johnny')
new_t.start()

time.sleep(1)

print('finally, in main thread value is '+ str(my_stack.top))
