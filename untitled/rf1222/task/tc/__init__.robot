*** Settings ***
Library   pylib.WebOpAdmin
Variables  cfg/cfg.py

Suite Setup    setupwebtest
Suite Teardown  teardownwebtest
Force Tags  回归测试