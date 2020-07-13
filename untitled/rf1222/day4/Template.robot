*** Settings ***
Resource    rclib.robot    #导入资源文件

*** Test Cases ***
case1
    [Template]    datadriven
    #不写关键字，写关键字的参数
    20200521
    20200522
    20200523
    20200524


case2---不能作为数据驱动的方案
    ${datas}   realExceldata    filepath.xls
    FOR  ${data}   IN  @{datas}
        datadriven   ${data}
    END


*** Keywords ***
datadriven
    [Arguments]   ${date}
    ${res}  checklog3   ${date}
    log to console  ${res}