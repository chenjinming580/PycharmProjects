# author:JinMing time:2020-06-02
# -*- coding: utf-8 -*-
import pytest


# before mark  fixture
# def simple_request():
#     import requests
#     res=requests.get('http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20')
#     return res.status_code
#
# def test_request():
#     status_code=simple_request()
#     assert status_code==200


# 方式1
# @pytest.fixture
# def simple_request(request):
#     print('开始初始化')
#     import requests
#     res=requests.get('http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20')
#     request.addfinalizer(after_test)
#     return res
#
# def after_test():
#     print('开始清除')
#
# def test_request(simple_request):
#     print('开始执行用例')
#     status_code=simple_request.status_code
#     assert status_code==200


# 方式2
# @pytest.fixture
# def simple_request():
#     print('开始初始化')
#     import requests
#     res=requests.get('http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20')
#     yield res
#     after_test()
#
# def after_test():
#     print('开始清除')
#
# def test_request(simple_request):
#     print('开始执行用例')
#     status_code=simple_request.status_code
#     assert status_code==200


# @pytest.fixture(scope='function',autouse=True)
# def simple_request():
#     print('开初始化')
#     yield
#     after_test()
#
# def after_test():
#     print('开始清除')
#
# def test_request():
#     print('开始执行测试')
#     assert 200==200

@pytest.fixture(scope='function')
def simple_request(request):
    print('开初始化')
    request.addfinalizer(after_test)


def after_test():
    print('开始清除')


def test_request(simple_request):
    print('开始执行测试')
    assert 200 == 200


@pytest.fixture(scope='function')
def simple_request2(request):
    print('开初始化2')
    request.addfinalizer(after_test2)


def after_test2():
    print('开始清除2')


def test_request2(simple_request2):
    print('开始执行测试2')
    assert 200 == 200