# author:JinMing time:2020-06-02
# -*- coding: utf-8 -*-
from pylib.courselib import *
import pytest

coursemsg = None


def get_course():
    return coursemsg


@pytest.fixture(scope='package', autouse=True)
def setup_course():
    global coursemsg
    print('***开始执行课程环境初始化***')
    res1 = add_course('初中语文', '语文课', 1)
    res2 = add_course('初中数学', '数学课', 2)
    res = [{"id": res1['id'], "name": "course"},
           {"id": res2['id'], "name": "初中数学"}]
    coursemsg = json.dumps(res)
    yield setup_course
    teardown_course()


def teardown_course():
    print('***开始执行课程环境清除***')
    delete_all_courses()