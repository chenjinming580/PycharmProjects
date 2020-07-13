# author:JinMing time:2020-06-05
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from seleniumStu.demno_PO.setting import driverPath, DOMIN, TIMEOUT, POLL_FREQUECY


class Driver:
    # 静态私有字段
    _driver = None

    @classmethod
    def get_driver(cls, browser_name="Chrome"):
        """
        获取浏览器对象
        :return:
        """
        if cls._driver is None:
            if browser_name == "Chrome":
                cls._driver = webdriver.Chrome(driverPath["Chrome"])
            elif browser_name == "Firefox":
                cls._driver = webdriver.Firefox(driverPath["Firefox"])
            # 省略号，其他的浏览器就不写了
            else:
                raise NameError("找不到浏览器")
        return cls._driver


class basePage:
    def __init__(self):
        # 浏览器对象
        self.driver = Driver.get_driver()
        # 访问网址
        self.driver.get(DOMIN)

    def get_element(self, locator):
        """
        重写了一个函数，定位、寻找元素
        提供一个显示等待
        :param locator: 元素对象 定位方法
        :return:
        """
        return WebDriverWait(
            # 传入浏览器对象
            driver=self.driver,
            # 传入超时时间
            timeout=TIMEOUT,
            # 设置轮询时间
            poll_frequency=POLL_FREQUECY
        ).until(
            # 定位元素是否可见
            ec.visibility_of_element_located(locator))
        # # 返回元素对象
        # return self.driver.find_element(*locator)


if __name__ == '__main__':
    from selenium.webdriver.common.by import By

    basePage().get_element((By.ID, "username")).send_keys("123")