# author:JinMing time:2020-05-16
# -*- coding: utf-8 -*-
import threading
import time

a = []


def foo():
    while True:
        a.append("1")
        print("生产了一个数据")
        time.sleep(1)


t = threading.Thread(target=foo)
# 设置守护线程，必须在 start 之前设置
# 其作用就是在主线程想要退出进程的时候，不需要等待自己运行结束，直接退出就行了
t.setDaemon(True)
t.start()

for i in range(20):
    if a:
        a.remove("1")
        print("消耗了一个数据")
    time.sleep(1)

print("不再需要消费数据了")