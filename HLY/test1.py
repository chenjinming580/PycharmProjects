from appium import webdriver

#准备自动化配置信息
desired_caps={
    #移动设备平台
    'platformName':'Android',
    #平台OS版本号,写整数位即可
    'plathformVersion':'10',
    #设备的名称--值可以随便写
    'deviceName':'test0106',
    #提供被测app的信息-包名，入口信息
    # adb shell dumpsys activity recents | findstr intent
    'appPackage':'com.ustcsoft.zshl.app',
    'appActivity':'.MainActivity',
    # 'skipServerInstallation':True,
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000,
    #设置底层测试驱动-1.15默认使用的底层驱动就是UiAutomator2
    'automationName':'UiAutomator2'#或者UiAutomator1
}

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素

driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()

driver.find_element_by_android_uiautomator('new UiSelector().text("免费办ETC")').click()
driver.find_element_by_android_uiautomator('new UiSelector().text("江苏ETC 卡+OBU")').click()
eles=driver.find_elements_by_android_uiautomator('new UiSelector().text("已完善")')
print(eles)



# for one in eles:
#     #取元素距离
#     weight=(one.size['width'])*0.5
#     print(weight)
#     height=(one.size['height'])*0.5
#     print(height)
#     distance=(one.size['width'])*0.5
#     driver.swipe(weight,height,weight,height,duration=500)






driver.find_element_by_android_uiautomator('new UiSelector().text("下一步")').click()
driver.find_element_by_android_uiautomator('new UiSelector().text("新增账户")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().text("慧易通账户 请选择已有账户")').click()
ele=driver.find_elements_by_android_uiautomator('new UiSelector().textMatches(".*正常")')
ele[0].click()
driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
ele=driver.find_elements_by_class_name('android.widget.EditText')
ele[2].send_keys('安徽')
driver.find_element_by_android_uiautomator('new UiSelector().text("提交")').click()
