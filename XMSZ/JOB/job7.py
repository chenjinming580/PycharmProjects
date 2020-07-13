# author:JinMing time:2020-07-06
# -*- coding: utf-8 -*-
'''
7、浏览器进入网页云音乐  https://music.163.com/
在首页的发现音乐菜单，点击进入排行榜>云音乐新歌版
查看排名前三的歌曲下的评论，在精彩评论部分找到点赞数量最高的评论，获取评论作者，内容，时间和当前点赞数量

'''

from selenium import webdriver
import time

driver = webdriver.Chrome(f'F:\webdriver\selenium\webdriver\chromedriver.exe')
driver.get('https://music.163.com/')
driver.maximize_window()
driver.implicitly_wait(10)
# 点击排行榜元素
driver.find_element_by_xpath('//*[@data-module="toplist"]').click()
time.sleep(1)

a = 0

while a < 3:
    ifrele = driver.find_element_by_css_selector('#g_iframe')
    driver.switch_to.frame(ifrele)
    time.sleep(1)
    driver.find_element_by_xpath('//ul[@class="f-cb"]//li[@data-res-id="3779629"]//a[@class="avatar"]').click()
    toplist = driver.find_elements_by_xpath('//*[@class="m-table m-table-rank"]//*[@class="rank"]')
    songname= toplist[a].find_element_by_xpath('.//*[@class="txt"]//b').get_attribute('title')
    toplist[a].find_element_by_xpath('.//*[@class="rpic"]').click()
    driver.execute_script('window.scrollBy(0,1000)')

    #取第一个为评论最多
    topcom=driver.find_element_by_css_selector('.cmmts.j-flag .itm:nth-of-type(1)')
    #找到评论作者
    comauthor=topcom.find_element_by_xpath('.//*[@class="s-fc7"]').text
    #找到评论内容
    comcontent=topcom.find_element_by_css_selector('.cmmts.j-flag .itm:nth-of-type(1) .cnt.f-brk').text
    comcontent=comcontent.split('：')[-1].strip()
    #找到评论时间
    comtime=topcom.find_element_by_css_selector('.cmmts.j-flag .itm:nth-of-type(1) .time.s-fc4').text
    #找到点赞数量
    pointnum=topcom.find_element_by_css_selector('.cmmts.j-flag .itm:nth-of-type(1) [data-type="like"]').text
    pointnum=pointnum.split('(')[-1].split(')')[0]
    print(f'第{a+1}名:\n歌曲名:{songname}\n评论内容:{comcontent}\n评论时间:{comtime}\n点赞数量:{pointnum}\n\n')

    a += 1
    driver.back()


driver.quit()

