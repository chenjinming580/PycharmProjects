import requests
from config import HOST


dict1={'Content-Type':'application/json'}


payload={
    "action": "add_course_json", 
    "data": {
        "name": "初中化22学1",
        "desc": "初中化学课程", 
        "display_idx": "4"
    }
}

#3.用requests发送post请求，data参数如果传入的是字符串，会按原格式发送
r=requests.post(f'{HOST}/apijson/mgr/sq_mgr/',headers=dict1,json=payload)

print(r.json())
