*** Settings ***
Library  Collections
Suite Setup   log to console   产生套件1所需数据
Suite Teardown   log to console   清除套件1产生数据

*** Test Cases ***
测试1
    [Setup]   log to console   生成用例1所需数据
    [Teardown]   log to console   清除用例1产生数据
    ${var}=   create list  hello   world
    append to list  ${var}   a   b    c
    log to console   ${var}
    fail

测试2
    [Setup]   log to console   生成用例1所需数据
    [Teardown]   log to console   清除用例1产生数据
    ${var}=   create list  hello   world
    append to list  ${var}   a   b    c
    log to console   ${var}

#自动化用例设计规范
#1.用例之间不可以存在耦合现象
#2.用例执行完成必须清除自身产生的测试数据，保证测试环境的整洁