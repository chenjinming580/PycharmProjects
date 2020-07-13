# author:JinMing time:2020-06-02
# -*- coding: utf-8 -*-
from pylib.courselib import *


class TestAddCourse:
    def test_001(self):
        res = add_course('初中化学', '化学描述', '1')
        assert res['retcode'] == 0
        self.courseid = res['id']

    def teardown(self):
        delete_course(self.courseid)