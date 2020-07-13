# author:JinMing time:2020-05-18
# -*- coding: utf-8 -*-
import paramiko

# 创建 ssh 对象
ssh = paramiko.SSHClient()

# 连接方式
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 远程主机 ip 地址，端口号，在远程主机已经存在的用户名和密码
ssh.connect("192.168.2.149", 22, "songqin", "songqin")

"""
# 执行命令，并获取命令执行结果
# stdin, stdout, stderr = ssh.exec_command("cd Desktop;ls")
# # print(stdout.read().decode("utf8"))
# stdin, stdout, stderr = ssh.exec_command("pwd")
# print(stdout.read().decode("utf8"))
"""

sftp = ssh.open_sftp()

# # 将本地文件传送到远程机器, 第一个参数是本地文件路径，第二个参数是远程文件路径
# sftp.put(r"D:\test\script\study\seleniumStu\day7\loginPage.py", "/home/songqin/Desktop/loginPage.py")

# 将远程机器文件下载到本地，第一个参数远程文件路径，第二个参数是本地路径
sftp.get("/home/songqin/Desktop/A", "D:\\test\script\study\pythonAdvanced\day5\A")

ssh.close()