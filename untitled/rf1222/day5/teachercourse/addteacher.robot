*** Settings ***
Library  SeleniumLibrary
Library  Collections
#Suite Setup  delteacher
Resource  rclib/rclib.robot
Suite Setup    Setup WebTest
Suite Teardown    TearDown WebTest


*** Test Cases ***
#case1
#   log to console  检查课程是否存在
#   checkcourse
#
#
#case2
#    log to console   选择初中语文
#    addteacher  张三  123  123  2  初中语文
#
#case3
#    log to console  选择初中化学
#    addteacher  李四  456  456  1   初中数学



case1
    loginwebsite
    log to console  检查课程是否存在
    @{courselist}  GetCourseList
    log to console  ${courselist}
    SHOULD BE TRUE     $courselist==['初中数学','初中语文']


case2
    loginwebsite
    log to console   删除所有老师
    DeleteAllTeacher



case3
      loginwebsite
      addteacher  123  234  2323  1  初中语文


case4
      loginwebsite
      addteacher  1233  2343  2323  2  初中数学