# author:JinMing time:2020-03-26
from selenium import webdriver #导入一个浏览器
from selenium.webdriver.common.action_chains import ActionChains  #导入鼠标操作
from selenium.webdriver.common.keys import Keys  #导入键盘
import time

driver=webdriver.Chrome('F:\webdriver\selenium\webdriver\chromedriver.exe') #打开浏览器
#打开头条网
driver.get('https://www.toutiao.com/')
driver.maximize_window()
time.sleep(1)
#找到今日头条 channel.channel-fixe元素
Title=driver.find_element_by_xpath(
    '/html/body/div/div[2]/div[1]/div/div')
#找到ul大标签
ul=Title.find_element_by_css_selector(
    'body > div > div.bui-box.container > div.bui-left.index-channel > div > div > ul')
#找到ul标签里的元素
ulList=ul.find_elements_by_class_name('channel-item')
#找到更多标签
MoreTitl=ul.find_element_by_xpath(
    '/html/body/div/div[2]/div[1]/div/div/ul/li[13]')
span=MoreTitl.find_element_by_tag_name('span')
#鼠标悬停更多标签
ActionChains(driver).move_to_element(span).perform()
#找到更多里面的ul大标签
rightTitle=MoreTitl.find_element_by_xpath(
    '/html/body/div/div[2]/div[1]/div/div/ul/li[13]/div/ul')
#找打ul大标签的bui-left元素
rightTitles=rightTitle.find_elements_by_class_name('bui-left')
#合成一个列表
Alltitle=ulList+rightTitles
for one in Alltitle:
    span = one.find_element_by_tag_name('span').text
    print(f'{span:*<10}')
time.sleep(1)
driver.quit()




