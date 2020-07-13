*** Settings ***
Library  pylib.WebOpAdmin
Suite Setup  run keywords  deleteAll   teacher  AND  deleteAll  course
...   AND  AddCourse  初中语文  测试  2
...   AND  AddCourse  初中数学  测试  1
Suite Teardown  run keywords  deleteAll  teacher  AND  deleteAll  course
Force Tags   老师管理



*** Test Cases ***
case1
    log to console  添加老师1
    Addteacher  小张  123  234  2  初中语文
    ${teacherlist}  GetAlllist  teacher
    should be true  ['小张']==$teacherlist

case2
    log to console  添加老师2
    Addteacher  小王  987  234  1  初中数学
    ${teacherlist}  GetAlllist  teacher
    should be true  ['小王','小张']==$teacherlist
