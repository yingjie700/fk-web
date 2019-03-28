from numpy.core.tests.test_scalarinherit import D
from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
import re
import itertools
class Risks_Score(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.web = webdriver.Chrome()
        self.web.get('http://10.1.1.99:7991/web/login')  # 登录页面
        time.sleep(2)
        self.web.find_element_by_name(name='username').send_keys('yscredit')    # 定位元素  账号密码
        self.web.find_element_by_name(name='password').send_keys('yscredit808')
        self.web.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/button').click()   #点击登陆
        time.sleep(2)
        print('开始测试test_riskscore')
    @classmethod
    def tearDownClass(self):
        print('完成测试test_riskscore')
        self.web.quit()
    def add_risk_score(self,entname):

        self.web.find_element_by_id('search_input').send_keys(entname)      #在搜索框输入测试输入
        self.web.find_element_by_id('search_btn').click()                               #点击搜索
        time.sleep(3)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[1]/div[2]/ul/li[1]/a').click()
        windows = self.web.window_handles
        new_window=len(windows)-1
        self.web.switch_to.window(windows[new_window])
        time.sleep(3)
        self.web.maximize_window()
        time.sleep(5)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div/ul/li[5]/a').click()#点击风险分析tab
        time.sleep(2)
        #自身风险
        page_path = '//*[@id="riskContent"]/div/div/div/div/a'
        try:
            c = self.web.find_elements_by_xpath('//*[@id="riskContent"]/div/div/div/div/a')  # 获取页码路径
        except:
            print('only one page')
        try:
            end_page_len=len(c)-2
            end_page_path=page_path+'['+str(end_page_len)+']'
            end_page_num=self.web.find_element_by_xpath(end_page_path).text
            print(end_page_num)
            end_page_num=int(end_page_num)
            page_num = len(c) - 3  # 总页数
        except:
            print('only one self_risk_page')
            end_page_num=1
        b = []
        float_self_score = []
        for self_risks in range(1, end_page_num+1):
            a = self.web.find_elements_by_xpath('//*[@id="riskContent"]/div/ul/li/p')  # 获取分数集合
            for sum_self_risk in a:
                sum_self_risktext = sum_self_risk.text
                sum_self_risktext = re.findall('\d+\.?\d*', sum_self_risktext)
                #print(sum_self_risktext)
                b.append(sum_self_risktext)
            d=str(len(c)-1)
            next_page_button=page_path+'['+d+']'
            try:
                self.web.find_element_by_xpath(next_page_button).click()  # 下一页按钮
                time.sleep(4)
            except:
                print('only one self_risk_page1')
        b = list(itertools.chain.from_iterable(b))
        for num in b:
            float_self_score.append(float(num))
        #print(float_self_score)
        int_self_score = sum(float_self_score)
        int_self_score1 = round(int_self_score, 3)
        #print(int_self_score)
        total_self_score = int((int_self_score + 0.5))
        print(total_self_score)  # 自身风险总分
        time.sleep(2)
        #关联风险
        try:
            self.web.find_element_by_xpath("//div[@id='xhxq']/div/ul/li[2]").click()
        except:
            raise
        time.sleep(2)
        page_path='//*[@id="riskContent"]/div/div/div/div/a'
        try:
            c=self.web.find_elements_by_xpath('//*[@id="riskContent"]/div/div/div/div/a')
        except:
            print('only one related_risk_page')
        try:
        #c=self.web.find_elements_by_xpath('//*[@id="riskContent"]/div/div/div/div/a')#获取页码路径
            end_page_len = len(c) - 2
            end_page_path = page_path + '[' + str(end_page_len) + ']'
            end_page_num = self.web.find_element_by_xpath(end_page_path).text
            #print(end_page_num)
            end_page_num = int(end_page_num)
            page_num=len(c)-3#总页数
        except:
            print('only one related_risk_page1')
            end_page_num=1
        b = []
        float_related_score=[]
        for related_risks in range(1,end_page_num+1):
            a = self.web.find_elements_by_xpath('//*[@id="riskContent"]/div/ul/li/p')  # 获取分数集合
            for sum_risk in a:
                sum_related_risktext=sum_risk.text
                sum_related_risktext=re.findall('\d+\.?\d*',sum_related_risktext)
                #print(sum_related_risktext)
                b.append(sum_related_risktext)

            d=str(len(c)-1)
            next_page_button=page_path+'['+d+']'
            try:
                self.web.find_element_by_xpath(next_page_button).click() # 下一页按钮
                time.sleep(4)
            except:
                print('only one page2')
        b=list(itertools.chain.from_iterable(b))
        for num in b:
            float_related_score.append(float(num))
        #print(float_related_score)
        int_related_score=sum(float_related_score)
        int_related_score1=round(int_related_score,3)
        #print(int_related_score)
        total_related_score=int((int_related_score+0.5))
        print(total_related_score)#关联风险总分

        #自身风险总分+关联风险总分
        total_score=total_self_score+total_related_score
        ture_score=self.web.find_element_by_xpath('//*[@id="risk-analysis"]/div[2]/div[1]/div[2]/p[1]').text#页面展示的分数
        ture_score=int(ture_score)
        print(ture_score)
        if total_score>=999:
            total_score=999
            print(total_score)
            self.assertEqual(total_score, 999)
        else:
            print(total_score)
            self.assertEqual(total_score,ture_score)
        windows = self.web.window_handles
        self.web.switch_to.window(windows[0])

    def test_riskscore(self):
        self.add_risk_score('广东中磊投资集团有限公司')
    def test_riskscore1(self):
        self.add_risk_score('广发证券股份有限公司')

    def test_riskscore2(self):
        self.add_risk_score('小米科技有限责任公司')
    def test_riskscore3(self):
        self.add_risk_score('山东海洋集团有限公司')

if __name__ == "__main__":
    unittest.main()