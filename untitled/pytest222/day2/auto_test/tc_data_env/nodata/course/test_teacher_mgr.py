# author:JinMing time:2020-06-02
# -*- coding: utf-8 -*-
from tc_data_env.nodata.course import *
from tc_data_env.nodata import *

teacherid = None


def setup():
    print('开始执行添加老师初始化')
    delete_all_teacher()


def teardown():
    print('开始执行添加老师清除')
    delete_teacher(teacherid)


def test_add_teacher():
    print('开始执行添加老师初用例')
    course = get_course()
    global teacherid
    res = add_teacher('kongzi', '123456', '孔子', '语文老师', course, 1)
    assert res['retcode'] == 0
    teacherid = res['id']