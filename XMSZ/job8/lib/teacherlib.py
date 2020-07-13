# author:JinMing time:2020-07-07
# -*- coding: utf-8 -*-
import requests
from config import *
from robot.libraries.BuiltIn import BuiltIn

def addTeacher(username, password, realname, desc, courseid,display_idx,idSavedName=None):
    url = f'{host}/api/mgr/sq_mgr/'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {
        'action': 'add_teacher',
        'data': f'''{{"username":"{username}",
        "password":"{password}",
        "realname":"{realname}",
        "desc":"{desc}",
        "courses":[{{"id":{courseid},"name":"初中数学"}}],
        "display_idx":"{display_idx}"
        }}'''

    }


    response = requests.post(url=url, headers=headers, data=payload)
    r=response.json()

    if idSavedName:
        print('before')
        BuiltIn().set_global_variable(f'${idSavedName}',r['id'])
        print(f"global var set: ${idSavedName}:{r['id']}")

    return r




def listTeacher(pagenum,pagesize):
    url = f'{host}/api/mgr/sq_mgr/'
    headers={'Content-Type':'application/x-www-form-urlencoded'}
    payload = {
        'action':'list_teacher',
        'pagenum': pagenum,
        'pagesize': pagesize

    }
    try:
        r=requests.get(url=url,headers=headers,params=payload)
        return r.json()
    except:
        return {'retcode': 999, 'reason': '程序异常'}

def deleteTeacher(id):
    url = f'{host}/api/mgr/sq_mgr/'
    headers={'Content-Type':'application/x-www-form-urlencoded'}
    payload={
        'action':'delete_teacher',
        'id':id

    }
    try:
        r=requests.delete(url=url,headers=headers,data=payload)
        return r.json()
    except:
        return {'retcode': 999, 'reason': '程序异常'}

def deleteAllteacher(pagenum,pagesize):
    r=listTeacher(pagenum,pagesize)
    list=r['retlist']
    for one in list:
        delid=one['id']
        deleteTeacher(delid)
    r=listTeacher(pagenum, pagesize)
    if r['total']==0:
        return '删除成功'
    else:
        return '删除失败'



# if __name__ == '__main__':
#     one =addTeacher('dasdwerwesd',2121212,'asdsaddd','dasdas',1992,1)
#     print(one)




