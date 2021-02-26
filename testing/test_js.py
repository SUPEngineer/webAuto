# @Time : 2021/2/24 16:08 
# @Author : qiulingfeng
# @File : test_js.py
from time import sleep

from selenium.webdriver.common.by import By

from testing.base import Base


class TestJS(Base):
    def test_js(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element(By.ID, 'kw').send_keys('selenium测试')
        # 执行JS脚本
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(3)

        # 输出页面加载时间信息
        print(self.driver.execute_script('return JSON.stringify(performance.timing)'))

    # 修改12306的出发时间
    def test_dateTime(self):
        self.driver.get('https://www.12306.cn/index/')
        js_scrip = "a=document.getElementById('train_date');a.removeAttribute('readonly');a.value='2020-02-03'"
        self.driver.execute_script(js_scrip)
        sleep(10)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
