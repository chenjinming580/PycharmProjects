*** Settings ***
Variables  config/cfg.py

*** Keywords ***
Setup WebTest
    Open Browser   http://localhost/mgr/login/login.html    chrome
    Set Selenium Implicit Wait   10

TearDown WebTest
    Close Browser

loginwebsite
    go to  ${MgrLoginUrl}
    set selenium implicit wait  10
    #登录
    input text    id=username    &{adminuser}[name]
    input text    id=password     &{adminuser}[pw]
    click element    css=.btn-success

addCourse
    [Arguments]   ${name}   ${desc}   ${idx}=1
    click element    css=[ng-click="showAddOne=true"]
    input text  css=[ng-model="addData.name"]   ${name}
    input text  css=[ng-model="addData.desc"]   ${desc}
    input text  css=[ng-model="addData.display_idx"]   ${idx}
    click element  css=[ng-click="addOne()"]

checkCourse
    [Arguments]   ${expect}
    ${course}  get text  css=tbody td:nth-child(2)
    should be true   $course==$expect


clearcourse
     loginwebsite
     set selenium implicit wait  2

     FOR  ${one}  IN RANGE   9999
     ${elements}  get webelements  css=[ng-click="delOne(one)"]
     RUN KEYWORD IF  $elements==[]  EXIT FOR LOOP
     CLICK ELEMENT  ${elements[0]}
     Click Element   css=button.btn-primary
     sleep  1
     END
     set selenium implicit wait  10


addteacher
    [Arguments]   ${realname}  ${username}   ${desc}    ${idx}  ${lesson}

    Click Element   css=ul.nav a[href*=teacher]
    Sleep  1  # wait for lesson info displayed


    Click Element   css=button[ng-click^=showAddOne]

    input text      css=input[ng-model='addEditData.realname']    ${realname}
    input text      css=input[ng-model='addEditData.username']    ${username}
    input text      css=textarea[ng-model='addEditData.desc']    ${desc}
    input text      css=input[ng-model='addEditData.display_idx']    ${idx}

    Select From List By Label   css=select[ng-model*=courseSelected]    ${lesson}
    Click Element    css=button[ng-click*=addTeachCourse]

    Click Element   css=button[ng-click^=addOne]

    sleep   1


GetCourseList

    Click Element   css=ul.nav a[ui-sref=course]
    Sleep  1  # wait for Course info displayed
    ${eles}=    Get Webelements    css=tr>td:nth-child(2)

    ${courses}=    create list
    FOR   ${ele}   IN   @{eles}
    log to console    ${ele.text}
    Append To List   ${courses}   ${ele.text}
    END

    [Return]   ${courses}


DeleteAllTeacher


    Click Element   css=ul.nav a[ui-sref=teacher]
    Sleep  1  # wait for Course info displayed

    Set Selenium Implicit Wait   2
    FOR   ${one}  IN RANGE  20
    sleep  1
    ${html}=  Get Webelement  tag=html
    ${eles}=  Evaluate   $html.find_elements_by_css_selector("*[ng-click^='delOne']")

    Exit For Loop If   $eles==[]
    Click Element   ${eles}[0]
    Click Element   css=.modal-footer .btn-primary
    END

    Set Selenium Implicit Wait   10
    Click Element   css=ul.nav a[ui-sref=teacher]
    Sleep  1  # wait for Course info displayed

    Set Selenium Implicit Wait   2
    FOR   ${one}  IN RANGE  20
    sleep  1
    ${html}=  Get Webelement  tag=html
    ${eles}=  Evaluate   $html.find_elements_by_css_selector("*[ng-click^='delOne']")

    Exit For Loop If   $eles==[]
    Click Element   @{eles}[0]
    Click Element   css=.modal-footer .btn-primary
    END
