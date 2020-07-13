# author:JinMing time:2020-07-06
# -*- coding: utf-8 -*-
'''
6、如下变量对应了 学生的姓名、年龄和身高
name   = '小明'
age    = 16
height = 170
用一行代码，打印出如下格式的字符串
姓名=xx&年龄=xx&身高=xx

'''
name   = '小明'
age    = 16
height = 170

print(f'姓名={name}&年龄={age}&身高={height}')
info='姓名={}&年龄={}&身高={}'.format(name,age,height)
print(info)
