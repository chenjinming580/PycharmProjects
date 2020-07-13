# author:JinMing time:2020-04-23
import requests
from config import HOST
header={'Content-Type':'application/x-www-form-urlencoded'}
payload={'action':'delete_course','id':1519}
respon=requests.delete(f'{HOST}/api/mgr/sq_mgr/',headers=header,data=payload)
print(respon.text)