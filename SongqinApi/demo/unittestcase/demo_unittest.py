# author:JinMing time:2020-04-28
import unittest
from lib.excelManagerLib import redExcel,getNewExcel
from lib.sendCoursceReq import sendCourseReq
import json
import time
from lib.courselib import add,list,delete
from ddt import ddt,data
import MySQLdb


path = r'F:\PycharmProjects\SongqinApi\data\教管系统-测试用例V1.2 .xls'
# 1-1 从Excel中读取工作表中的测试用例
retList = redExcel(path, 0)
reasonList=[]
@ddt
class  DemoUnittest(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        path = r'F:\PycharmProjects\SongqinApi\data\教管系统-测试用例V1.2 .xls'
        newPath = r'F:\PycharmProjects\SongqinApi\report\教管系统-测试结果V1.2.xls'
        newWorkBook = getNewExcel(path)
        newworksheet = newWorkBook.get_sheet(0)
        for i in range(0, len(reasonList)):
            if reasonList[i] == '测试通过':
                newworksheet.write(i + 1, 7, reasonList[i])
            else:
                newworksheet.write(i + 1, 7, '测试不通过')
                newworksheet.write(i + 1, 8, reasonList[i])

        newWorkBook.save(newPath)

    @classmethod
    def setUpClass(cls):
        cls.clearData()


    @classmethod
    def clearData(cls):
        # 1-1 调用列出课程接口
        retList = list(1, 400)
        num = 0
        # 1-2 循环删除课程
        for data in retList['retlist']:
            delete(data['id'])
            num = num + 1
        print('本次共删除了:', num, '条数据')

    @classmethod
    def clearDb(cls):
        # 1-1 获取数据库连接的对象(注意修改IP、数据库密码)
        mydb = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', db='plesson')
        # 1-2 获取操作游标
        cursor = mydb.cursor()
        # 1-3 执行sql语句
        cursor.execute('delete from sq_course ')
        # 1-4 提交
        mydb.commit()
        # 1-5获取所有记录列表
        #cursor.fetchall()
        # 1-6 关闭游标和数据库连接
        cursor.close()
        mydb.close()



    @data(*retList)
    def test001(self,row):
        time.sleep(0.0001)
        ret = sendCourseReq(row)
        # print(ret)
        colus7 = json.loads(row[6])  # 第7列的值
        # print(colus7)
        # 1-3 断言
        v_reason =''
        if ret['retcode']==colus7['code']:
            reasonList.append('测试通过')
        else:
            if 'reason' in ret.keys():
                v_reason = ret['reason']
            else:
                reasonList.append('原因不存在')


        if 'reason' in ret.keys():
            v_reason=ret['reason']
        self.assertEqual(ret['retcode'],colus7['code'],v_reason)
        print('测试通过')






    def test003(self):
        courseName = "大学英语" + str(int(time.time() * 10000))
        # 1-1 先列出课程
        retList0 = list(1, 400)
        # 1-2 再新增课程
        ret = add(courseName, '课程描述', '0')
        print(ret)
        #1-3 断言1
        self.assertEqual(ret['retcode'] ,0,'新增课程失败1')
        print(">>>>>新增课程测试通过1")
        # 1-4 再次列出课程
        retList1 = list(1, 400)
        #1-5 断言2
        self.assertEqual(retList0['total'] + 1,retList1['total'],'新增课程失败2')
        print(">>>>>新增课程测试通过3")



    @unittest.skip('skip的原因')
    def test002(self):
        print('方法二调用了')

