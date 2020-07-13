*** Settings ***
Library  t1
#Test Setup  deleteAllCourse

*** Test Cases ***
测试
    [Setup]   deleteAllCourse
    [Teardown]  deleteAllCourse
    add  初中化学111  测试  1
    add  初中化学2  测试11  22
    @{course}  list  1  10
    log to console  @{course}
    should contain  ${course}  初中化学2
#    should be true  初中化学 in ${course}
