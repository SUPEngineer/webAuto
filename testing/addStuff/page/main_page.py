from selenium import webdriver

from testing.addStuff.page.address_page import AddressPage


class MainPage:
    def __init__(self):
        # 设置option参数，打开调试窗口
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        # 复用浏览器
        self.driver = webdriver.Chrome(options=chrome_arg)

    def goto_address_page(self):
        """
        点击进入通讯录
        :return: AddressPage
        """
        self.driver.find_element_by_xpath("//*[@id='menu_contacts']/span").click()
        return AddressPage(self.driver)
