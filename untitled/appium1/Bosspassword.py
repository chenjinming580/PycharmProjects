# author:JinMing time:2020-04-15

#导包
from appium import webdriver
from appium1.setting import *
class bossZP:
#准备自动化配置信息
    def __init__(self):
        caps={
        #移动设备平台
        'platformName':'Android',
        #平台OS版本号,写整数位即可
        'plathformVersion':'6',
        #设备的名称--值可以随便写
        'deviceName':'test0106',
        #提供被测app的信息-包名，入口信息
        # adb shell dumpsys activity recents | findstr intent
        'appPackage':'com.hpbr.bosszhipin',
        'appActivity':'.module.launcher.WelcomeActivity',
        'skipServerInstallation':True,
        #确保自动化之后不重置app
        'noReset':True,
        #设置session的超时时间，单位秒
        'newCommandTimeout':6000,
        #设置底层测试驱动-1.15默认使用的底层驱动就是UiAutomator2
        'automationName':'UiAutomator2'#或者UiAutomator1
        }

        #初始化driver对象-用于控制手机-启动被测应用
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
        self.driver.implicitly_wait(10)#稳定元素

    def get_password(self):
        self.new_password=input('请输入新密码:')
        self.old_passeord=input('请输入旧密码:')

    def change_password(self):
    #找到我的元素
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/fl_tab_4_red_dot').click()
        #找到设置图标
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/iv_general_settings').click()
        #找到账户与绑定
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/cl_item').click()
        #找到修改密码
        self.driver.find_element_by_xpath('//*[@resource-id=\'com.hpbr.bosszhipin:id/rv_list\']/android.widget.LinearLayout[2]').click()
        #输入旧密码
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_old').send_keys(self.old_passeord)
        #输入新密码
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new').send_keys(self.new_password)
        #确认密码
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_new_confirm').send_keys(self.new_password)
        #点击修改密码
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_save').click()


    def login(self):
        #找到账户密码登录
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_password_login').click()
        #输入密码
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/et_password').send_keys(self.new_password)
        #点击登录
        self.driver.find_element_by_id('com.hpbr.bosszhipin:id/btn_login').click()


    def __del__(self):
        self.driver.quit()


if __name__ == '__main__':
    boss = bossZP()
    boss.get_password()
    boss.change_password()
    boss.login()


