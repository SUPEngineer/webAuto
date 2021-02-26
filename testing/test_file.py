# @Time : 2021/2/24 19:46 
# @Author : qiulingfeng
# @File : test_file.py
from time import sleep

from selenium.webdriver.common.by import By

from testing.base import Base


class TestFile(Base):
    def test_file(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.XPATH, "//*[@id='sttb']/img[1]").click()
        self.driver.find_element(By.ID, 'uploadImg').send_keys('C:/Users/qiulingfeng01/Desktop/测试上传文档/测试图片')
        sleep(3)
