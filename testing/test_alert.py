# @Time : 2021/2/24 20:10 
# @Author : qiulingfeng
# @File : test_alert.py
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from testing.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame('iframeResult')
        drag = self.driver.find_element_by_id('draggable')
        drop = self.driver.find_element_by_id('droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop)
        action.perform()
        # 切换到alert，点击确认
        self.driver.switch_to.alert.accept()
        # 返回到原来的页面
        self.driver.switch_to.default_content()
        # 点击运行
        self.driver.find_element_by_id('submitBTN').click()
        sleep(3)

