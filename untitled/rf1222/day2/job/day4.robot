*** Test Cases ***
case1
   ${list}  create list  0  1  2  3  4  5
   FOR   ${one}  IN   @{list}
   log to console  ${one}
   RUN KEYWORD IF  $one=='0'   log to console  测试通过
   ...  ELSE  log to console  测试不通过
   END
