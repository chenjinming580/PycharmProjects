# author:JinMing time:2020-04-28
import requests
import xlrd
import json
import time
from lib.excelManagerLib import redExcel,getNewExcel
from lib.loginlib import login
#这里是作业
#1-1 定义一个函数
def excutXLTestCase2():
    #1-2 用户登录
    sessionID =login('auto', 'sdfsdfsdf')
    cookie = {'sessionid': sessionID}
    #1-3 调用readExcel函数,读取Excel中的测试用例,得到一个列表
    path=r'F:\PycharmProjects\SongqinApi\data\教管系统-测试用例V1.2 .xls'
    savaPath=r'F:\PycharmProjects\SongqinApi\report\教管系统-测试结果V1.2.xls'
    list=redExcel(path,2)
    #1-4 复制得到一个新工作簿和工作表对象
    workBookNew=getNewExcel(path)
    workSheetNew=workBookNew.get_sheet(2)

    #2-1. 循环列表，判断第10列【是什么方法】
    for i in range(0,len(list)):
        time.sleep(0.001)  # 添加睡眠时间
        row=list[i]  #获取一行记录
        headers = json.loads(row[11])# 获取请求头-并转dict
        payload = json.loads(row[5]) #获取请求体内容-并转dict
        test = json.loads(row[6]) #获取断言结果-并转dict
        r=None #预先定义响应对象
        # 3. 请求url、请求头、data数据都从Excel中获取（课程新增除外）
        if row[10]=='get':
            r=requests.get(row[9],params=payload,headers=headers,cookies=cookie)
        elif row[10]=='delete':
            r = requests.delete(row[9], data=payload, headers=headers,cookies=cookie)
        elif row[10]=='post':
            randomStr = str(int(time.time() * 10000)) # 时间戳
            data=row[5].replace('{{courseName}}',randomStr) #课程名称-替换
            #添加部分参数
            payload={
                "action":"add_course",
                "data":data
            }
            print(payload)
            r = requests.post(row[9], data=payload, headers=headers,cookies=cookie)
        try:
            # 4. 结果写回Excel中
            dictBody=r.json()
            if dictBody['retcode']==test['code']:
                workSheetNew.write(i+1,7,'PASS') #写第7列，测试是否通过
            else:
                workSheetNew.write(i + 1, 7, 'FAIL')
                if 'reason' in dictBody.keys():
                    workSheetNew.write(i + 1, 8, dictBody['reason'])#写第8列，不通过原因
        except:
            workSheetNew.write(i + 1, 7, 'FAIL')
            workSheetNew.write(i + 1, 8, '异常')
    #5. 保存excel
    workBookNew.save(savaPath)
excutXLTestCase2()

