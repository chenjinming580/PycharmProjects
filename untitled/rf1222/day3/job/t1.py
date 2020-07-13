# author:JinMing time:2020-05-23
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import requests
def deleteAllCourse():
    driver = webdriver.Chrome('F:\webdriver\selenium\chromedriver\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('http://localhost/mgr/ps/mgr/index.html#/')
    # list = driver.find_elements_by_css_selector('.table.table-hover .btn.btn-green')
    # for one in list:
    #     if one.text == '删除':
    #         one.click()
    #         time.sleep(2)
    #         delete1 = driver.find_element_by_css_selector('button.btn-primary')
    #         delete1.click()
    #         time.sleep(1)
    driver.implicitly_wait(1)
    while True:
        deleteButtons = driver.find_elements_by_css_selector(
            '[ng-click="delOne(one)"]')
        if deleteButtons:
            deleteButtons[0].click()
            driver.find_element_by_css_selector('button.btn-primary').click()
            time.sleep(1)
        else:
            break
    driver.implicitly_wait(10)
    driver.quit()


def add(name,desc,display_idx):
    try:
        header={'Content-Type':'application/x-www-form-urlencoded'}
        payload={
        'action':'add_course',
        'data':f'{{"name":"{name}","desc":"{desc}","display_idx":"{display_idx}"}}'}
        respon=requests.post('http://localhost/api/mgr/sq_mgr/',headers=header,data=payload)
        return respon.json()

    except:
        return {'retcode':888,'reason':'项目异常'}

def list(pagenum,pagesize):
    try:
        payload={'action':'list_course','pagenum':pagenum,'pagesize':pagesize}
        r=requests.get('http://localhost/api/mgr/sq_mgr/',params=payload)
        r.encoding="utf-8"
        list = r.json()
        return [one['name'] for one in list['retlist']]
    except:
        return {'retcode': 888, 'reason': '项目异常'}

if __name__ == '__main__':
    one=list(1,10)
    print(one)