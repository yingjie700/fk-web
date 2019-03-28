from numpy.core.tests.test_scalarinherit import D
from selenium import webdriver
import unittest
import time


class Login_case(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('开始测试test_login')
        self.web = webdriver.Chrome()
        self.web.get('http://10.1.1.99:7991/web/login')  # 登录页面
        self.web.maximize_window()
        time.sleep(2)

    @classmethod
    def tearDownClass(self):
        print('完成测试test_login')
        self.web.quit()
        # 定义登录方法 主体

    def login(self, username, password,title):      #username=用户名
                                                     #password=密码
                                                    #title=预期页面title
        self.web.find_element_by_name(name='username').send_keys(username)#定位元素账号密码
        self.web.find_element_by_name(name='password').send_keys(password)
        self.web.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/button').click()#点击登陆
        time.sleep(2)
        pagetitle = self.web.title
        try:
            self.assertEqual(title,pagetitle)                  #这里使用判断页面title是否是预期结果进行判断
        except Exception:
            raise
            self.web.get_screenshot_as_file("D:\\1\\1.png")     #截图
        self.web.refresh()
         # 用户名正确、密码不正确
    def test_login_pwd_error(self):
        self.login('yscredit', '1','login')  # 正确用户名，错误密码
        time.sleep(2)

        # 用户名正确、密码为空
    def test_login_pwd_null(self):
        self.login('13000000000', '','login')  # 密码为空
        time.sleep(2)

        # 用户名错误、密码正确
    def test_login_user_error(self):
        self.login('1300', 'yscredit808','login')  # 密码正确
        time.sleep(3)

        # 用户名为空、密码正确
    def test_login_user_null(self):
        self.login('', 'yscredit808','login')  # 用户名为空，密码正确
        time.sleep(3)

        # 正确用户名和密码
    def test_loginz_success(self):
        self.login('yscredit', 'yscredit808','工作台')
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()
