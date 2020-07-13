# CN_Mobile=['131','132','133','134'] #移动
# CN_Unicorn=['147','199','188'] #联通
# CN_telecon=['156','158','157'] #电信
#
# mobile=input('请输入11位的手机号码:')#输入11位手机号码
# mobile_s = mobile[:3] #截取前三位手机号码
# if mobile.isdigit():
#     if len(mobile)!=11:
#         print('号码位数不对')
#     else:
#         if mobile_s in CN_Mobile:
#             print('这是移动号码段')
#         elif mobile_s in CN_Unicorn:
#             print('这是联通号码段')
#         elif mobile_s in CN_telecon:
#             print('这是电信号码段')
#         else:
#             print('非电话号码段')
# else:
#         print('非法字符！')



telno=input("请输入手机号码:")
if not telno.isdigit():
    print("输入内容有非法字符")
elif len(telno) !=11:
    print("输入的手机号码位数不对！")
else:
    telno3=telno[:3]
    print("手机号前3位："+telno3)
    if telno3 in ('130','131','132','145','155','156','166','171','175','176','185','186','166'):
        print ("联通号段")
    elif telno3 in('134','135','136','137','138','139','147','150','151','152','157','158','159','172','178','182','183','184','187','188','198'):
        print("移动号段")
    elif telno3 in('133','149','153','173','177','180','181','189','199'):
        print("电信号段")
    else:
        print("未知号段！")
















