*** Keywords ***
Setup WebTest
    Open Browser   http://localhost/mgr/login/login.html    chrome
    Set Selenium Implicit Wait   10

TearDown WebTest
    Close Browser

loginwebsite
    go to   http://localhost/mgr/login/login.html
    set selenium implicit wait  10
    #登录
    input text    id=username     auto
    input text    id=password     sdfsdfsdf
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





