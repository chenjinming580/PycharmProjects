# author:JinMing time:2020-04-16
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
    'appPackage':'io.manong.developerdaily',
    'appActivity':'io.toutiao.android.ui.activity.LaunchActivity',
    'skipServerInstallation':True,
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000,
    #设置底层测试驱动-1.15默认使用的底层驱动就是UiAutomator2
    'automationName':'UiAutomator2'#或者UiAutomator1
}

#初始化driver对象-用于控制手机-启动被测应用
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素
title=driver.find_elements_by_xpath('//*[@resource-id=\'io.manong.developerdaily:id/home_feature_recycler_view\']//*[@resource-id=\'io.manong.developerdaily:id/tv_title\']')
titleTest=title[0].text
title[0].click()

time.sleep(2)
checkTitle=driver.find_element_by_id('io.manong.developerdaily:id/tv_title').text
#检查断点
assert titleTest==checkTitle
#返回
driver.press_keycode(4)
time.sleep(2)
#检查返回页面
titleList=driver.find_elements_by_class_name('android.widget.TextView')
firstTitle=titleList[0].text
assert firstTitle=='精选'



