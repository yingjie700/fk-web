from pandas._libs import window
from selenium.webdriver.common.action_chains import ActionChains
from numpy.core.tests.test_scalarinherit import D
from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

class Logout_case(unittest.TestCase):
    def setUp(self):
        self.web = webdriver.Chrome()
        self.web.get('http://10.1.1.99:7991/web/login')  # 登录页面
        time.sleep(2)
        self.web.find_element_by_name(name='username').send_keys('yscredit')    # 定位元素  账号密码
        self.web.find_element_by_name(name='password').send_keys('yscredit808')
        self.web.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/button').click()   #点击登陆
        time.sleep(3)
        self.web.maximize_window()
        print('开始测试test_loginout')

    def tearDown(self):
        print('完成测试test_loginout')
        self.web.quit()

    def logout(self):
        self.web.maximize_window()
        username=self.web.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/a')
        time.sleep(2)
        ActionChains(self.web).move_to_element(username).perform()
        time.sleep(3)
        self.web.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div/div/a').click()
        time.sleep(2)

        #登出后在同时打开的另一个页面操作
    def act_in_another_broswer(self,path,url): #path=在另一个页面点击的元素路径
        #url = 'http://10.1.1.99:7991/web/workbench'
        js='window.open(" %s")' % url
        self.web.execute_script(js)  # 调用js打开新窗口
        handles = self.web.window_handles
        #print(handles)
        self.web.switch_to.window(handles[0])
        time.sleep(3)
        self.logout()
        time.sleep(2)
        self.web.switch_to.window(handles[1])
        time.sleep(2)
        self.web.find_element_by_xpath(path).click()
        time.sleep(2)
        try:
            self.assertEqual(self.web.title,'login')
        except:
            raise

        #正常退出操作
    def test_logout0(self):
        self.logout()
        self.assertEqual(self.web.title,'login')

        #登出后在首页点击360搜索按钮
    def test_logout1(self):
        self.act_in_another_broswer('//*[@id="app"]/div[2]/div[2]/ul/li[1]/a','http://10.1.1.99:7991/web/workbench')

        #登出后在预警监控页面点击今日推送
    def test_logout2(self):
        self.act_in_another_broswer('//*[@id="app"]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[2]/p[2]','http://10.1.1.99:7991/web/riskwarning#/')


if __name__ == "__main__":
    unittest.main()
