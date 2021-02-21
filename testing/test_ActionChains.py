import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_clicks(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        click_ele = self.driver.find_element(By.XPATH, '/html/body/form/input[3]')
        double_click_ele = self.driver.find_element(By.XPATH, '/html/body/form/input[2]')
        right_click_ele = self.driver.find_element(By.XPATH, '/html/body/form/input[4]')
        actions = ActionChains(self.driver)
        # 单击
        actions.click(click_ele)
        # 双击
        actions.double_click(double_click_ele)
        # 右键点击
        actions.context_click(right_click_ele)
        # 执行
        actions.perform()
        time.sleep(3)

    def test_move_to(self):
        self.driver.get('https://cn.bing.com/')
        elem = self.driver.find_element(By.XPATH, '//*[@id="office"]')
        action = ActionChains(self.driver)
        action.move_to_element(elem)
        action.perform()
        time.sleep(3)

    def test_drag_drop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        source_elem = self.driver.find_element(By.ID, 'dragger')
        target_elem = self.driver.find_element(By.XPATH, '/html/body/div[2]')
        action = ActionChains(self.driver)
        action.drag_and_drop(source_elem, target_elem)
        action.perform()
        time.sleep(3)

    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        elem = self.driver.find_element(By.XPATH, '/html/body/label[1]/input')
        action = ActionChains(self.driver)
        action.click(elem)
        action.send_keys('web').pause(3)
        action.send_keys(Keys.SPACE)
        action.send_keys('test').pause(3)
        action.send_keys(Keys.BACK_SPACE)
        action.perform()
        time.sleep(3)
