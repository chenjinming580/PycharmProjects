# author:JinMing time:2020-03-31
'''
打开 12306 网站  https://kyfw.12306.cn/otn/leftTicket/init

出发城市 填写 ‘南京南’， 到达城市 填写 ‘杭州东’

发车时间 选 06:00--12:00

发车日期选当前时间的下一天，也就是日期标签栏的，第二个标签

我们要查找的是所有 二等座还有票的车次，打印出这些有票的车次的信息，结果如下：

G7641
G1505
G7393
G7689
'''
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome('F:\\Tool\selenium\chromedriver.exe')
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
driver.implicitly_wait(10)
driver.maximize_window()
#找到出发地
driver.find_element_by_css_selector('input#fromStationText').click()
driver.find_element_by_id('nav_list4').click()
driver.find_element_by_css_selector('[title=\'南京南\']').click()
#找到目的地
driver.find_element_by_css_selector('input#toStationText').click()
driver.find_element_by_id('nav_list3').click()
driver.find_element_by_css_selector('[title=\'杭州东\']').click()
#选择出发时间
ele=driver.find_element_by_css_selector('select#cc_start_time')
Select(ele).select_by_visible_text("06:00--12:00")
#选择出发日期
driver.find_element_by_css_selector('#date_range > ul > li:nth-child(2) > span:nth-child(1)').click()
# 获取所有的车次信息
trainSli = driver.find_elements_by_css_selector("#queryLeftTable > tr[class]")
# 迭代列表
for train in trainSli:
    # 获取本车次的二等座信息
    secondSeat = train.find_elements_by_css_selector("tr>td")
    #     # 二等座无票, 则跳过
    if secondSeat[3].text in ["无", "--", "候补"]:
        continue
    # 有票, 获取 车次
    print(train.find_element_by_css_selector("a[title=\"点击查看停靠站信息\"]").text)

driver.quit()







#queryLeftTable>#ticket_5l000D323901>td