# @Time : 2021/2/23 15:24 
# @Author : qiulingfeng
# @File : base.py
'''
执行时使用命令执行
browser=firefox pytest test_frame.py
即可方便得指定浏览器运行测试用例
'''
import os

from selenium import webdriver


class Base():
    def setup(self):
        browser = os.getenv('browser')
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
