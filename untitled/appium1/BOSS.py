# author:JinMing time:2020-04-09
#导包
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
    'appPackage':'com.hpbr.bosszhipin',
    'appActivity':'.module.launcher.WelcomeActivity',
    # 'skipServerInstallation':True,
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

#点击放大镜
eles=driver.find_elements_by_id('com.hpbr.bosszhipin:id/img_icon')#先取所有符合条件的元素
#找到第二个元素--放大镜
btn=eles[1]
btn.click()

#搜索框输入职位信息
search_input=driver.find_element_by_id('com.hpbr.bosszhipin:id/et_search')
search_input.send_keys('软件测试')#输入参数

#选择符合条件的第一个搜索结果
driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_filtered_name').click()




#获取当前页面所有职位信息元素
job_msg=driver.find_elements_by_id('com.hpbr.bosszhipin:id/view_job_card')

print (job_msg)

for job in job_msg:
    #输出岗位名称
    name=job.find_element_by_id('com.hpbr.bosszhipin:id/tv_position_name').text
    # print(name.text)
    #输出薪资
    salray=job.find_element_by_id('com.hpbr.bosszhipin:id/tv_salary_statue').text
    # print(salray.text)
    #输出公司名称
    companys=job.find_elements_by_id('com.hpbr.bosszhipin:id/tv_company_name')
    if companys:
        company=companys[0].text
    else:
        company=''

    print('%s|%s|%s'%(name,salray,company))



# input('......')


driver.quit()