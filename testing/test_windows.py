# @Time : 2021/2/23 15:24 
# @Author : qiulingfeng
# @File : test_windows.py
from selenium.webdriver.common.by import By

from testing.base import Base
from time import sleep


class TestWindows(Base):
    def test_windows(self):
        self.driver.get("http://www.baidu.com/")
        self.driver.find_element(By.LINK_TEXT, '登录').click()
        sleep(2)
        self.driver.find_element(By.LINK_TEXT, '立即注册').click()
        sleep(2)
        # 切换新窗口
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(By.NAME, 'userName').send_keys("username")
        # 返回原来的窗口，点击用户名登录
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@title="用户名登录"]').click()
        self.driver.find_element(By.NAME, "userName").send_keys('user')
        self.driver.find_element(By.NAME, "password").send_keys('password')
        sleep(2)
