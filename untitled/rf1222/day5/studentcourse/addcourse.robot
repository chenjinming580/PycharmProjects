*** Settings ***
Library  SeleniumLibrary

Resource  rclib/rclib.robot
Suite Setup  Setup WebTest
Suite Teardown  TearDown WebTest

*** Test Cases ***
case1
    [Setup]  clearcourse
     log to console   添加初中语文
     addCourse   初中语文  语文  1
     checkCourse  初中语文


case2
    [Setup]  clearcourse
    log to console  添加初中数学
    addCourse   初中数学  初中数学  1
    checkCourse  初中数学

