*** Settings ***
Resource   rflib/rc.robot
Force Tags  添加老师  回归测试

*** Test Cases ***
添加老师1
   [Setup]  run keywords   deleteAllTeacher   AND   deleteAllLesson
   ...     AND    addcourse  初中语文    语文课    2
   ...     AND    addCourse   初中数学    数学课   1
   [Teardown]  run keywords   deleteAllTeacher   AND   deleteAllLesson
    addTeacher  小章老师   xiaozhang   语文老师   1   初中语文
    checkTeacher    小章老师

#*** Keywords ***
#techersetup
#    deleteAllTeacher
#    deleteAllLesson
#    addcourse  初中语文    语文课    2
#    addCourse   初中数学    数学课   1