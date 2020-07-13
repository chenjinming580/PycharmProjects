# author:JinMing time:2020-05-25
# -*- coding: utf-8 -*-
import time

from selenium import webdriver

def deleteAllLesson():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    #登录
    driver.get('http://localhost/mgr/login/login.html')
    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('username').send_keys('auto')
    driver.find_element_by_id('password').clear()
    driver.find_element_by_id('password').send_keys('sdfsdfsdf')
    driver.find_element_by_css_selector('.btn-success').click()
    #删除课程
    driver.implicitly_wait(1)
    while 1:
        del_btns = driver.find_elements_by_css_selector('[ng-click="delOne(one)"]')
        #判断当删除按钮没有时，退出删除课程操作
        if del_btns==[]:
            break

        del_btns[0].click()#点击删除按钮
        #点击确认框
        driver.find_element_by_css_selector('.btn-primary').click()
        #等待弹出框消失
        time.sleep(1)
    driver.implicitly_wait(10)

    driver.quit()



if __name__ == '__main__':
    deleteAllLesson()