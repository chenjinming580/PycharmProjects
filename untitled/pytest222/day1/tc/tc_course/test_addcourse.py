# author:JinMing time:2020-06-01
# -*- coding: utf-8 -*-
from lib.courselib import *
class Test_addcourse():
    def setup(self):
        delete(1)

    def test_addcourse(self):
        add('之中','ceshi',1)



