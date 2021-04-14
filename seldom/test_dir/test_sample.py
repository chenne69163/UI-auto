import seldom
from seldom import ChromeConfig


class YouTest(seldom.TestCase):

    def test_case1(self):
        """a simple test case """
        self.open("https://www.baidu.com")
        self.type(id_="kw", text="seldom")
        self.click(css="#su")
        self.assertInTitle("seldom")

    def test_case2(self):
        """a simple test case """
        self.open("https://www.baidu.com")
        self.type(id_="kw", text="字节跳动")
        self.click(css="#su")
        self.assertInTitle("字节")


if __name__ == '__main__':
    # seldom.main(debug=True)
    ChromeConfig.executable_path = "/Users/chenneng/Desktop/UI_auto/lib/chromedriver"
    seldom.main(browser="chrome", debug=True)
