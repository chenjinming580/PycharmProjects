# author:JinMing time:2020-05-11
# -*- coding: utf-8 -*-
def bar(func):
    def inner(something,a,b,c,d):
        print('中间')
        func(something,a,b,c,d)
        # 此处是装饰器为函数新增的功能
        print("学会了一些神奇的知识")

    return inner


@bar
def foo(something,a,b,c,d):
    print("正在某事:", something)


foo("看电视",'a','b','c','d')



