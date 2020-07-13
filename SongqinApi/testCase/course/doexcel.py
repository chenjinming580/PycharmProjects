# author:JinMing time:2020-04-28
from lib.excelManagerLib import redExcel,getNewExcel
from lib.sendCoursceReq import sendCourseReq
import json
path=r'F:\PycharmProjects\SongqinApi\data\教管系统-测试用例V1.2 .xls'
newPath=r'F:\PycharmProjects\SongqinApi\report\教管系统-测试结果V1.2.xls'

newWorkBook=getNewExcel(path)
newworksheet=newWorkBook.get_sheet(0)



redList=redExcel(path,0)

for i in range(0,len(redList)):
    row=redList[i]
    ret1=sendCourseReq(row)

    colus7=json.loads(row[6])
    if ret1['retcode']==colus7['code']:
        print(row[0]+'测试通过')
        newworksheet.write(i+1,7,'测试通过')
    else:
        print(row[0]+'测试不通过')
        newworksheet.write(i+1,7,'测试不通过')
        if 'reason' in ret1.keys():
            newworksheet.write(i+1,8,ret1['reason'])

newWorkBook.save(newPath)