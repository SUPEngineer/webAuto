# @Time : 2021/2/24 15:02 
# @Author : qiulingfeng
# @File : test_frame.py
from selenium.webdriver.common.by import By

from testing.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame('iframeResult')
        print(self.driver.find_element(By.ID, 'draggable').text)
        # 返回原页面中
        self.driver.switch_to.parent_frame()
        # 或者使用下面的方法回到原来默认的页面中，效果与self.driver.switch_to.parent_frame()相同
        # self.driver.switch_to.default_content()
        print(self.driver.find_element(By.ID, 'submitBTN').text)
