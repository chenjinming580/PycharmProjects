# author:JinMing time:2020-06-02
# -*- coding: utf-8 -*-
import requests
from cfg import *

url = f'http://{HOST}/api/mgr/sq_mgr/'


def add_teacher(username, password, realname, desc, course, idx):
    body = {
        'action': 'add_teacher',
        'data': f'''
            {{
                "username":"{username}",
                "password":"{password}",
                "realname":"{realname}",
                "desc":"{desc}",
                "courses":{course},
                "display_idx":{idx}
            }}

        '''
    }
    res = requests.post(url, data=body)
    print(res.json())
    return res.json()


def delete_teacher(id):
    body = {
        'action': 'delete_teacher',
        'id': id
    }

    resp = requests.delete(url, data=body)
    print(resp.json())
    return resp.json()


def list_teacher():
    listurl = f'{url}?action=list_teacher&pagenum=1&pagesize=20'

    resp = requests.get(listurl)
    print(resp.json())
    return resp.json()


def delete_all_teacher():
    res = list_teacher()
    retlist = res['retlist']
    for ret in retlist:
        resp = delete_teacher(ret['id'])
        print(f'删除老师:\n{resp}')