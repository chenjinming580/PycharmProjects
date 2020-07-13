# author:JinMing time:2020-05-16
# -*- coding: utf-8 -*-
import threading
import time


def foo(something, num):  # 定义每个线程要执行的函数
    for i in range(num):
        print("CPU 正在", something)
        time.sleep(1)


# 创建线程实例，target 指向任务函数，args 为 target 指向的函数传参
t1 = threading.Thread(target=foo, args=("看电影", 2))  # 生成了一个线程实例
t2 = threading.Thread(target=foo, args=("听音乐", 5))  # 生成了另一个线程实例

# 启动线程
t1.start()
t2.start()