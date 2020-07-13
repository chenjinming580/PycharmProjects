# author:JinMing time:2020-05-16
# -*- coding: utf-8 -*-
import threading
import time


def foo():
    time.sleep(10)
    print("阳光明媚")


t1 = threading.Thread(target=foo)
t1.start()
t1.join()  # 在线程 t1 结束运行之前，阻塞住主线程，不让继续往下运行

print("主线程最后一行代码")

print("最后的最后")