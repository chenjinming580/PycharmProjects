# author:JinMing time:2020-06-02
# -*- coding: utf-8 -*-
# 创建添加课程和删除课程请求
import json
from cfg import *
import requests

url = f'http://{HOST}/api/mgr/sq_mgr/'


def add_course(name, desc, idx):
    body = {
        'action': 'add_course',
        'data': f'''
           {{
              "name":"{name}",
              "desc":"{desc}",
              "display_idx":"{idx}"
            }}
        '''
    }
    resp = requests.post(url, data=body)
    print(resp.json())
    return resp.json()


def delete_course(id):
    body = {
        'action': 'delete_course',
        'id': int(id)
    }
    resp = requests.delete(url, data=body)
    print(resp.json())
    return resp.json()


def list_courses():
    params = {
        'action': 'list_course',
        'pagenum': '1',
        'pagesize': '20'
    }
    resp = requests.get(url, params=params)
    return resp.json()


# 定义一个删除所有课程的操作用来做初始化
def delete_all_courses():
    res = list_courses()
    retlist = res['retlist']
    for ret in retlist:
        delete_course(ret['id'])