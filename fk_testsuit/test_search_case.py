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
        #            #最大化页面
        time.sleep(2)
        self.web.find_element_by_name(name='username').send_keys('yscredit')    # 定位元素  账号密码
        self.web.find_element_by_name(name='password').send_keys('yscredit808')
        self.web.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/button').click()   #点击登陆
        print('开始测试test_search')
        time.sleep(2)

    @classmethod
    def tearDownClass(self):
        print('完成测试test_login')
        self.web.quit()

        #搜索步骤加逻辑判断
    def search(self, entname, full_entname):#entname=搜索的企业名
                                            # full_name=预期结果
        self.web.find_element_by_id('search_input').send_keys(entname)      #在搜索框输入测试输入
        self.web.find_element_by_id('search_btn').click()                   #点击搜索
        time.sleep(3)
        a=self.web.find_elements_by_xpath('//*[@id="app"]/div[2]/div[2]/div[2]/ul/li/a/div[1]/span')    #获取列表内容
        if len(a)!=0:                                  #搜索不为空
            try:
                for i in a:
                    if i.text == full_entname:       #在搜素结果列表中循环匹配预期结果
                        break                        #跳出循环 i=full_entname
                    else:
                        i=''

        #print(i.text)        #调试
        #print('已完成搜索')  #调试
                try:
                    i.click()                       #点击匹配到的企业名
                    windows = self.web.window_handles
                    time.sleep(2)
                    print(windows)
                    x=len(windows)-1
                    #if windows<3:
                    self.web.switch_to.window(windows[x])  #转换窗口
                    #else:
                       # self.web.switch_to.window(windows[1])
                    time.sleep(4)
                    ture_name = self.web.find_element_by_xpath('//*[@id="overview"]/div[1]/div[1]/p[1]')   #找到真实企业名
                    ture_name=ture_name.text
                    time.sleep(2)
                    try:
                        self.assertEqual(full_entname,ture_name)    #断言预期结果
                        print(ture_name)
                    except Exception as e:
                        raise                                       #真实企业名与预期不匹配抛出异常
                except NoSuchElementException:
                    raise                                           #列表中没有预期企业抛出异常
            except NoSuchElementException:
                raise                                               #错误
        else:                                                       #搜索为空
            print('no such ent')
        windows = self.web.window_handles
        self.web.switch_to.window(windows[0])
        # 匹配企业全称
    def test_search0(self):
        self.search('周大生珠宝股份有限公司', '周大生珠宝股份有限公司')
        time.sleep(2)

        # 匹配企业全称+数字
    def test_search1(self):
        self.search('周大生珠宝股份有限公司123123', '')
        time.sleep(2)

        # 匹配企业部分名称
    def test_search2(self):
        self.search('周大生', '九江周大生实业有限公司')
        time.sleep(2)
    def test_search3(self):
        self.search('', '')
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()
