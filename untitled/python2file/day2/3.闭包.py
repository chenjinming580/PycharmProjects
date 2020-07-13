# author:JinMing time:2020-05-11
# -*- coding: utf-8 -*-
# 在一个内部函数里边，对在外部作用域(不能是全局作用域)的变量进行调用
# 那么这个内部函数就被称之为闭包
def outer():
    x = 10

    def inner():
        print(x)

    return inner


outer()()  # inner()
# 可以拆为下面两行
a = outer()  # a = inner
a()  # inner()
