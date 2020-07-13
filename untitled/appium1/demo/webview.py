# author:JinMing time:2020-06-05
# -*- coding: utf-8 -*-
# coding=utf8
from appium import webdriver
import time
import traceback

desired_caps = {
    # 'automationName': 'UiAutomator2',
    'platformName': 'Android',
    'platformVersion': '6',
    'deviceName': 'test',
    'appPackage': 'com.example.jcy.wvtest',
    'appActivity': '.MainActivity',
    'chromedriverExecutableDir': r'C:\Tools\webdriver\chromedriver_win32_2.23',
    'noReset': True,
    'newCommandTimeout': 6000
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动Remote RPC
driver.implicitly_wait(10)

# 操作原始应用里的webview
try:
    # -----------------------
    # 查看手机当前的context
    print(driver.contexts)

    print(driver.current_context)
    # 如果处于NATIVE_APP,就切换到webview里面
    if driver.current_context == 'NATIVE_APP':
        driver.switch_to.context('WEBVIEW_com.example.jcy.wvtest')

    print(driver.current_context)

    # 此时可以操作web元素了
    driver.find_element_by_id('index-kw').send_keys('松勤\n')
    # driver.find_element_by_id('index-bn').click()

    res = driver.find_element_by_css_selector('#results>div:nth-child(1) header')

    print(res.text)

    print(driver.current_context)
    # 切回原生模式
    driver.switch_to.context('NATIVE_APP')
    print(driver.current_context)
    # 操作元素界面控件
    driver.find_element_by_accessibility_id('面板').click()
    time.sleep(3)
    driver.find_element_by_accessibility_id('通知').click()

    # -----------------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()