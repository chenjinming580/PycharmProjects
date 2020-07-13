#time: 2020 - 06 - 02
# -*- coding: utf-8 -*-
from pylib.teacherlib import *
from pylib.courselib import *
import pytest


@pytest.fixture(scope='session', autouse=True)
def setup_nodata():
    print('***开始执行空环境初始化***')
    delete_all_teacher()
    delete_all_courses()



