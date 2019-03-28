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
        time.sleep(2)
        self.web.find_element_by_name(name='username').send_keys('yscredit')    # 定位元素  账号密码
        self.web.find_element_by_name(name='password').send_keys('yscredit808')
        self.web.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/button').click()   #点击登陆
        time.sleep(2)
        self.web.find_element_by_id('search_input').send_keys('广发证券股份有限公司')      #在搜索框输入测试输入
        self.web.find_element_by_id('search_btn').click()                               #点击搜索
        time.sleep(2)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[1]/div[2]/ul/li[1]/a').click()
        windows = self.web.window_handles
        self.web.switch_to.window(windows[1])
        self.web.maximize_window()
        print('开始测试test_endpage')
        time.sleep(2)
    @classmethod
    def tearDownClass(self):
        print('完成测试test_endpage')
        self.web.quit()

    def endpage(self,path,page_path):   #path=翻页控件路径
                                        #page_path=第一页的列表信息路径
        a = self.web.find_elements_by_xpath(path)
        b = str(len(a) - 2)
        l = path+'['+b+']'
        #print(l) #调试
        first_page=self.web.find_elements_by_xpath(page_path)#获取第一页的列表信息
        for first_page_msg in first_page:
            first_page_msg=first_page_msg.text
            print(first_page_msg)
        print('--------------------------------------------')
        time.sleep(2)
        self.web.find_element_by_xpath(l).click() #跳到尾页
        time.sleep(2)
        end_page=self.web.find_elements_by_xpath(page_path)
        time.sleep(2)
        for end_page_msg in end_page:
            end_page_msg=end_page_msg.text
            print(end_page_msg)
        time.sleep(2)
        try:
            self.assertNotEqual(first_page_msg,end_page_msg)
        except:
            raise

        #成员信息
    def test_endpage1(self):
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div/ul/li[2]/a').click()
        self.endpage('//*[@id="memberTable"]/div/div/a','// *[ @ id = "memberTable"] / table / tr')
        time.sleep(2)

        #预警监控
    def test_endpage3(self):
        self.web.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/ul/li[2]/a').click()#点击风险预警按钮
        time.sleep(5)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[1]'
                                       '/div/div[1]/div/div[2]/div[2]/p[2]').click()#点击今日推送按钮
        time.sleep(3)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[2]/div[1]'
                                       '/div/div[1]/div[1]/div[1]/div/span[3]').click()#点击30天筛选按钮
        time.sleep(4)
        self.endpage('//*[@id="app"]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/a','// *[ @ id = "app"] / div[2] /div[2] / div / div[2] / div[1] / div / div[1] / div[2] / table / tr')
        time.sleep(2)

    def test_endpage2(self):

        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div/ul/li[6]/a').click()
        time.sleep(2)
        self.endpage('//*[@id="Cpws"]/div[12]/div/a','//*[@id="Cpws"]/div[2]/a')

if __name__ == "__main__":
    unittest.main()
