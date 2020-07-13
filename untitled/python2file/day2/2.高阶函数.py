# author:JinMing time:2020-05-11
# -*- coding: utf-8 -*-
def foo():
    print("我是一个函数")


"""
# # a = 1
# # b = a
# 
# # 函数名可以赋值给其他变量
# b = foo
# 
# # print(foo)
# # print(b)
# b()
"""

"""
def test(a):
    a()

# 函数名作为参数传递
test(foo)
"""


def bar():
    print("我是bar函数")

    def inner():
        print("我是inner函数")

    # 函数名作为返回值
    return inner


a = bar()
a()
print(a)



