*** Settings ***
Suite Setup   log to console   执行套件初始化~~~~~~
Suite Teardown  log to console  执行套件清除动作~~~~~~
Test Setup  log to console   执行默认初始化
Test Teardown  log to console  执行默认清除

*** Test Cases ***
setupANDteardown
    [Setup]  fail
    #任何情况下setup与 teardown都会执行，即使用例主体出错
    [Teardown]  log to console  执行用例清除动作$$$
    #如果setup失败，用例主体不会执行
    log to console  执行用例主体
    should be true  1>2

setupANDteardown1
    [Setup]  log to console    执行初始化动作####
    #任何情况下setup与 teardown都会执行，即使用例主体出错
    #如果setup失败，用例主体不会执行
    log to console  执行用例主体
    should be true  1>2

setupANDteardown2
    [Teardown]  log to console  执行用例清除动作$$$
    #任何情况下setup与 teardown都会执行，即使用例主体出错
    #如果setup失败，用例主体不会执行
    log to console  执行用例主体
    should be true  1>2