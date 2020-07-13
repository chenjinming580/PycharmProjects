# author:JinMing time:2020-05-18
# -*- coding: utf-8 -*-
import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 13000))
sk.listen()

while True:
    # 等待传入连接
    conn, addr = sk.accept()
    # 接受数据
    data = conn.recv(1024)
    print(data.decode("utf8"))

    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<p>欢迎欢迎，热烈欢迎</p>
<select>
    <option>选项1</option>
    <option>选项2</option>
    <option>选项3</option>
</select>
</body>
</html>
"""

    conn.sendall(("HTTP/1/1 200 OK\r\n%s" % html).encode("utf8"))