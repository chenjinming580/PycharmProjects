# author:JinMing time:2020-05-16
# -*- coding: utf-8 -*-
import requests
import threading

url1 = 'http://mirrors.163.com/centos/6/isos/x86_64/README.txt'
url2 = 'http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt'
newStr = ''
r = threading.Lock()


def read_txt(url):
    r.acquire()
    global newStr

    newStr += requests.get(url).text
    r.release()


t1 = threading.Thread(target=read_txt, args=(url1,))

t2 = threading.Thread(target=read_txt, args=(url2,))
t1.start()

t2.start()

t1.join()
t2.join()

with open('read89.txt', 'w', encoding='utf8') as f:
    f.write(newStr)

print('运行结束了')
