*** Settings ***
Library  lib.teacherlib


*** Test Cases ***
添加老师001
   ${ret}  addTeacher  李世明   123456   李世明在世   老师   ${suitesetclassid}  1   suiteseteacherid
   should be true  $ret['retcode']==0
   [Teardown]  deleteTeacher  ${suiteseteacherid}




