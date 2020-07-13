# author:JinMing time:2020-05-26
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
from robot.api import logger
import time
def addteacher(name,username,desc,number,course):
    """

    :param name: 姓名
    :param username:用户名
    :param desc: 描述
    :param number: 次序
    :param course: 添加课程名称
    :return:
    """
    driver = webdriver.Chrome()
    driver.get('http://localhost/mgr/login/login.html')
    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('username').send_keys('auto')
    driver.find_element_by_id('password').clear()
    driver.find_element_by_id('password').send_keys('sdfsdfsdf')
    driver.find_element_by_css_selector('.btn.btn-success').click()
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector('[ui-sref="teacher"]').click()
    time.sleep(1)
    driver.find_element_by_css_selector('[ng-click="showAddOne=true"]').click()
    time.sleep(1)
    driver.find_element_by_css_selector('[ng-model="addEditData.realname"]').send_keys(name)
    driver.find_element_by_css_selector('[ng-model="addEditData.username"]').send_keys(username)
    driver.find_element_by_css_selector('[ng-model="addEditData.desc"]').send_keys(desc)
    driver.find_element_by_css_selector('[ng-model="addEditData.display_idx"]').clear()
    time.sleep(1)
    driver.find_element_by_css_selector('[ng-model="addEditData.display_idx"]').send_keys(number)
    ele = driver.find_element_by_css_selector('[ng-options="course as course.name for course in courseList"]')
    Select(ele).select_by_visible_text(course)
    driver.find_element_by_css_selector('.fa.fa-plus').click()
    driver.find_element_by_css_selector('[ng-click="addOne()"]').click()
    driver.quit()

def delteacher():
    driver = webdriver.Chrome()
    driver.get('http://localhost/mgr/login/login.html')
    driver.implicitly_wait(10)
    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('username').send_keys('auto')
    driver.find_element_by_id('password').clear()
    driver.find_element_by_id('password').send_keys('sdfsdfsdf')
    driver.find_element_by_css_selector('.btn.btn-success').click()
    driver.find_element_by_css_selector('[ui-sref="teacher"]').click()
    time.sleep(1)
    driver.implicitly_wait(1)
    while True:
        eles=driver.find_elements_by_css_selector('[ng-click="delOne(one)"]')
        if eles==[]:
            break
        else:
            eles[0].click()
            driver.find_element_by_css_selector('.btn.btn-primary').click()
            time.sleep(1)
    driver.implicitly_wait(10)
    driver.quit()

def checkcourse():
    driver = webdriver.Chrome()
    driver.get('http://localhost/mgr/login/login.html')
    driver.implicitly_wait(10)
    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('username').send_keys('auto')
    driver.find_element_by_id('password').clear()
    driver.find_element_by_id('password').send_keys('sdfsdfsdf')
    driver.find_element_by_css_selector('.btn.btn-success').click()
    time.sleep(2)
    eles=driver.find_elements_by_css_selector('tbody td:nth-child(2)')
    list=[one.text for one in eles]
    print(list)
    if ['初中数学','初中语文']==list:
        logger.console('课程存在')
    else:
        logger.console('课程不存在')
    driver.quit()




if __name__ == '__main__':
    checkcourse()
