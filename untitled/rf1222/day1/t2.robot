#库的导入需要放到配置表
*** Settings ***
Library  SeleniumLibrary     #库名称大小写敏感
#注释内容，和python一样

#RF用例需要写在用例表里面

*** Test Cases ***
#标题需要顶格来写
用例1
    #配置部分用于写用例的说明和其他一些功能
    [Documentation]  用例的说明--webUI自动化-百度松勤
    [Tags]     smoketest   回归测试

#用例步骤由关键字和参数组成，需要另起一行，并且空两个以上的空格
#关键字如果由参数，需要和关键字空两个以上的空格，参数之间也是一样的
#再RF语法里面，RF通过两个以上的空格区分关键字和参数，两个以上的空格相当于分割符
    open browser    https://www.baidu.com     松勤\n/   chrome
    input text      id=kw
    set selenium implicit wait    1
    ${res}          get text                 id=1
    should contain  ${res}        松勤网 - 松勤软件测试
    close browser
