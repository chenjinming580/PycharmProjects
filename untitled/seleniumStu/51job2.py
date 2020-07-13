# author:JinMing time:2020-03-30
'''
登录http: // www.51job.com
点击高级搜索
输入搜索关键词python
地区选择杭州
职能类别选计算机软件 -> 高级软件工程师
公司性质选外资欧美
工作年限选1 - 3年
搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息
python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8 - 1.6
万 / 月 | 04 - 27
Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1 - 1.5
万 / 月 | 04 - 27
'''

from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome('F:\\Tool\selenium\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('http://www.51job.com')
#找到高级搜索
driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/a').click()
#输入python
driver.find_element_by_css_selector('.el #kwdselectid').send_keys('python')
#找到关键字+标签
driver.find_element_by_xpath('//*[@id="work_position_click"]/em').click()
#去掉已选择
while driver.find_elements_by_css_selector("#work_position_click_multiple_selected > span"):
    driver.find_element_by_css_selector("#work_position_click_multiple_selected > span").click()



# 找到杭州并且点击
driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200").click()
# 点击确定按钮
driver.find_element_by_id("work_position_click_bottom_save").click()
#找到职能类别标签+
driver.find_element_by_css_selector('#funtype_div #funtype_click').click()
#找到后端开发
driver.find_element_by_xpath('//*[@id="funtype_click_center_right_list_category_0100_0100"]').click()
#找到高级软件工程师
driver.find_element_by_xpath('//*[@id="funtype_click_center_right_list_sub_category_each_0100_0106"]').click()
#找到确定按钮并点击
driver.find_element_by_xpath('//*[@id="funtype_click_bottom_save"]').click()
time.sleep(1)
#找到行业类型标签+
driver.find_element_by_xpath('//*[@id="indtype_click"]').click()
#找到计算机软件
driver.find_element_by_xpath('//*[@id="indtype_click_center_right_list_category_01_01"]').click()
#找到确定按钮并点击
driver.find_element_by_xpath('//*[@id="indtype_click_bottom_save"]').click()
#找到公司性质下拉框并点击
driver.find_element_by_css_selector('#cottype_list .i_arrow').click()
driver.find_element_by_css_selector('span[title=\'民营公司\']').click()
#找到工作年限
driver.find_element_by_css_selector('#workyear_list .i_arrow').click()
driver.find_element_by_css_selector('span[title=\'5-10年\']').click()
#点击搜索按钮
driver.find_element_by_css_selector('.btnbox .p_but').click()

el_title=driver.find_element_by_class_name('dw_table')
el_titles=el_title.find_elements_by_class_name('el')



for titleobject in el_titles:
    if 'title' in titleobject.get_attribute('class'):
        continue
    jobs=titleobject.find_elements_by_tag_name('span')
    for one in jobs:
        print(one.text,end='|')
    print()
driver.quit()
