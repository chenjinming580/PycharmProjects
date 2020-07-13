# author:JinMing time:2020-04-23
#定义新增课程课程函数
from config import HOST
import requests
def add(name,desc,dispay_idx):
    try:
        header={'Content-Type':'application/x-www-form-urlencoded'}
        payload={
        'action':'add_course',
        'data':f'{{"name":"{name}","desc":"{desc}","display_idx":"{dispay_idx}"}}'}
        respon=requests.post(f'{HOST}/api/mgr/sq_mgr/',headers=header,data=payload)
        return respon.json()
    except:
        return {'retcode':888,'reason':'项目异常'}

#定义新增课程函数2
def add2(name,desc,display_idx):
    try:
        dict1 = {'Content-Type': 'application/json'}
        payload = {
            "action": "add_course_json",
            "data": {
                "name":name,
                "desc":desc,
                "display_idx":display_idx
            }
        }
        r = requests.post(f'{HOST}/apijson/mgr/sq_mgr/', headers=dict1, json=payload)
        return r.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}


#定义删除课程函数
def delete(id):

    header={'Content-Type':'application/x-www-form-urlencoded'}
    payload={'action':'delete_course','id':id}
    respon=requests.delete(f'{HOST}/api/mgr/sq_mgr/',headers=header,data=payload)
    try:
        return respon.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}



#定义查询课程函数
def list(pagenum,pagesize):
    try:
        payload={'action':'list_course','pagenum':pagenum,'pagesize':pagesize}
        r=requests.get(f'{HOST}/api/mgr/sq_mgr/',params=payload)
        r.encoding="utf-8"
        return r.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}


#定义修改课程函数
def modify(id,name,desc,display_idx):
    try:
        payload={
        'action':'modify_course',
        'id':id,
        'newdata':f'{{"name":"{name}","desc":"{desc}","display_idx":"{display_idx}"}}'
        }
        header={'Content-Type':'application/x-www-form-urlencoded'}
        respon=requests.put(f'{HOST}/api/mgr/sq_mgr/',data=payload,headers=header)
        return respon.json()
    except:
        return {'retcode': 888, 'reason': '项目异常'}


if __name__ == '__main__':
    one=list(1,10)
    print(one)

