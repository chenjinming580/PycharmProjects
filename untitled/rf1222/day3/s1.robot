*** Test Cases ***
条件判断
    ${year}   set variable  2020
    run keyword if   ${year}=='2020'      log to console  测试通过
    #should be true  ${year}=={"a":1}   #只有当关键字的参数是Python表达式的时候可以采用$变量名
    log to console  ${year}


条件判断2
    ${date}   get time
    run keyword if  '2020' in $date and '05' in $date
    ...     log to console  pass
    log to console  ${date}

条件判断3---条件成立只能执行一个关键字
    ${date}   get time
    run keyword if  '2020' in $date and '05' in $date
    ...     log to console  pass