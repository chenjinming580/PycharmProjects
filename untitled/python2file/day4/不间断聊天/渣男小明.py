# author:JinMing time:2020-05-16
# -*- coding: utf-8 -*-
import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 13000))
print("大白上线了...")

while True:
    # 向女神发送数据
    data = "小明：" + input(">>>")

    # 退出判断
    if "exit" in data:
        break

    sk.sendall(data.encode("utf8"))

    # 接受数据
    data = sk.recv(1024)
    print(data.decode("utf8"))