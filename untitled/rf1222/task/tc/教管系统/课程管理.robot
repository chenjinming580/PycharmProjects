*** Settings ***
Library  pylib.WebOpAdmin
Suite Setup  deleteAll   course
Suite Teardown  deleteAll  course
Force Tags   课程测试



*** Test Cases ***
case1
    log to console  添加课程1
    AddCourse  初中语文  测试  2
    ${courselist}  GetAlllist  course
    should be true  ['初中语文']==$courselist

case2
    log to console  添加课程2
    AddCourse  初中数学  测试  1
    ${courselist}  GetAlllist  course
    should be true  ['初中数学' ,'初中语文']==$courselist













