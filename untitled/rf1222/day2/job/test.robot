*** Settings ***
Library  course_mgr
Library  SeleniumLibrary
*** Test Cases ***
case1
  ${list}  listCourse  1  11
  FOR  ${one}  IN  @{list}
  log to console  ${one}
  END

  ${lesson}  CREATE LIST  大学英语158822359448  大学英语15882236645393
  FOR  ${a}  IN  @{lesson}
  log to console  ${a}
  should contain  ${list}  ${a}
  END

case2
  Open Browser  https://www.vmall.com/  chrome
  Set Selenium Implicit Wait  4
  ${ele}  Get Webelements  css=.span-968.fl .grid-list.clearfix .grid-title
  FOR  ${one}  IN  @{ele}
  log to console  ${one.text}
  END
  Close Browser
