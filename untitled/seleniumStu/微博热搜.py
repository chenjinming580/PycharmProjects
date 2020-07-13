# author:JinMing time:2020-03-24

from selenium import webdriver
import re

import time
#加载浏览器驱动
from selenium import webdriver
import re

driver=webdriver.Chrome('F:\webdriver\selenium\webdriver\chromedriver.exe')
#打开浏览器
driver.get('https://m.weibo.cn/')
#点击大家都在搜
driver.find_element_by_class_name('m-search').click()
time.sleep(1)
#找到热搜大标签
hotlist=driver.find_element_by_class_name('m-col-2')
#在大标签中匹配热搜列表
hotlistly=hotlist.find_elements_by_class_name('m-item-box')
#取列表的最后一个元素，即微博热搜并点击
hotlistly[-1].click()
time.sleep(1)
#找到实时热点，每分钟更新一次
hotpoint=driver.find_element_by_css_selector('#app > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div > div')
# hotpoint=driver.find_element_by_class_name('card-title')
time.sleep(1)
hotDivSli = hotpoint.find_elements_by_class_name('card4')
print(hotDivSli)

for hotdiv in hotDivSli:
    #判断这行有没有图片标签
    iconSli = hotdiv.find_elements_by_class_name("m-link-icon")
    if iconSli:
        #获取img标签
        img= iconSli[0].find_element_by_tag_name('img')
        #获取src属性
        srcLink = img.get_attribute('src')
        if "hot" in srcLink:
            hotType = "热"
            hotText = hotdiv.find_element_by_class_name("m-text-cut").text
            print(f'{hotType}: {hotText}')
        elif "new" in srcLink:
            hotType = "新"
            hotText = hotdiv.find_element_by_class_name("m-text-cut").text
            print(f'{hotType}: {hotText}')
        elif "fei" in srcLink:
            hotType = "沸"
            hotText = hotdiv.find_element_by_class_name("m-text-cut").text
            print(f'{hotType}: {hotText}')


time.sleep(5)


driver.quit()













