# author:JinMing time:2020-04-23
firdir='F:/ceshhi.txt'
from selenium import webdriver
import time

with open(firdir,'r',encoding='UTF-8') as fo:
    CardInfo=fo.readlines()

driver=webdriver.Chrome('F:\webdriver\selenium\chromedriver.exe')
driver.get('http://60.173.223.54/hthl-xxtd/admin/sms/query')
driver.implicitly_wait(10)

driver.find_element_by_css_selector('input.form-control[name="userName"]').send_keys('admin')
driver.find_element_by_css_selector('input.form-control[name="password"]').send_keys('1a2b3c.')
driver.find_element_by_class_name('btn.btn-primary.btn-block.btn-flat').click()
driver.find_element_by_class_name('btn.btn-default.ok').click()
driver.find_element_by_id('sendSms').click()
for one in CardInfo:
    infolis=one.split('\t')
    if len(infolis)>0:
        mobile=infolis[0].strip()
        info=infolis[1].strip()
        driver.find_element_by_id('admin_toMobiles').send_keys(mobile)
        driver.find_element_by_id('admin_content').send_keys(info)
        driver.find_element_by_id('smsSendBtn').click()
        driver.find_element_by_class_name('btn.btn-default.ok').click()
        time.sleep(1)
        driver.find_element_by_id('sendSms').click()
    else:
        continue

driver.quit()










