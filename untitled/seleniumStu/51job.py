# author:JinMing time:2020-03-28
from selenium import webdriver
import time

driver=webdriver.Chrome('F:\webdriver\selenium\chromedriver\chromedriver.exe')
driver.implicitly_wait(10)

driver.get('http://www.51job.com')
inputObject=driver.find_element_by_xpath('//*[@id="kwdselectid"]')
inputObject.click()
inputObject.send_keys('python')
# inputObject.submit()
driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/button').click()


driver.find_element_by_id('work_position_input').click()

hiticy=driver.find_element_by_xpath('//*[@id="work_position_click_multiple_selected"]')

hitcitys=hiticy.find_elements_by_class_name('ttag')
for delcity in hitcitys:
    delone=delcity.find_element_by_tag_name('em')
    delone.click()


tab=driver.find_element_by_xpath('//*[@id="work_position_click_center_right_list_000000"]/table/tbody/tr[1]/td[7]')
tab.find_element_by_tag_name('em').click()

driver.find_element_by_xpath('//*[@id="work_position_click_bottom_save"]').click()

driver.find_element_by_xpath('/html/body/div[2]/form/div/div[1]/button').click()


el_title=driver.find_element_by_class_name('dw_table')
el_titles=el_title.find_elements_by_class_name('el')



for titleobject in el_titles:
    if 'title' in titleobject.get_attribute('class'):
        continue
    jobs=titleobject.find_elements_by_tag_name('span')
    for one in jobs:
        print(one.text,end='|')
    print()


    # strField=[one.text for one in jobs]
    # print('|'.join(strField))


driver.quit()