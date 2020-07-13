*** Settings ***
Library  SeleniumLibrary
Resource  rclib.robot
Suite Setup        Setup WebTest
Suite Teardown     TearDown WebTest


*** Test Cases ***
case1
   [Setup]  clearcourse
   [Teardown]  clearcourse
   addCourse   robotframework   robot    1
   checkCourse    robotframework

case2
    [Setup]  clearcourse
    [Teardown]  clearcourse
    addCourse   selenium   selenium    1
   checkCourse    selenium
