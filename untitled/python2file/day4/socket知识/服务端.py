# author:JinMing time:2020-05-16
# -*- coding: utf-8 -*-
import socket

# 创建socket对象
sk = socket.socket()
# 绑定ip地址和端口号
sk.bind(("0.0.0.0", 13000))
# 监听，有没有请求过来
sk.listen()
print("服务端启动了")

# 等待传入连接，连接成功之前，会处于阻塞状态
# 连接成功之后，解除阻塞，返回一个新的socket对象和客户端的ip地址
conn, addr = sk.accept()
print("客户端的地址", addr)

# 接受数据(接受到的是客户端发来的消息)
# 在接受到数据之前，会处于阻塞状态
client_data = conn.recv(1024)
print(client_data.decode("utf8"))

send_data = input(">>>")
# 发送数据(发送一个键盘输入，发给客户端)
conn.sendall(send_data.encode("utf8"))