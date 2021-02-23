# @Time : 2021/2/23 15:24 
# @Author : qiulingfeng
# @File : base.py
from selenium import webdriver


class Base():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
