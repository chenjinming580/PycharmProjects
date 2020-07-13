*** Settings ***
*** Test Cases ***
case1
      ${list}   evaluate  [one for one in range(10)]
      log to console  ${list}
      should be true  [0,1,2,3,4,5,6,7,8,9]==$list