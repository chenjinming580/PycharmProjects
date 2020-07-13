# author:JinMing time:2020-06-02
# -*- coding: utf-8 -*-
import json

import pytest
import requests

from readExcel import readExcel

'''
pytest使用回顾
requests发送接口案例介绍
pytest执行接口自动化案例
接口案例升级-参数化，excel读取数据
pytest参数化介绍
组合使用

'''


def add_course(payload):
    # payload
    res = requests.post('http://localhost/api/mgr/sq_mgr/',
                        {'action': 'add_course',
                         'data': payload})
    return res.json()


def check_addCourse(resp, expected):
    retcode = resp['retcode']
    actual = f'{{"code":{retcode}}}'
    assert actual == expected


# '初中语文', '初中语文描述', 1
def get_params():
    myData = readExcel('doc/教管系统-测试用例V1.2.xls', "课程管理")
    params = []
    for data in myData:
        if data['功能'] == '增加课程':
            params.append((data['请求参数'], data['断言']))

    return params


@pytest.mark.parametrize('payload,expected', get_params())
def test_addCourse(payload, expected):
    res = add_course(payload)
    try:
        check_addCourse(res, expected)
    except:
        print(res)
        raise AssertionError


if __name__ == '__main__':
    pass