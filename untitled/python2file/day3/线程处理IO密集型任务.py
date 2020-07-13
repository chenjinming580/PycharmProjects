# author:JinMing time:2020-05-16
# -*- coding: utf-8 -*-
import threading
import time


def foo(something):
    print(something)
    time.sleep(1)


begin_time = time.time()

# 创建线程实例
t1 = threading.Thread(target=foo, args=("磁盘写入100M数据",))
t2 = threading.Thread(target=foo, args=("cpu去做其他事情",))

# 总消耗时长 1.0033142566680908
# 启动线程
t1.start()
t2.start()
# 在子线程完成运行之前，这个子线程的主线程将一直被阻塞
t1.join()
t2.join()

"""
# 串行的成绩 总消耗时长 2.0012686252593994
foo("磁盘写入100M数据")
foo("cpu去做其他事情")
"""

end_time = time.time()
print("总消耗时长", end_time - begin_time)