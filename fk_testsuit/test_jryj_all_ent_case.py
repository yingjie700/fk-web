from numpy.core.tests.test_scalarinherit import D
from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
class Yjjk_num(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.web = webdriver.Chrome()
        self.web.get('http://10.1.1.99:7991/web/login')  # 登录页面
        time.sleep(2)
        self.web.find_element_by_name(name='username').send_keys('yscredit')  # 定位元素  账号密码
        self.web.find_element_by_name(name='password').send_keys('yscredit808')
        self.web.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/button').click()  # 点击登陆
        time.sleep(2)
        self.web.get('http://10.1.1.99:7991/web/riskwarning#/Yjjk')
        time.sleep(4)
        print('开始测试')

    @classmethod
    def tearDownClass(self):
        print('完成测试')
        self.web.quit()
    def numofyjjk(self):
        page_path='//*[@id="app"]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/a'
        c = self.web.find_elements_by_xpath(
            '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/a')  # 翻页控件路径
        end_page_len=len(c)-2

        end_page_path = page_path + '[' + str(end_page_len) + ']'
        end_page_num = self.web.find_element_by_xpath(end_page_path).text
        print(end_page_num)
        end_page_num = int(end_page_num)
        next_button=len(c) - 1
        total = 0 #计数器
        for i in range(1,end_page_num+1):
            fk=self.web.find_elements_by_class_name('color0')#预警
            se=self.web.find_elements_by_class_name('smltit')#自定义
            page_total=(len(fk)+len(se))#单页总和
            total +=page_total
            print(total)
            time.sleep(2)
            self.web.find_element_by_xpath(page_path+'['+str(next_button)+']').click()
            time.sleep(1)
        print(total)
        ture_total=self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[1]/div[2]/div[2]/span')#页面统计数量
        ture_total=int(ture_total.text)
        self.assertEqual(total,ture_total)
    def test_num(self):
        self.numofyjjk()

if __name__ == "__main__":
    unittest.main()