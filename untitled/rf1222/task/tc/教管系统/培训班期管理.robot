*** Settings ***
Library  pylib.WebOpAdmin
Suite Setup  DeleteAll  traininggrade

Force Tags   培训班期管理



*** Test Cases ***
case1
    log to console  添加培训班
    Addtraininggrade  初中班1期  测试  2  初中培训班
    ${traininglist}  GetAlllist  traininggrade
    should be true  ['初中班1期']==$traininglist