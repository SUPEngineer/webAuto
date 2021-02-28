from selenium import webdriver
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait


class TestPageObjec():
    def setup(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_add_stuff(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_xpath("//*[@id='menu_contacts']/span").click()

        def waite_username(x):
            self.driver.find_elements_by_xpath("//*[@class='qui_btn ww_btn js_add_member']")[1].click()
            elem = self.driver.find_elements_by_xpath("//*[@id='username']")
            return len(elem) > 0
        WebDriverWait(self.driver, 10).until(waite_username)
        self.driver.find_element_by_id("username").send_keys("韩立")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("hanli")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("17300000001")
        self.driver.find_element_by_xpath("//*[@class='qui_btn ww_btn js_btn_save']").click()

