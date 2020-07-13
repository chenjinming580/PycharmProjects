*** Test Cases ***
条件判断-分支
    ${date}   get time
    run keyword if  '2021' in $date   log to console  今年是2021年
    ...         ELSE     log to console  今年不是2021

条件判断-多分支
    ${date}   get time
    run keyword if   '2021' in $date   log to console  今年是2021年
    ...  ELSE IF    '05' in $date   log to console  现在是5月份
    ...  ELSE    log to console   现在天气很热