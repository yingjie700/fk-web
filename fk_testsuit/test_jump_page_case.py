from numpy.core.tests.test_scalarinherit import D
from selenium import webdriver
import unittest
import time
import cookie_login

class Jump_page_case(unittest.TestCase):
    def setUp(self):
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
        time.sleep(3)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[1]/div[2]/ul/li[1]/a').click() #点击第一家企业
        windows = self.web.window_handles
        self.web.switch_to.window(windows[1]) #转换窗口
        self.web.maximize_window()
        time.sleep(5)

    def tearDown(self):
        time.sleep(5)
        print('完成测试test_jump_page')
        self.web.quit()

    def jump_page(self, path,page_path):#path=翻页控件路径
                                        #页面文本内容路径
        try:
            a = self.web.find_elements_by_xpath(path)
            for x in range(2,len(a)-3,2):#rang为总页数范围
                first_button = path + '[' + str(x) + ']'#第一页x为2
                self.web.find_element_by_xpath(first_button).click()#点击第一页
                first_page=self.web.find_elements_by_xpath(page_path)#找到第一页内容
                first_page_list=[]
                for first_page_msg in first_page:
                    first_page_msg=first_page_msg.text
                    first_page_list.append(first_page_msg)
                    print(first_page_msg)#调试
                print('-----------------------------------------------')
                x +=2
                second_page=path+'['+str(x)+']'
                time.sleep(3)
                self.web.find_element_by_xpath(second_page).click()#点击第n+1页
                time.sleep(3)
                second_page=self.web.find_elements_by_xpath(page_path)#找到第n+1页内容
                time.sleep(2)
                second_page_list=[]
                for second_page_msg in second_page:
                    second_page_msg=second_page_msg.text
                    second_page_list.append(second_page_msg)
                    print(second_page_msg)#调试
                print('-------------------------------------------------')
                self.assertNotEqual(first_page_list,second_page_list)#判断第n页与n+2页内容是否相同                   (报错)
        #// *[ @ id = "publicopinion-analysis"] / div[1] / div[4] / div[2] / div / div / a[2]    第一页
        #// *[ @ id = "publicopinion-analysis"] / div[1] / div[4] / div[2] / div / div / a[4]    第三页
        # print(l) #调试                                                                     4-9-13
                                                                                              #1页-8页-大于8页

        except:
            raise


    def test_jump_page1(self):
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div/ul/li[11]/a').click()
        time.sleep(5)
        self.jump_page('//*[@id="publicopinion-analysis"]/div[1]/div[4]/div[2]/div/div/a',
                                       '//*[@id="publicopinion-analysis"]/div[1]/div[4]/div[2]/ul/li')
        time.sleep(2)

    def test_jump_page2(self):
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div/ul/li[7]/a').click()
        self.jump_page('//*[@id="changeTable"]/div/div/a[1]','//*[@id="changeTable"]/table/tr[2]')


if __name__ == "__main__":
    unittest.main()
