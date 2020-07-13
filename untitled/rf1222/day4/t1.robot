*** Settings ***
Library  course
Library  SeleniumLibrary



*** Test Cases ***
测试1
    [Setup]  deleteAllLesson
    [Teardown]  deleteAllLesson
    loginWebSite   auto    sdfsdfsdf
    addCourse   robotframework   robot    1
    checkCourse    robotframework


测试2
    [Setup]  deleteAllLesson
    [Teardown]  deleteAllLesson
    loginWebSite   auto    sdfsdfsdf
    addCourse   selenium   webUI自动化    2
    checkCourse    selenium
    #校验


#case001
#    ${res}  getcourse
#    log to console  ${res}

*** Keywords ***
loginWebSite
    [Arguments]   ${username}    ${password}
    open browser  http://localhost/mgr/login/login.html   Chrome
    set selenium implicit wait  10
    input text    id=username    ${username}
    input text    id=password     ${password}
    click element   css=.btn-success

addCourse
    [Arguments]   ${name}    ${desc}   ${idx}
    #添加课程-点击添加课程
    click element  css=[ng-click="showAddOne=true"]
    #输入课程名称
    input text   css=[ng-model="addData.name"]   ${name}
    #输入详情描述
    input text  css=[ng-model="addData.desc"]    ${desc}
    #输入展示次序
    input text  css=[ng-model="addData.display_idx"]   ${idx}
    #点击确认
    click element  css=[ng-click="addOne()"]

checkCourse
    [Arguments]  ${expect}
    #获取系统中的课程
    ${eles}   get webelements    css=tr td:nth-child(2)
    ${course}    evaluate    [ele.text for ele in $eles]
    should be true     $expect in $course

#getCourse
#    #获取系统中的课程
#    ${eles}   get webelements    css=tr td:nth-child(2)
#    ${course}    evaluate    [ele.text for ele in $eles]
#    [Return]  ${course}  ${eles}