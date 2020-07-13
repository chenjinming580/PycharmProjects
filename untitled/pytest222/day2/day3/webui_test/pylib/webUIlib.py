# author:JinMing time:2020-06-04
# -*- coding: utf-8 -*-
import time
from selenium import webdriver

driver=None
def websetup(url):
    global driver
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)

def webteardown():
    # global driver
    driver.quit()


def delete_all_courses():
    # global driver
    driver.find_element_by_css_selector('[ui-sref="course"]').click()
    driver.implicitly_wait(1)
    while 1:
        deleteBtn = driver.find_elements_by_css_selector('[ng-click="delOne(one)"]')
        if deleteBtn == []:
            break
        deleteBtn[0].click()
        driver.find_element_by_class_name('btn-primary').click()
        time.sleep(1)
    driver.implicitly_wait(10)

def add_course(name,desc,idx):
    # global driver
    driver.find_element_by_css_selector('[ui-sref="course"]').click()
    driver.find_element_by_css_selector('[ng-click="showAddOne=true"]').click()
    driver.find_element_by_css_selector('[ng-model="addData.name"]').send_keys(name)
    driver.find_element_by_css_selector('[ng-model="addData.desc"]').send_keys(desc)
    driver.find_element_by_css_selector('[ng-model="addData.display_idx"]').send_keys(idx)
    driver.find_element_by_css_selector('[ng-click="addOne()"]').click()
    time.sleep(1)

def check_course(name,exist=None):
    driver.find_element_by_css_selector('[ui-sref="course"]').click()
    driver.implicitly_wait(3)
    eles=driver.find_elements_by_css_selector('tbody td:nth-child(2)')
    course=[ele.text for ele in eles]
    if exist:
        assert name in course
    else:
        assert name not in course
    driver.implicitly_wait(10)

#根据课程名称删除
def delete_course(name):
    driver.find_element_by_css_selector('[ui-sref="course"]').click()

    eles=driver.find_elements_by_css_selector('tbody tr')
    for ele in eles:
        coures_name=ele.find_element_by_css_selector('td:nth-child(2)').text
        #查看课程是否为待删除的
        if coures_name == name:
            del_btn=ele.find_element_by_css_selector('[ng-click="delOne(one)"]')
            del_btn.click()
            driver.find_element_by_css_selector('.btn-primary').click()
            time.sleep(1)
            break



if __name__ == '__main__':
    websetup('http://localhost/mgr/ps/mgr/index.html#/')
    add_course('初中语文','语文课','3')
    # delete_course('初中语文')
    webteardown()