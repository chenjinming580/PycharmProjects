# author:JinMing time:2020-04-27
import xlrd
from xlutils.copy import copy

def redExcel(path,sheet_num):
    workBook=xlrd.open_workbook(path)
    worksheet=workBook.sheet_by_index(sheet_num)
    retList=[]
    for i in range(1,worksheet.nrows):
        onerow=worksheet.row_values(i)
        retList.append(onerow)
    return retList



def getNewExcel(path):

    workbook=xlrd.open_workbook(path,formatting_info=True)
    newWorkBook=copy(workbook)
    return newWorkBook

