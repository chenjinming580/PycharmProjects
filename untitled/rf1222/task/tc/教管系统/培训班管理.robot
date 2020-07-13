*** Settings ***
Library  pylib.WebOpAdmin
Suite Setup  run keywords  deleteAll   teacher  AND  deleteAll  course
...   AND  AddCourse  初中语文  测试  2
...   AND  AddCourse  初中数学  测试  1
#Suite Teardown  run keywords  deleteAll  teacher  AND  deleteAll  course
#...   AND  deleteAll  training
Force Tags   培训班管理


*** Test Cases ***

case1
    log to console  添加培训班
    ADDtraining  初中班   测试  2  初中语文  初中数学
    ${traininglist}  GetAlllist  training
    should be true  ['初中班','测试']==$traininglist


