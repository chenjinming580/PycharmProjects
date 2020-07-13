# author:JinMing time:2020-04-23
import requests
from config import HOST
payload={
'action':'modify_course',
'id':1516,
'newdata':'{"name":"初中化学","desc":"初中化学课程","display_idx":4}'}
header={'Content-Type':'application/x-www-form-urlencoded'}

respon=requests.put(f'{HOST}/api/mgr/sq_mgr/',data=payload,headers=header)

print(respon.text)