
from selenium import webdriver
import unittest
import time


class Total_invest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.web=webdriver.Chrome()
        self.web.get('http://10.1.1.99:7991/web/login')
        time.sleep(2)
        self.web.find_element_by_name(name='username').send_keys('yscredit')  # 定位元素  账号密码
        self.web.find_element_by_name(name='password').send_keys('yscredit808')
        self.web.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/button').click()  # 点击登陆
        time.sleep(2)
        print('开始测试test_total_invest')
    @classmethod
    def tearDownClass(self):
        self.web.quit()
        print('完成测试test_total_invest')
    def add_invest(self,entname):
        self.web.find_element_by_id('search_input').send_keys(entname)  # 在搜索框输入测试输入
        self.web.find_element_by_id('search_btn').click()  # 点击搜索
        time.sleep(4)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[1]/div[2]/ul/li[1]/a').click()
        time.sleep(2)
        windows = self.web.window_handles
        new_window = len(windows) - 1
        self.web.switch_to.window(windows[new_window])
        time.sleep(3)
        #self.web.maximize_window()
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div/ul/li[4]/a').click()
        time.sleep(3)
        ture_total=self.web.find_element_by_xpath('//*[@id="tzgmfx"]/div[2]/div[2]/div[1]/div[1]/div[1]/p').text
        ture_total_num=ture_total.replace('万元','')
        ture_total_num=float(ture_total_num)
        #try:
        x = []
        print(x)
        page_path='//*[@id="investmentTable"]/div/div/a'
        page_path1=self.web.find_elements_by_xpath('//*[@id="investmentTable"]/div/div/a')#翻页控件
        page=len(page_path1)-2
        print(page)
        next_page_button_path=len(page_path1)-1
        next_page_button=page_path+'['+str(next_page_button_path)+']'
        time.sleep(2)
        for next_page in range(1,page):
            a = self.web.find_elements_by_xpath('//*[@id="investmentTable"]/table/tr/td[3]')  # 找到投资金额一列
            for i in a:
                print(i.text)
                b = i.text.replace('万', '')
                c = b.replace(' 人民币', '')
                w = c.replace('--  ','0')
                q = float(w)
                x.append(q)
            try:
                self.web.find_element_by_xpath(next_page_button).click()
                time.sleep(2)
            except:
                print('its last page')
            print(sum(x))
            print(type(ture_total_num))
            self.assertEqual(sum(x),ture_total_num)

    def test_invest1(self):
        self.add_invest('山东海洋集团有限公司')

    def test_invest2(self):
        self.add_invest('杭州有好数据科技有限公司')

if __name__ == "__main__":
    unittest.main()