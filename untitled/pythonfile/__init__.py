# import time
# for i in range(10):
#     print("\r离程序退出还剩%s秒" % (9-i),end='')
#     time.sleep(1)
# print('hello\n' * 3)
#
# alist=[2,3,4,5,6,7,8]
# alist.append(5)
# print(alist[::2])
# del alist[1]


# str1='12121212r21'
# print(str1.replace('f','w',1))
# print(str1.split('e'))
# print(str1.strip())
# assert  str1.isdigit()
# aa=''
# aa.open('','')


# print('q')
# while True:
# #     var=input('请输入密码：')
# #     if var=='123456':
# #         print('输入正确')
# #         break
# #     else:
# #         print('请重新输入')
# alist=[3,5,4,6,9,7]
# new=alist.sort(reverse=True)
# print(new)
# alist = [9,2,6,0]
# print(alist.sort(reverse=True))

# import json
# # # # dict={'name':'jack','age':20,'sex':'男'}
# # # # for one,two in dict.items():
# # # #     print(one,two)
# # # #
# # # # dict=json.dumps(dict)
# # # # print(dict)
# def func(**args):
#     return args
#
# list=func(kk=1,oo=7)
# print(list.keys())
# print(*{'ee':9})
# import traceback
# try:
#     b = 4 / 0
# except Exception:
#     print('报错了\n'+traceback.format_exc())
#     raise ValueError('0不能做分母')



# alist = [9,2,6,0]
# alist.sort(reverse=True)
# print(alist)
# a=4
# print('%04d' %(a))
# print('{:0>4}'.format(a))

# a=[1,2,2,6,7]
# a[0]=6
# a[2]=1
# print(a)
# a.insert(3,4)
# print(a)
# print(set(a))


alist = [9,2,6,0]
alist.sort(reverse=True)
print(alist)
