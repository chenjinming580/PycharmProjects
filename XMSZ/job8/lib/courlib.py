# author:JinMing time:2020-07-08
# -*- coding: utf-8 -*-
import requests
from config import *
from robot.libraries.BuiltIn import BuiltIn


def add(name, desc, dispay_idx, idSavedName=None):
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {
        'action': 'add_course',
        'data': f'{{"name":"{name}","desc":"{desc}","display_idx":"{dispay_idx}"}}'}
    respon = requests.post(f'{host}/api/mgr/sq_mgr/', headers=header, data=payload)

    r = respon.json()
    if idSavedName:
        print('before')
        BuiltIn().set_global_variable(f'${idSavedName}', r['id'])
        print(f"global var set: ${idSavedName}:{r['id']}")

    return r


def delete(id):
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'action': 'delete_course', 'id': id}
    s= requests.delete(f'{host}/api/mgr/sq_mgr/', headers=header, data=payload)
    try:
        return s.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}


def list(pagenum, pagesize):
    try:
        payload = {'action': 'list_course', 'pagenum': pagenum, 'pagesize': pagesize}
        r = requests.get(f'{host}/api/mgr/sq_mgr/', params=payload)
        r.encoding = "utf-8"
        return r.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}


def deleteallcourse(pagenum, pagesize):
    r = list(1, 100)
    courselist = r['retlist']
    for one in courselist:
        delete(one['id'])
    r = list(pagenum, pagesize)
    if r['total'] == 0:
        return '删除成功'
    else:
        return '删除失败'

# if __name__ == '__main__':
#     one = list(1,100)
#     print(one)
