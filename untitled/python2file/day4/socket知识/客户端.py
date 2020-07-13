# author:JinMing time:2020-05-16
# -*- coding: utf-8 -*-
import socket

# 创建 socket 对象
sk = socket.socket()
# 客户端不需要设置ip地址和端口号，ip地址就是设备的ip地址，端口号由系统分配一个空闲的端口号
# 发起连接
sk.connect(("127.0.0.1", 13000))

# 发送数据到服务端
sk.sendall(input(">>>").encode("utf8"))

# 接收数据，接受服务端发来的消息
server_data = sk.recv(1024)
print(server_data.decode("utf8"))