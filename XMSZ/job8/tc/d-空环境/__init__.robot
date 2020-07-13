*** Settings ***
Library  lib.courlib
Library  lib.teacherlib



Suite Setup   run keywords  deleteAllteacher  1  100    AND   deleteallcourse  1  100

