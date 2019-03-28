from numpy.core.tests.test_scalarinherit import D
from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
class Search_case(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.web = webdriver.Chrome()
        self.web.get('http://10.1.1.99:7991/web/login')  # 登录页面
        #self.web.maximize_window()#窗口最大化
        time.sleep(2)
        self.web.find_element_by_name(name='username').send_keys('yscredit')    # 定位元素  账号密码
        self.web.find_element_by_name(name='password').send_keys('yscredit808')
        self.web.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/button').click()   #点击登陆
        print('开始测试test_sort')
        time.sleep(2)
    @classmethod
    def tearDownClass(self):
        print('完成测试test_sort')
        self.web.quit()
    def dwtzsort(self,entname):
        self.web.find_element_by_id('search_input').send_keys(entname)  # 在搜索框输入测试输入
        self.web.find_element_by_id('search_btn').click()  # 点击搜索
        time.sleep(2)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[1]/div[2]/ul/li[1]/a').click()
        windows = self.web.window_handles
        new_window = len(windows) - 1
        self.web.switch_to.window(windows[new_window])

        time.sleep(4)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div/ul/li[4]/a').click()
        a = self.web.find_elements_by_xpath('//*[@id="investmentTable"]/table/tr/td[4]')
        b = []
        for i in a:
            if i.text == '--':
                b.append(float(0))
            else:
                i = ''.join(i.text.split('%'))
                floati = float(i)
                b.append(floati)
        print(b)
        after = sorted(b, reverse=True)
        print(after)
        self.assertListEqual(after, b)
    def gdbjsort(self,entname):
        self.web.find_element_by_id('search_input').send_keys(entname)  # 在搜索框输入测试输入
        self.web.find_element_by_id('search_btn').click()  # 点击搜索
        time.sleep(2)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[1]/div[2]/ul/li[1]/a').click()
        windows = self.web.window_handles
        new_window = len(windows) - 1
        self.web.switch_to.window(windows[new_window])
        time.sleep(4)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div/ul/li[3]/a').click()
        a = self.web.find_elements_by_xpath('//*[@id="shareholderTable"]/table/tr/td[4]')
        b = []
        for i in a:
            if i.text == '--':
                b.append(float(0))
            else:
                i = ''.join(i.text.split('%'))
                floati = float(i)
                b.append(floati)
        print(b)
        after = sorted(b, reverse=True)
        print(after)
        self.assertListEqual(after, b)
    def bgfxsort(self,entname):
        self.web.find_element_by_id('search_input').send_keys(entname)  # 在搜索框输入测试输入
        self.web.find_element_by_id('search_btn').click()  # 点击搜索
        time.sleep(2)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[1]/div[2]/ul/li[1]/a').click()
        windows = self.web.window_handles
        new_window=len(windows)-1
        self.web.switch_to.window(windows[new_window])
        time.sleep(4)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div/ul/li[7]/a').click()
        a=self.web.find_elements_by_xpath('//*[@id="changeTable"]/table/tr/td[5]')
        b=[]
        for i in a :
            i = ''.join(i.text.split('-'))
            #print(i)
            inti=int(i)
            b.append(inti)
        print(b)
        after=sorted(b,reverse=True)
        print(after)
        self.assertListEqual(after,b)
    def gqczsort(self,entname):
        self.web.find_element_by_id('search_input').send_keys(entname)  # 在搜索框输入测试输入
        self.web.find_element_by_id('search_btn').click()  # 点击搜索
        time.sleep(2)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[1]/div[2]/ul/li[1]/a').click()
        windows = self.web.window_handles
        new_window = len(windows) - 1
        self.web.switch_to.window(windows[new_window])
        time.sleep(5)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div/ul/li[9]/a').click()

        time.sleep(3)
        a = self.web.find_elements_by_xpath('//*[@id="gqcz"]/div/table/tr/td[8]')
        b = []
        for i in a:
            if i.text == '--':
                b.append(0)
            else:
                i = ''.join(i.text.split('-'))
                inti = int(i)
                b.append(inti)
        print(b)
        after = sorted(b, reverse=True)
        print(after)
        self.assertListEqual(after, b)
        time.sleep(2)

    def test_sort1(self):
        self.bgfxsort('周大生珠宝股份有限公司')
    def test_sort2(self):
        self.gqczsort('广发证券股份有限公司')
    def test_sort3(self):
        self.gdbjsort('上海重阳投资管理股份有限公司')
    def test_sort4(self):
        self.gdbjsort('广发证券股份有限公司')
    def test_sort5(self):
        self.dwtzsort('广发证券股份有限公司')

if __name__ == "__main__":
    unittest.main()
