*** Settings ***
Library  t1


*** Test Cases ***
循环1
    :FOR  ${var}   IN   a  b  c  d
    \   log to console  ${var}
    log to console  循环外面

循环2
    ${list}    get list
    FOR   ${var}   IN   @{list}
    log to console  ${var}
    END   #出循环体
    log to console  循环外面

循环的range
    FOR  ${var}  IN RANGE    1   10   2
    log to console  ${var}
    END   #出循环体
    log to console  循环外面

模拟while循环
    #不知道循环多少次，但是只要循环足够的次数就可以
    FOR  ${VAR}   IN RANGE   9999
    log to console  ${var}
    #加判断条件控制出循环
    END