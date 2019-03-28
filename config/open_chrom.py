import time
from selenium import webdriver
from config.config_path import login_url
import unittest

class Jump_page_case():
    def open_and_login(self):
        print('开始测试test_jump_page')
        self.web = webdriver.Chrome()
        self.web.get('http://10.1.1.99:7991/web/login')  # 登录页面
        time.sleep(2)
        self.web.find_element_by_name(name='username').send_keys('yscredit')    # 定位元素  账号密码
        self.web.find_element_by_name(name='password').send_keys('yscredit808')
        self.web.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/button').click()   #点击登陆
        time.sleep(2)
        self.web.find_element_by_id('search_input').send_keys('海南航空控股股份有限公司')      #在搜索框输入测试输入
        self.web.find_element_by_id('search_btn').click()                               #点击搜索
        time.sleep(2)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[2]/ul/li[1]').click() #点击第一家企业
        windows = self.web.window_handles
        self.web.switch_to.window(windows[1]) #转换窗口
        self.web.maximize_window()
        time.sleep(5)

if __name__ == "__main__":
    unittest.main()
