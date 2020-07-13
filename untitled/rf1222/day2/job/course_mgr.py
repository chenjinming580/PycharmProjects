# author:JinMing time:2020-05-21
# -*- coding: utf-8 -*-
import requests
def listCourse(pagenum,pagesize):
    try:
        payload={'action':'list_course','pagenum':pagenum,'pagesize':pagesize}
        r=requests.get('http://localhost/api/mgr/sq_mgr/',params=payload)
        r.encoding="utf-8"
        list=r.json()
        return [one['name'] for one in list['retlist']]
    except:
        return {'retcode': 888, 'reason': '项目异常'}


def returndict():
    return {
        'ele1' : 'male',
        'ele2' : 'female'
    }


if __name__ == '__main__':
    text=listCourse(1,11)
    print(text)

# import sys
# print(sys.path)
# sys.path.append('F:\webdriver\selenium')