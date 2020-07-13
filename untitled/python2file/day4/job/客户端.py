# author:JinMing time:2020-05-17
# -*- coding: utf-8 -*-
import socket

name = "Nathaniel"


def handleData(data):
    """
    将消息处理为特定格式
    :param data: 消息原文
    :return: 处理后的消息
    """
    # 先处理消息第二部分
    if data == "Nathaniel":
        dataType = "1"
    else:
        dataType = "2"

    # 处理消息的第一部分
    strLen = len(data)
    if strLen < 4:
        dataLen = "0" * (4 - strLen) + data
    else:
        dataLen = data

    return "|".join([dataLen, dataType, data])

sk = socket.socket()
sk.connect(("127.0.0.1", 13000))

# 先自报家门
sk.sendall(handleData(name).encode("utf8"))
sk.recv(1024)

while True:
    # 发消息
    inp = input(">>>")
    sk.sendall(handleData(inp).encode("utf8"))

    if inp == "exit":
        break

    # 收消息
    serverData = sk.recv(1024).decode("utf8")
    print(serverData)