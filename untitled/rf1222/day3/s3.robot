*** Settings ***
Library  testlib3
Library  Dialogs


*** Test Cases ***
case1
    FOR  ${one}  IN RANGE  9999
    ${score}    get value from user  请输入你的分数
    #当用户输入over时候，结束循环-break
    run keyword if   $score=='over'    exit for loop
    #当用户输入cont时候，重新开始循环--continue
    run keyword if  $score=='cont'    continue for loop
    check score   ${score}
    END

case2
    FOR  ${one}  IN RANGE  9999
    ${score}    get value from user  请输入你的分数
    #当用户输入over时候，结束循环-break
    exit for loop if   $score=='over'
    continue for loop if  $score=='cont'
    #当用户输入cont时候，重新开始循环--continue
    check score   ${score}
    END