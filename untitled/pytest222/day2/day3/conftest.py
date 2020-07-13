# author:JinMing time:2020-06-04
# -*- coding: utf-8 -*-
def pytest_configure(config):
    config.addinivalue_line("markers", "add")
    config.addinivalue_line("markers", "delete")


