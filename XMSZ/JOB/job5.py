# author:JinMing time:2020-07-06
# -*- coding: utf-8 -*-
'''
5、这样的字符串
info = '姓名=小王&年龄=16&身高=175'
用一行代码，得到其中的年龄数字，不要数索引
'''
info = '姓名=小王&年龄=16&身高=175'


print(info.split('&')[1].split('=')[-1])