from selenium.webdriver.support.wait import WebDriverWait


class AddressPage:
    def __init__(self, driver):
        self.driver = driver

    def add_stuff(self):
        """
        在通讯录中添加成员
        :return:
        """
        def waite_username(x):
            self.driver.find_elements_by_xpath("//*[@class='qui_btn ww_btn js_add_member']")[1].click()
            elem = self.driver.find_elements_by_xpath("//*[@id='username']")
            return len(elem) > 0

        WebDriverWait(self.driver, 10).until(waite_username)
        # 输入姓名
        self.driver.find_element_by_id("username").send_keys("韩立")
        # 输入账号名
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("hanli")
        # 输入电话号码
        self.driver.find_element_by_id("memberAdd_phone").send_keys("17300000001")
        # 点击保存
        # self.driver.find_element_by_xpath("//*[@class='qui_btn ww_btn js_btn_save']").click()
