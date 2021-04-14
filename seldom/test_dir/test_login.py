import seldom
from seldom import ChromeConfig


class CnTest(seldom.TestCase):

    def test_case1(self):
        """ Login with right data that login was successful. """
        self.open("http://192.168.129.30:6060")
        self.type(id_="login_username", text="admin")
        self.type(id_="login_password", text="Pwd123456")
        self.click(xpath='//button[@type="submit"]')

        self.assertInUrl("chooseTenant")
        self.assertInTitle("容器云管理平台")
        self.delete_all_cookies()

    def test_case2(self):
        """ Login with wrong data that login was failed. """
        self.open("http://192.168.129.30:6060")
        self.type(id_="login_username", text="admin")
        self.type(id_="login_password", text="Pwd123")
        self.click(xpath='//button[@type="submit"]')

        self.assertInUrl("compass-web")
        self.assertText("用户名或密码错误")
        # self.assertAlertText("用户名或密码错误")
        self.delete_all_cookies()

    def test_case3(self):
        """ Test case Failed. """
        self.open("http://192.168.129.30:6060")
        self.type(id_="login_username", text="admin")
        self.type(id_="login_password", text="Pwd123456")
        self.click(xpath='//button[@type="submit"]')

        self.assertInUrl("compass-web")
        self.assertText("用户名或密码错误")


if __name__ == '__main__':
    # seldom.main(debug=True)
    ChromeConfig.executable_path = "/Users/chenneng/Desktop/UI_auto/lib/chromedriver"
    seldom.main(browser="chrome", debug=True)
