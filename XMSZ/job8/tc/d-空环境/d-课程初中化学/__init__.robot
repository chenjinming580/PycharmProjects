*** Settings ***
Library    lib.courlib
Suite Setup    add  初中化学  客户  1  suitesetclassid
Suite Teardown    delete    ${suitesetclassid}


