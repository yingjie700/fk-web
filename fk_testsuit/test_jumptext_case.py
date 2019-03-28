from numpy.core.tests.test_scalarinherit import D
from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

class Jumptext_case(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.web = webdriver.Chrome()
        self.web.get('http://10.1.1.99:7991/web/login')  # 登录页面
        time.sleep(2)
        self.web.find_element_by_name(name='username').send_keys('yscredit')    # 定位元素  账号密码
        self.web.find_element_by_name(name='password').send_keys('yscredit808')
        self.web.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/button').click()   #点击登陆
        self.web.implicitly_wait(2)
        self.web.find_element_by_id('search_input').send_keys('海航集团有限公司')      #在搜索框输入测试输入
        self.web.find_element_by_id('search_btn').click()                               #点击搜索
        time.sleep(2)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[1]/div[2]/ul/li[1]/a').click()#进入第一家企业
        windows = self.web.window_handles
        self.web.switch_to.window(windows[1])
        self.web.maximize_window()
        print('开始测试test_jumptext_case')
        time.sleep(4)

    @classmethod
    def tearDownClass(self):
        print('完成测试test_jumptext_case')
        self.web.quit()

    def jumptext_change(self, path,text_path,input_text,value):       #断言操作后变的情况
        a=self.web.find_elements_by_xpath(path)
        first_page=self.web.find_elements_by_xpath(text_path)
        for first_page_msg in first_page:
            first_page_msg=first_page_msg.text
            #print(first_page_msg)#调试
        l=len(a)-4 #总页数
        int(l)
        go=str(len(a))
        go_path=path+'['+go+']'           #找到go按钮所在的位置
        self.web.find_element_by_xpath(input_text).send_keys(value)
        time.sleep(2)
        self.web.find_element_by_xpath(go_path).click()
        time.sleep(2)
        second_page=self.web.find_elements_by_xpath(text_path)
        for second_pagemsg in second_page:
            second_pagemsg=second_pagemsg.text
           #print(second_pagemsg)#调试
        try:
            self.assertNotEqual(first_page_msg,second_pagemsg)
        except:
            raise
        self.web.refresh()
        time.sleep(5)

    def jumptext_notchange(self, path,text_path,input_text,value):       #断言操作后不变的情况
                                                                #path=第一页按钮的路径
                                                                #text_path=文本内容所在路径
                                                                #value=输入的值
        a=self.web.find_elements_by_xpath(path)
        first_page=self.web.find_elements_by_xpath(text_path)
        for first_page_msg in first_page:
            first_page_msg=first_page_msg.text
            #print(first_page_msg)#调试
        l=len(a)-4 #总页数
        int(l)
        go=str(len(a))
        go_path=path+'['+go+']'
        self.web.find_element_by_xpath(input_text).send_keys(value)
        time.sleep(2)
        self.web.find_element_by_xpath(go_path).click()
        time.sleep(2)
        second_page=self.web.find_elements_by_xpath(text_path)
        for second_pagemsg in second_page:
            second_pagemsg=second_pagemsg.text
           #print(second_pagemsg)#调试
        try:
            self.assertEqual(first_page_msg,second_pagemsg)
        except:
            raise
        self.web.refresh()
        time.sleep(5)

    def test_jumtext1(self):
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div/ul/li[6]/a').click()
        time.sleep(2)
        self.jumptext_change('//*[@id="Ktgg"]/div[11]/div/a','//*[@id="Ktgg"]/div[1]/div','//*[@id="Ktgg"]/div[11]/div/input','2')

    def test_jumtext2(self):
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div/ul/li[6]/a').click()
        time.sleep(2)
        self.jumptext_notchange('//*[@id="Ktgg"]/div[11]/div/a','//*[@id="Ktgg"]/div[1]/div','//*[@id="Ktgg"]/div[11]/div/input','1')

if __name__ == "__main__":
    unittest.main()
