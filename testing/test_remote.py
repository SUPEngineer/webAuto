# @Time : 2021/2/26 11:49 
# @Author : qiulingfeng
# @File : test_remote.py
import json

from selenium import webdriver
from time import sleep


class TestRemote():
    def setup(self):
        # 设置option参数，打开调试窗口
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    # def test_remote(self):
    #     self.driver.get("https://www.bilibili.com/")
    #
    #     sleep(3)

    def test_cookie(self):
        """
        使用cookie跳过登录
        :return:
        """
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        # 获取cookies
        # cookies = self.driver.get_cookies()
        # with open("cookies.txt", "w", encoding="utf-8") as f:
        #     json.dump(cookies, f)

        # 读取cookies
        with open("cookies.txt", "r", encoding="utf-8") as f:
            cookies = json.load(f)

        # 注入cookies
        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()
        sleep(6)
