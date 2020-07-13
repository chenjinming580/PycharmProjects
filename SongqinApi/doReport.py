# author:JinMing time:2020-04-23
from ClassicHTMLTestRunner import HTMLTestRunner
import unittest
from demo.unittestcase.demo_unittest import DemoUnittest
from demo.unittestcase.demo_unittest2 import DemoUnittest2
from ClassicHTMLTestRunner import HTMLTestRunner

#（一）构建测试套件 test_suite
#1-1 方法一：用例逐个添加到suite
# suite=unittest.TestSuite()

# suite.addTest(DemoUnittest("test001"))
# suite.addTest(DemoUnittest("test003"))
# suite.addTest(DemoUnittest("test002")) #skip
# suite.addTest(DemoUnittest2("test021"))


#1-2 方法二：用例放入列表中，再添加到suite
# list=[DemoUnittest("test001"),
#       DemoUnittest("test002"),
#       DemoUnittest("test003"),
#       DemoUnittest2("test021")]
# suite.addTests(list)


#1-3 方法三：通过TestLoader类的discover 方法来  ok
suite=unittest.defaultTestLoader.discover('demo.unittestcase',pattern='demo_unittest*.py')


#（二）测试运行器查看结果
#2-1 第1种情况：不使用HtmlTestRunner插件
# runner=unittest.TextTestRunner()
# runner.run(suite)

#2-2 第2种情况：使用【经典版】HtmlTestRunner插件  ok

path=r"F:\PycharmProjects\SongqinApi\report\htmlReport.html"
reportFile=open(path,'wb')
#第三方插件HTMLTestRunner 可以返回一个runner对象
runner=HTMLTestRunner(stream=reportFile,verbosity=2,description='用例执行明细',
                      title='xxx项目的测试报告',tester='陈金明')
runner.run(suite)



