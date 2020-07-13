*** Keywords ***
loginwebsite
    open browser  http://localhost/mgr/login/login.html   chrome
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
