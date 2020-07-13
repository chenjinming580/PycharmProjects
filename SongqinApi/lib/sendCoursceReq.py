# author:JinMing time:2020-04-27
from lib.courselib import add,list,delete
from lib.excelManagerLib import redExcel
import json
import time

def sendCourseReq(row):
    colue5=row[4]
    colue6=json.loads(row[5])
    ret=None
    if colue5=='add':
        courceName=colue6['name']
        courceName=courceName.replace('{{courseName}}',str(int(time.time() * 100)))
        ret=add(courceName,colue6['desc'],colue6['display_idx'])
    elif colue5=='list':
        ret=list(colue6['pagenum'],colue6['pagesize'])
    elif colue5=='delete':
        ret=delete(colue6['id'])
    return ret

# path=r'F:\PycharmProjects\SongqinApi\data\教管系统-测试用例V1.2.xls'
# excelCases=redExcel(path,0)
# sendCourseReq(excelCases[0])

