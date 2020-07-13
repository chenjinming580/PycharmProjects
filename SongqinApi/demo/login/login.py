# author:JinMing time:2020-04-23
import requests
from config import HOST
header={'Content-Type':'application/x-www-form-urlencoded'}
payload={'username':'auto','password':'sdfsdfsdf'}
respon=requests.post(f'{HOST}/api/mgr/loginReq',headers=header,data=payload)
print(respon.text)