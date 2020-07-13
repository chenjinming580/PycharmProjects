# author:JinMing time:2020-05-16
# -*- coding: utf-8 -*-
import os
import socket


def get_file(sk_obj):
    """
    接受文件
    :param sk_obj: socket 对象
    :return: None
    """
    # 接受文件大小
    file_size = int(sk_obj.recv(1024).decode("utf8"))
    sk_obj.sendall(b"ok")

    # 接受文件名称
    file_name = sk_obj.recv(1024).decode("utf8")
    sk_obj.sendall(b"ok")

    # 接受文件内容
    with open("./a.png", "wb") as f:
        while file_size > 0:
            f.write(sk_obj.recv(1024))
            file_size = file_size - 1024


# 创建socket对象
sk = socket.socket()
# 绑定ip地址和端口号
sk.bind(("127.0.0.1", 13000))
# 监听
sk.listen()

# 等待传入连接
conn, addr = sk.accept()

get_file(conn)

# 释放
conn.close()
sk.close()