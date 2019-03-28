from pandas._libs import window
from selenium.webdriver.common.action_chains import ActionChains
from numpy.core.tests.test_scalarinherit import D
from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

class Loginout_case(unittest.TestCase):
    def setUp(self):
        self.web = webdriver.Chrome()
        self.web.get('https://10.1.1.99：7991/web/login')  # 登录页面
        time.sleep(2)
        self.web.find_element_by_name(name='username').send_keys('yscredit')    # 定位元素  账号密码
        self.web.find_element_by_name(name='password').send_keys('yscredit808')
        self.web.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/button').click()   #点击登陆
        time.sleep(2)
        self.web.maximize_window()
        print('开始测试test_endpage')

    def tearDown(self):
        print('完成测试test_endpage')
        #self.web.quit()

    def click_check(self,entname):
        self.web.find_element_by_id('search_input').send_keys(entname)  # 在搜索框输入测试输入
        self.web.find_element_by_id('search_btn').click()  # 点击搜索
        time.sleep(3)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[2]/ul/li[1]').click()#点击第一家企业
        windows = self.web.window_handles
        self.web.switch_to.window(windows[1])
        self.web.maximize_window()
        time.sleep(3)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div/ul/li[4]/a').click()
        a = self.web.find_elements_by_class_name('hrefJump')  # 找到所有能点击跳转的企业
        self.web.find_elements_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div/ul/li[1]/a')
        moduls=self.web.find_elements_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div/ul/li/a')
        for modul in range(1,len(moduls)):
            modul=1
            for b in a:
                try:
                    b.click()
                    time.sleep(2)
                    windows = self.web.window_handles
                    new_windows=len(windows)-1
                    self.web.switch_to.window(windows[new_windows])
                    time.sleep(4)
                    name=self.web.find_element_by_xpath('//*[@id="overview"]/div[1]/div[1]/p[1]').text
                    print(name)
                    time.sleep(2)
                    self.assertEqual(b.text,name)
                    self.web.switch_to.window(windows[1])
                    print(windows[1])
                    time.sleep(3)
                except:
                    self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div/ul/li'+'['+str(modul)+']'+'/a')
                    modul +=1
                    break

    def test_click_check1(self):
        self.click_check('深圳开维教育信息技术股份有限公司')

if __name__ == "__main__":
    unittest.main()