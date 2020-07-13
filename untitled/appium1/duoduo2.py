# author:JinMing time:2020-04-13
#导包
from appium import webdriver

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
    'appPackage':'com.ibox.calculators',
    'appActivity':'.SplashActivity',
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
#找到元素9
driver.find_element_by_xpath('//*[@resource-id=\'com.ibox.calculators:id/digit9\']').click()
#找到元素+
driver.find_element_by_xpath('//*[@resource-id=\'com.ibox.calculators:id/plus\']').click()
#找到元素3
driver.find_element_by_xpath('//*[@resource-id=\'com.ibox.calculators:id/digit3\']').click()
#找到元素=
driver.find_element_by_xpath('//*[@resource-id=\'com.ibox.calculators:id/equal\']').click()
#找到元素*
driver.find_element_by_xpath('//*[@resource-id=\'com.ibox.calculators:id/mul\']').click()
#找到元素5
driver.find_element_by_xpath('//*[@resource-id=\'com.ibox.calculators:id/digit5\']').click()
#找到元素=
driver.find_element_by_xpath('//*[@resource-id=\'com.ibox.calculators:id/equal\']').click()


ele=driver.find_element_by_xpath('//*[@resource-id=\'com.ibox.calculators:id/cv\']/android.widget.TextView[2]')
if ele.text=='60':
    print('测试通过')
else:
    print('测试不通过')


driver.quit()

