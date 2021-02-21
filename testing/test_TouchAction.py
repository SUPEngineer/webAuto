import time

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchAction:
    def setup(self):
        # 初始化webdriver时要加上这个option参数
        # chromedriver都会默认把W3C协议设置为true
        # 而TouchAction这种鼠标操作本质是不符合W3C标准协议的操作
        option = webdriver.ChromeOptions()
        option.add_experimental_option("w3c", False)
        self.driver = webdriver.Chrome(options=option)

        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_scroll(self):
        self.driver.get('https://www.baidu.com')
        actions = TouchActions(self.driver)
        elem = self.driver.find_element(By.ID, "kw")
        search_elem = self.driver.find_element(By.ID, "su")
        elem.send_keys('selenium')
        actions.tap(search_elem)
        actions.perform()
        time.sleep(3)
        actions.scroll_from_element(elem, 0, 10000)
        actions.perform()
        time.sleep(3)
