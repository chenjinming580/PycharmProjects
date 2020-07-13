# author:JinMing time:2020-05-11
# -*- coding: utf-8 -*-
# import os
#
# # 相当于打开操作系统的shell， 敲入一串命令
# # 阻塞式调用：调用的外部程序每没有退出时，python程序会一直停在这里
# # 直到调用的外部程序退出，代码才接着往下执行
# ret = os.system("or %i in (1,2,10) do @echo %i")
#
# print("ret =", ret)

from subprocess import Popen, PIPE

# # 执行一个指定的命令，并将结果以字节字符串的形式返回
# # 阻塞式调用
# out = subprocess.check_output("mspaint")
# print("执行结果", out.decode("gbk"))

# # 输出重定向
# child = Popen(
#     "ipconfig",
#     stdout=PIPE,
# )
#
# output, err = child.communicate()
# print(output)

# 输入重定向
child = Popen(
    "python ioTest.py",
    stdout=PIPE,
    stdin=PIPE,
    # encoding="gbk"
)

output, err = child.communicate("的\n好".encode("gbk"))
print(output)