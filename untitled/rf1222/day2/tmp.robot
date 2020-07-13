*** Settings ***
Library    job.course_mgr

*** Test Cases ***

case1
#    ${var1}     returndict
    ${var1}     create dictionary  a=1  b=2  c=3
    FOR  ${one}  IN   &{var1}
    LOG TO CONSOLE     ${one}
    END
#    LOG TO CONSOLE     &{var1}

case2
    ${var2}  create dictionary  a=1  b=2  c=3
    log to console  ${var2['a']}
#    log to console  ${var2}[a]


