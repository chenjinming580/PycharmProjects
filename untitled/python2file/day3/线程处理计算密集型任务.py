# author:JinMing time:2020-05-16
# -*- coding: utf-8 -*-
import threading
import time


def foo():
    num = 0
    for i in range(10000000):
        num += 1


begin_time = time.time()

# 并发
t1 = threading.Thread(target=foo)
t2 = threading.Thread(target=foo)
t1.start()
t2.start()
t1.join()
t2.join()

"""
# 串行 总消耗时长 1.808426856994629
foo()
foo()
"""

end_time = time.time()
print("总消耗时长", end_time - begin_time)