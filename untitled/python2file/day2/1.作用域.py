# author:JinMing time:2020-05-11
# -*- coding: utf-8 -*-
g = "全局作用域"

def foo():
    print(g)

    def foo1():
        print(g)

        def foo2():
            print(g)


# L（Local）：局部作用域
def ha():
    c = 1

    def foo():
        a = "hello world"  # E（enclosing）嵌套作用域

        def bar():
            b = "hello python"  # L（Local）：局部作用域
            print(a)

            # print(b)


