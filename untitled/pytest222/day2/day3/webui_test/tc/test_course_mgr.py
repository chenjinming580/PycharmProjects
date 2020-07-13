# author:JinMing time:2020-06-04
# -*- coding: utf-8 -*-
import pytest
from pylib.webUIlib import *
class TestCourseMgr():
    #需要在套件初始化清除时操作浏览器
    def setup_class(self):
        websetup('http://localhost/mgr/ps/mgr/index.html#/')

    def teardown_class(self):
        webteardown()

    @pytest.fixture(scope='function')
    def add_coures_setup(self,request):
        delete_all_courses()
        # yield
        # self.add_coures_teardown()
        request.addfinalizer(self.add_coures_teardown)

    def add_coures_teardown(self):
        delete_all_courses()

    # 测试添加课程
    @pytest.mark.add
    def test_add_cousre(self,add_coures_setup):
        add_course('初中化学', '化学描述', '1')
        check_course('初中化学',1)

    @pytest.fixture(scope='function')
    def setup_delete_course(self):
        delete_all_courses()
        add_course('初中化学', '化学描述', '1')


    # 测试删除课程
    @pytest.mark.delete
    def test_delete_course(self,setup_delete_course):
        delete_course('初中化学')
        check_course('初中化学')