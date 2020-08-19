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

# import traceback
#
# try:
#     b=4/0
# except:
#     print('报错了\n'+traceback.format_exc())

#
# import sys
# print(sys.path)
str=[5,3,1,1,7,9]
print(str.pop(3))
str.remove(1)
print(str)
str=str+[39]
print(str)
str.extend([666])
print(str)


s=['i','like','football']

print(','.join(str))
s.extend([1,2,3])


print(str)

dict1 = {'name': 'Jack', 'age': 40}
# dict1['sex']='男'
# dict1['age']=30
# print(dict1)
#
# del dict1['name']
# print(dict1)
#
#
# print(dict1.items())

for one in dict1.values():
    print(one)
import traceback
try:
    4/0
except:
    print('报错了\n',traceback.format_exc())

import random
print(random.randint(0,9))


import time
print(int(time.time())//1000000)