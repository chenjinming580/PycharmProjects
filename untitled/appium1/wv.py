# author:JinMing time:2020-04-16
#导包
from appium import webdriver
import time

#准备自动化配置信息
desired_caps={
    #移动设备平台
    'platformName':'Android',
    #平台OS版本号,写整数位即可
    'plathformVersion':'6',
    #设备的名称--值可以随便写
    'deviceName':'test0106',
    #提供被测app的信息-包名，入口信息
    # adb shell dumpsys activity recents | findstr intent
    'appPackage':'com.example.jcy.wvtest',
    'appActivity':'.MainActivity',
    'skipServerInstallation':True,
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000,
    #设置底层测试驱动-1.15默认使用的底层驱动就是UiAutomator2
    'automationName':'UiAutomator2',#或者UiAutomator1
    'chromedriverExecutableDir':'F:\webdriver\selenium\chromedriver（2.28）'
}

#初始化driver对象-用于控制手机-启动被测应用
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素
print(driver.contexts)
print(driver.current_context)
time.sleep(2)

driver.switch_to.context('WEBVIEW_com.example.jcy.wvtest')
print(driver.current_context)

driver.find_element_by_css_selector('input.se-input.adjust-input').send_keys('松勤')
driver.find_element_by_css_selector('button#index-bn').click()

driver.switch_to.context('NATIVE_APP')
print(driver.current_context)

titleList=driver.find_elements_by_id('com.example.jcy.wvtest:id/icon')
titleList[-1].click()

