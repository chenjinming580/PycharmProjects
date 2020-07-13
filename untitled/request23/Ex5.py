# author:JinMing time:2020-04-21
import requests
# header={'Content-Type':'application/x-www-form-urlencoded'}
# payload={
#     'username':'auto',
#     'password':'sdfsdfsdf'
# }
#
# r=requests.post('http://127.0.0.1:80/api/mgr/sq_mgr/',headers=header,data=payload)
# print(r.text)


payload='username=auto&password=sdfsdfsdf'
header={'Content-Type':'application/x-www-form-urlencoded'}


r=requests.post('http://127.0.0.1:80/api/mgr/sq_mgr/',headers=header,data=payload)
print(r.text)