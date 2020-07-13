# author:JinMing time:2020-04-21
# import requests
# # # # payload={'action':'list_course',
# # # #          'pagenum':1,
# # # #          'pagesize':20
# # # #
# # # # }
# # # # r=requests.get('http://127.0.0.1:80/api/mgr/sq_mgr/',params=payload)
# # # # print(r.text)
# # # # r=r.json()
# # # # print(type(r))
# # # # assert r['retcode']==0

import traceback

try:
    b=4/0
except:
    print('报错了\n'+traceback.format_exc())









