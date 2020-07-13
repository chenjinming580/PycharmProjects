# author:JinMing time:2020-05-11
# -*- coding: utf-8 -*-
def bar1(func):
    def inner1():
        func()
        print(1)

    return inner1


def bar2(func):
    def inner2():
        func()

        print(2)

    return inner2


def bar3(func):
    def inner3():
        func()
        print(3)

    return inner3


@bar3
@bar2  # inner2
@bar1  # inner1
def foo():
    print("我是foo")


foo()
