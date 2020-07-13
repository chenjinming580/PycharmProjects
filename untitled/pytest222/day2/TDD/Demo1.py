# author:JinMing time:2020-06-02
# -*- coding: utf-8 -*-
import pytest
import requests

from readExcel import readExcel


@pytest.mark.parametrize('a,b', [(1, 2), (3, 3), (1, 1)])
def test_case001(a, b):
    assert a == b


def get_data():
    myData = readExcel('doc/教管系统-测试用例V1.2.xls', "课程管理")
    params = []
    for data in myData:
        if data['功能'] == '增加课程':
            # 把请求参数和断言保存
            params.append((data['请求参数'], data['断言']))

    return params


@pytest.mark.parametrize('payload,expect', get_data())
def test_addCourse(payload, expect):
    res = requests.post('http://localhost/api/mgr/sq_mgr/',
                        {'action': 'add_course',
                         'data': payload
                         }
                        )
    print(res.json())
    actual_retcode = res.json()['retcode']
    actual = f'{{"code":{actual_retcode}}}'
    assert actual == expect


# @pytest.mark.parametrize('payload,expect',get_data())
# def test_addtest(payload,expect):
#     res = requests.post('http://localhost/api/mgr/sq_mgr/',
#                         {'action': 'add_course',
#                          'data': payload
#                          }
#                         )
#     print(res.json())
#     actual_retcode = res.json()['retcode']
#     actual = f'{{"code":{actual_retcode}}}'
#     assert actual == expect

if __name__ == '__main__':
    print(get_data())