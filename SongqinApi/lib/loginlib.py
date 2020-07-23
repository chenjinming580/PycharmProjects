# author:JinMing time:2020-04-23
import requests
from config import HOST
def login(username,password):
    try:
        header={'Content-Type':'application/x-www-form-urlencoded'}
        payload={'username':username,'password':password}
        respon=requests.post(f'{HOST}/api/mgr/loginReq',headers=header,data=payload)
        return respon.cookies['sessionid']
    except:
        return {'retcode': 888, 'reason': '项目异常'}


if __name__ == '__main__':
    r=login('auto','sdfsdfsdf')
    print(r)