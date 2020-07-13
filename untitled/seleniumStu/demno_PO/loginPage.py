# author:JinMing time:2020-06-05
# -*- coding: utf-8 -*-
from seleniumStu.demno_PO.basePage import basePage
from selenium.webdriver.common.by import By


class LoginPage(basePage):
    def __init__(self):
        # 执行父类的构造方法
        super().__init__()
        # 用户名输入框元素
        self.userNameInput = (By.ID, "username")
        # 密码输入框
        self.passwordInput = (By.ID, "password")
        # 登录按钮
        self.loginButton = (By.TAG_NAME, "button")
        # # 根据登录按钮去找
        # self.xx = (By.CSS_SELECTOR, "div[class]")

    # 抽离出具体的元素控件
    def userNameInputBox(self):
        return self.get_element(self.userNameInput)

    # 密码输入框元素对象
    def passwordInputBox(self):
        return self.get_element(self.passwordInput)

    # 登录按钮
    def loginButtonBox(self):
        return self.get_element(self.loginButton)
    # # xx
    # def xx(self):
    #     self.loginButtonBox().find_element()


class LoginPageAction(LoginPage):
    def login(self):
        self.userNameInputBox().clear()
        self.userNameInputBox().send_keys("auto")
        self.passwordInputBox().clear()
        self.passwordInputBox().send_keys("sdfsdfsdf")
        self.loginButtonBox().click()


if __name__ == '__main__':
    LoginPageAction().login()