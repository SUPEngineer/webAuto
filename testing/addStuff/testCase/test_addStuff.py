from testing.addStuff.page.main_page import MainPage


class TestAddStuff:
    def test_add_stuff(self):
        """
        测试添加成员
        1.复用浏览器
        2.进入通讯录
        3.添加成员
        :return:
        """
        mainPage =MainPage()
        mainPage.goto_address_page().add_stuff()
