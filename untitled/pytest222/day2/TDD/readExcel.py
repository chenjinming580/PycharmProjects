# author:JinMing time:2020-06-02
# -*- coding: utf-8 -*-
import xlrd

"""
实现功能：读取excel中的数据，返回一个字典列表
         其中每一行为一个字典，字典的Key为表头，值为字典的内容
传入参数1：fileName 文件名（带路径）
传入参数2：sheetName需要读取的工作表名称
"""


def readExcel(fileName, SheetName="Sheet1"):
    # 1-1 打开Excel，获取【workBook】 对象
    workBook = xlrd.open_workbook(fileName)

    # 1-2 从工作簿中，获取【workSheet】对象
    workSheet = workBook.sheet_by_name(SheetName)

    # 1-3 对【workSheet】工作表进行循环
    # 1-4 excel中的数据行数
    nrows = workSheet.nrows
    listData = []

    if nrows > 1:
        # 1.获取表头内容
        keys = workSheet.row_values(0)
        # 2.对表头下面的数据进行循环
        for i in range(1, nrows):
            row = workSheet.row_values(i)
            # 作用：通过zip和dict 组成字典
            rowDict = dict(zip(keys, row))
            # 3.把字典放入列表中
            listData.append(rowDict)
        return listData
    else:
        return listData


if __name__ == '__main__':
    myData = readExcel('../doc/教管系统-测试用例V1.2.xls', "课程管理")
    print(myData)