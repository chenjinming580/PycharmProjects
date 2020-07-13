# author:JinMing time:2020-05-18
# -*- coding: utf-8 -*-
from python2file.日志.mylog import viewsLog
import pandas
import requests
import json

# 读
caseData = pandas.read_excel("case.xls", encoding='utf8')
caseNum = len(caseData)
print(caseData)

for i in range(caseNum):
    res = requests.request(caseData["请求方法"][i], caseData["接口地址"][i])

    # 接口断言
    try:
        # 断言内容为空, 默认通过
        if str(caseData["断言"][i]) == "nan":
            caseData.loc[i, "测试结果"] = "成功"
            continue
        # 先转成字典再判断
        assertDic = json.loads(caseData["断言"][i])
        response = json.loads(res.text)
        # 更新 excel 的断言结果
        if assertDic["code"] == response["code"]:
            caseData.loc[i, "测试结果"] = "成功"
        else:
            viewsLog.debug("接口断言失败")
            viewsLog.debug("我发过去的参数是：%s" % caseData["请求参数"][i])
            viewsLog.debug("接口返回参数是：%s" % res.text)
            caseData.loc[i, "测试结果"] = "失败"
    except Exception as e:
        viewsLog.error("字典转换失败, err =\n", e)
        assertRet = False

caseData.to_excel("case.xls", encoding='utf8', index=False)

