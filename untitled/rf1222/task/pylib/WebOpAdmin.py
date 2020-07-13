# author:JinMing time:2020-05-28
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
# 这是python的导法
# from rf1222.task.cfg.cfg import *

# 这是rf导法

from cfg.cfg import *


class WebOpAdmin():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def setupWebTest(self, driverType='chorme'):
        self.driver = None
        if driverType == 'chorme':
            self.driver = webdriver.Chrome()
        elif driverType == 'firefox':
            self.driver == webdriver.Firefox()
        else:
            raise Exception('unknow driver type %s' % driverType)
        self.driver.implicitly_wait(10)

    def tearDownWebTest(self):
        self.driver.quit()

    def DeleteAll(self, deletetype):
        if deletetype == 'course':
            self.driver.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()
        elif deletetype == 'teacher':
            self.driver.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()
        elif deletetype == 'training':
            self.driver.find_element_by_css_selector('ul.nav a[ui-sref=training]').click()
        elif deletetype == 'traininggrade':
            self.driver.find_element_by_css_selector('ul.nav a[ui-sref=traininggrade]').click()
        self.driver.implicitly_wait(2)
        while True:
            delButtons = self.driver.find_elements_by_css_selector('*[ng-click^=delOne]')

            if delButtons == []:
                break

            delButtons[0].click()
            self.driver.find_element_by_css_selector('.modal-footer  .btn-primary').click()
            time.sleep(1)
        self.driver.implicitly_wait(10)

    def loginWebSite(self):
        self.driver.get(MgrLoginUrl)
        ele = self.driver.find_element_by_id('username')
        ele.clear()
        ele.send_keys('auto')
        ele = self.driver.find_element_by_id('password')
        ele.clear()
        ele.send_keys('sdfsdfsdf')

        self.driver.find_element_by_tag_name('button').click()

    def AddCourse(self, name, desc, idx):
        self.driver.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()

        self.driver.find_element_by_css_selector('button[ng-click^=showAddOne]').click()

        ele = self.driver.find_element_by_css_selector("input[ng-model='addData.name']")
        ele.clear()
        ele.send_keys(name)

        ele = self.driver.find_element_by_tag_name("textarea")
        ele.clear()
        ele.send_keys(desc)

        ele = self.driver.find_element_by_css_selector("input[ng-model='addData.display_idx']")
        ele.clear()
        ele.send_keys(idx)

        self.driver.find_element_by_css_selector('button[ng-click^=addOne]').click()

        time.sleep(2)

    def Addteacher(self, realname, username, desc, idx, lesson):
        self.driver.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()

        self.driver.find_element_by_css_selector('button[ng-click^=showAddOne]').click()

        ele = self.driver.find_element_by_css_selector(
            "input[ng-model='addEditData.realname']")
        ele.clear()
        ele.send_keys(realname)

        ele = self.driver.find_element_by_css_selector(
            "input[ng-model='addEditData.username']")
        ele.clear()
        ele.send_keys(username)

        ele = self.driver.find_element_by_css_selector(
            "textarea[ng-model='addEditData.desc']")
        ele.clear()
        ele.send_keys(desc)

        ele = self.driver.find_element_by_css_selector(
            "input[ng-model='addEditData.display_idx']")
        ele.clear()
        ele.send_keys(idx)

        select = Select(self.driver.find_element_by_css_selector(
            'select[ng-model*=courseSelected]'))
        select.select_by_visible_text(lesson)

        self.driver.find_element_by_css_selector('button[ng-click*=addTeachCourse]').click()

        self.driver.find_element_by_css_selector('button[ng-click^=addOne]').click()

        time.sleep(1)

    def ADDtraining(self, trainingname, desc, idex, *cotainlesson):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector('ul.nav a[ui-sref=training]').click()
        self.driver.find_element_by_css_selector('button[ng-click^=showAddOne]').click()
        ele = self.driver.find_element_by_css_selector('[ng-model="addEditData.name"]')
        ele.click()
        ele.send_keys(trainingname)
        ele = self.driver.find_element_by_css_selector('[ng-model="addEditData.desc"]')
        ele.click()
        ele.send_keys(desc)
        ele = self.driver.find_element_by_css_selector('[ng-model="addEditData.display_idx"]')
        ele.click()
        ele.send_keys(idex)
        # select = Select(self.driver.find_element_by_css_selector(
        #     '[ng-model="$parent.courseSelected"]'))
        self.driver.implicitly_wait(1)
        for one in cotainlesson:
            select = Select(self.driver.find_element_by_css_selector(
                '[ng-model="$parent.courseSelected"]'))
            select.select_by_visible_text(one)

            self.driver.find_element_by_css_selector('[ng-click="addEditData.addTeachCourse()"]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector('button[ng-click^=addOne]').click()

        time.sleep(1)

    def Addtraininggrade(self, EditData, desc, idex, cotainlesson):
        self.driver.find_element_by_css_selector('ul.nav a[ui-sref=traininggrade]').click()
        self.driver.find_element_by_css_selector('button[ng-click^=showAddOne]').click()
        ele = self.driver.find_element_by_css_selector('[ng-model="addEditData.name"]')
        ele.click()
        ele.send_keys(EditData)
        ele = self.driver.find_element_by_css_selector('[ng-model="addEditData.desc"]')
        ele.click()
        ele.send_keys(desc)
        ele = self.driver.find_element_by_css_selector('[ng-model="addEditData.display_idx"]')
        ele.click()
        ele.send_keys(idex)
        select = Select(self.driver.find_element_by_css_selector(
            '[ng-model="$parent.addEditData.training_id"]'))
        select.select_by_visible_text(cotainlesson)

        self.driver.find_element_by_css_selector('button[ng-click^=addOne]').click()

        time.sleep(1)

    def GetAlllist(self, gettype):
        if gettype == 'course':
            self.driver.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()
        elif gettype == 'teacher':
            self.driver.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()
        elif gettype == 'training':
            self.driver.find_element_by_css_selector('ul.nav a[ui-sref=training]').click()
        elif gettype == 'traininggrade':
            self.driver.find_element_by_css_selector('ul.nav a[ui-sref=traininggrade]').click()
        self.driver.implicitly_wait(2)
        # 试试 //tr/td[2]/span/text()
        eles = self.driver.find_elements_by_css_selector('tr>td:nth-child(2)')

        return [ele.text for ele in eles]


if __name__ == '__main__':
    one = WebOpAdmin()
    one.setupWebTest('chorme')
    one.loginWebSite()
    one.ADDtraining('测试', '测试', 1, '初中语文', '初中数学')

    # list=one.GetAlllist('teacher')
    # one.DeleteAll('course')
    # print(list)
