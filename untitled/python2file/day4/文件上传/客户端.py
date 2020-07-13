# author:JinMing time:2020-05-16
# -*- coding: utf-8 -*-
import os
import socket


def post_file(sk_obj, file_path):
    """
    发送文件
    :param sk_obj: socket对象
    :param file_path: 文件路径
    :return: None
    """
    # 发送文件大小
    file_size = os.stat(file_path).st_size  # 获取文件大小
    file_size = str(file_size)  # 将 int 转为 str
    file_size = file_size.encode("utf8")  # 将 str 转为 bytes
    sk_obj.sendall(file_size)
    sk_obj.recv(1024)

    # 发送文件名称
    sk_obj.sendall(os.path.split(file_path)[1].encode("utf8"))
    sk_obj.recv(1024)

    # 发送文件内容
    file_size = os.stat(file_path).st_size  # 重新获取，得到 int 类型
    with open(file_path, "rb") as f:
        while file_size > 0:
            sk_obj.sendall(f.read(1024))
            file_size = file_size - 1024


# 创建 socket 对象
sk = socket.socket()
# 发起连接
sk.connect(("127.0.0.1", 13000))

post_file(sk, "D:\\test\script\study\pythonAdvanced\day4\\2文件上传\客户端\\a.png")

# 释放
sk.close()