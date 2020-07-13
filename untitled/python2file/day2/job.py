# author:JinMing time:2020-05-11
# -*- coding: utf-8 -*-
import time

user_dict = {
    'user1': '123',
    'user2': '123'
}

token = ''



def get_token(func):
    def inner(*args):
        global token

        if token:
            func(*args)
        else:
            name = input('请输入用户名:')
            password = input('请输入密码：')
            if name in user_dict and user_dict[name] == password:
                token = int(time.time() * 1000000)
                func(*args)
                print(token)

            elif name in user_dict and user_dict[name] != password:
                print('输入的密码不对')

            else:
                print('输入的账户不存在')

    return inner


@get_token
def my_log():
    print('this is my_log')


@get_token
def my_name(name,age):
    print('欢迎登陆',name,age)


@get_token
def my_shopping_mall():
    print('商城购物')


while True:
    choss = input('1、查看日志\n2、我的信息\n3、我的商城\n请输入操作选项（请输入q退出）>>>')
    if choss == 'q':
        break
    elif choss == '1':
        my_log()
    elif choss == '2':
        my_name('张三',12)
    elif choss == '3':
        my_shopping_mall()
    else:
        print('输入不合法')

print(token)
