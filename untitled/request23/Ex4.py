# author:JinMing time:2020-04-21
import requests
# header={'Content-Type':'application/json'}
# payload='''{
#     "action":"add_course_json",
#     "data":{
#         "name":"初中化学",
#         "desc":"初中化学课程",
#         "display_idx":"4"
#     }
# }'''
#
# r=requests.post('http://127.0.0.1:80/api/mgr/sq_mgr/',headers=header,data=payload.encode(encoding='utf-8'))
# print(r.text)


header={'Content-Type':'application/json'}
payload={
    "action":"add_course_json",
    "data":{
        "name":"初中化学",
        "desc":"初中化学课程",
        "display_idx":"4"}}

r=requests.post('http://127.0.0.1/apijson/mgr/sq_mgr/',headers=header,json=payload)
print(r.text)