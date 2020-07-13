# author:JinMing time:2020-04-21
import requests
header={'Content-Type':'application/x-www-form-urlencoded'}
payload={
'action':'add_course',
'data':'''{
"name":"初中化学55",
"desc":"初中化学课程",
"display_idx":122}
}'''
}


r=requests.post('http://127.0.0.1:80/api/mgr/sq_mgr/',headers=header,data=payload)
print(r.text)


# dict1={'Content-Type':'application/x-www-form-urlencoded'}
# payload={
#     'action':'add_course',
#     'data':"""{"name":"初中2化学",
#     "desc":"初中化学课程",
#     "display_idx":"4"}"""
# }
#
# r=requests.post("http://localhost:80/api/mgr/sq_mgr/"
#                 ,headers=dict1,data=payload
#                 )
# print(r.text)


