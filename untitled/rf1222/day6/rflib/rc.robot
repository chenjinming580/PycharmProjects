*** Settings ***
Library  SeleniumLibrary
Variables  cfg/cfg.py

*** Keywords ***
loginwebsite
    [Arguments]
    #手动访问业务地址---相当于driver.get(url)
    go to    ${MgrLoginUrl}
    set selenium implicit wait  2
    #登录
    input text    id=username     &{user1}[name]
    input text    id=password     &{user1}[pw]
    click element    css=.btn-success

addCourse
    [Arguments]   ${name}   ${desc}   ${idx}=1
    #确保在课程界面
    click element  css=[ui-sref="course"]
    click element    css=[ng-click="showAddOne=true"]
    input text  css=[ng-model="addData.name"]   ${name}
    input text  css=[ng-model="addData.desc"]   ${desc}
    input text  css=[ng-model="addData.display_idx"]   ${idx}
    click element  css=[ng-click="addOne()"]

checkCourse
    [Arguments]   ${expect}
    #确保在课程界面
    click element  css=[ui-sref="course"]
    ${course}  get text  css=tbody td:nth-child(2)
    should be true   $course==$expect

deleteAllLesson

    #确保在课程界面
    click element  css=[ui-sref="course"]
    #删除课程
    set selenium implicit wait  2
    FOR  ${i}   IN RANGE    9999
        ${del_btns}   get webelements   css=[ng-click="delOne(one)"]
        #判断当删除按钮没有时，退出删除课程操作
        exit for loop if   $del_btns==[]
        #点击删除按钮
        click element   ${del_btns[0]}
        #点击确认框
        click element    css=.btn-primary
        #等待弹出框消失
        sleep  1
    END
    set selenium implicit wait  10


setupwebtest
    open browser  http://baidu.com   chrome
    set selenium implicit wait  10
    log to console  打开浏览器

teardownwebtest
    close browser
    log to console  关键浏览器


deleteAllTeacher
    #确保在老师界面
    click element  css=[ui-sref="teacher"]
    #开始删除课程
    set selenium implicit wait  3
    FOR  ${i}   IN RANGE    9999
        ${del_btns}   get webelements    css=[ng-click="delOne(one)"]
        #判断当删除按钮没有时，退出删除老师操作
        exit for loop if   $del_btns==[]
        #点击删除按钮
#        click element   ${del_btns[0]}
        evaluate    $del_btns[0].click()
        #点击确认框
        click element    css=.btn-primary
        #等待弹出框消失
        sleep  2
    END
    set selenium implicit wait  10

addTeacher
    [Arguments]   ${realname}   ${username}    ${desc}   ${idx}   ${course}
    #确保在老师界面
    click element  css=[ui-sref="teacher"]
    click element    css=[ng-click="showAddOne=true"]

    input text  css=[ng-model="addEditData.realname"]   ${realname}
    input text  css=[ng-model="addEditData.username"]   ${username}
    input text  css=[ng-model="addEditData.desc"]   ${desc}
    input text  css=[ng-model*="display_idx"]   ${idx}
    #关联授课信息
    select from list by label   css=[ng-model="$parent.courseSelected"]    ${course}

    click element   css=[ng-click="addEditData.addTeachCourse()"]
    click element  css=[ng-click="addOne()"]

checkTeacher
    [Arguments]   ${expect}
    #确保在老师界面
    click element  css=[ui-sref="teacher"]
    ${course}  get text  css=tbody td:nth-child(2)

    should be true   $course==$expect