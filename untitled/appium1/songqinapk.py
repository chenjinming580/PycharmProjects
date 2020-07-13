
# author:JinMing time:2020-04-15

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
    'appPackage':'com.sqauto',
    'appActivity':'.MainActivity',
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


#取屏幕中心
w_size=driver.get_window_size()
w_width=w_size['width']
w_height=w_size['height']
start_x=w_width/2
start_y=w_height/2

# #取元素滑动距离
ibox=driver.find_element_by_xpath('//android.widget.ScrollView//android.widget.ImageView[1]')
distace=ibox.size['height']

driver.implicitly_wait(0)#稳定元素
while True:
    driver.swipe(start_x,start_y,start_x,start_y-distace)
    ele=driver.find_elements_by_accessibility_id('user favorite')
    if ele:
        break
driver.implicitly_wait(10)#稳定元素

eles=driver.find_elements_by_xpath('//android.widget.ScrollView//android.widget.ImageView/following-sibling::android.widget.TextView[1]')
ele=eles[1:1+5]
elelist=[]
for i in ele:
    elelist.append(i.text)
print('最佳应用为:\n'+ '\n'.join(elelist))








