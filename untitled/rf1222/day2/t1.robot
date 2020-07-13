*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
case1
  ${var}   set variable  2000
  ${num}   convert to integer  2020
  ${folat}  convert to number  3.8
  log to console  ${var}
#  log  ${var}
#  sleep  1
#  should contain  ${var}  20
  should be equal  '2020'  '${num}'
#   should be true  'hello'.startswith('he')