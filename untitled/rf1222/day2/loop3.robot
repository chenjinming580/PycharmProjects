*** Settings ***
Library  mylib3

*** Test Cases ***

range用法
    [Documentation]    Loops over values from 0 to 9
    :FOR    ${index}    IN RANGE    10
    \    Log To Console    ${index}


Start and end用法
    [Documentation]  Loops over values from 1 to 10
    :FOR    ${index}    IN RANGE    1    11
    \    Log To Console    ${index}

步长用法
    [Documentation]  Loops over values 5, 15, and 25
    :FOR    ${index}    IN RANGE    5    26    10
    \    Log To Console    ${index}