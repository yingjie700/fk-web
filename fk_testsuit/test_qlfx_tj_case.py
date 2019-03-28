from selenium import webdriver
import unittest
import time

class Qlfx_tj(unittest.TestCase):
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
    def qlfx(self,entname):
        self.web.find_element_by_id('search_input').send_keys(entname)  # 在搜索框输入测试输入
        self.web.find_element_by_id('search_btn').click()  # 点击搜索
        time.sleep(4)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[1]/div[2]/ul/li[1]/a').click()
        time.sleep(2)
        windows = self.web.window_handles
        new_window = len(windows) - 1
        self.web.switch_to.window(windows[new_window])
        time.sleep(7)
        self.web.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div/ul/li[6]/a').click()#全量风险
        Sffx_path='//*[@id="total_risk"]/div[1]/div[1]/div[1]/div[1]/div/p'
        Sffx=self.web.find_elements_by_xpath(Sffx_path+'/span')#司法风险
        #//*[@id="total_risk"]/div[1]/div[1]/div[1]/div[1]/div/p[1]/span                        #数字
        Jyfx=self.web.find_elements_by_xpath('//*[@id="total_risk"]/div[1]/div[1]/div[1]/div[2]/div/p')#经营风险
        Swfx=self.web.find_elements_by_xpath('//*[@id="total_risk"]/div[1]/div[1]/div[1]/div[3]/div/p')  # 税务风险
        Xzcf=self.web.find_elements_by_xpath('//*[@id="total_risk"]/div[1]/div[1]/div[1]/div[4]/div/p')  # 行政处罚

    #司法风险数据统计对比
        sffx_lable_Path = '//*[@id="judicial_risk"]/div[1]/p'
        sffx_lable_Num=self.web.find_elements_by_xpath(sffx_lable_Path+'/i')
        sffx_list=[]
        sffx_lable_num_list=[]
        for sffx_lable_num in sffx_lable_Num:           #下面标签的数字
            sffx_lable_num_list.append(sffx_lable_num.text)
        print(sffx_lable_num_list)
        for sffx in Sffx:               #上面统计的数字
            sffx_list.append(sffx.text)
        print(sffx_list)
        assert sffx_lable_num_list==sffx_list

        for a in range(0,5):
            if a==0:#开庭公告
                self.web.find_element_by_xpath('//*[@id="judicial_risk"]/div[1]/p[1]').click()
                time.sleep(2)
                if sffx_list[0]!=0:
                    try:
                        Ktgg_page_path='//*[@id="Ktgg"]/div[11]/div/a'
                        Ktgg_page_path_len=self.web.find_elements_by_xpath(Ktgg_page_path)
                        self.web.find_element_by_xpath(Ktgg_page_path+'['+str(len(Ktgg_page_path_len)-2)+']').click()#翻到最后一页
                        time.sleep(4)
                        last_page_num_path='//*[@id="Ktgg"]/div'            #[5]/i'
                        last_page_num_path_len=self.web.find_elements_by_xpath(last_page_num_path)
                        last_page_num=self.web.find_element_by_xpath(last_page_num_path+'['+str(len(last_page_num_path_len)-1)+']/i')#找到最后一页最后一页序号
                        print(len(last_page_num_path_len))

                        time.sleep(3)
                        assert sffx_list[0]==last_page_num.text#与上面统计的对比
                        print(last_page_num.text)

                    except:
                        print('only one page')
                        last_page_num_path = '//*[@id="Ktgg"]/div'  #[5]/i'
                        last_page_num_path_len = self.web.find_elements_by_xpath(last_page_num_path)
                        last_page_num = self.web.find_element_by_xpath(last_page_num_path + '[' + str(len(last_page_num_path_len)-1) + ']/i')  # 找到最后一条序号

                        print(last_page_num)
                        time.sleep(3)
                        assert sffx_list[0] == last_page_num.text#与上面统计的对比
                        print(last_page_num.text)
                else:
                    print('该标签数量为0')
            else:
                print('0')
            if a==1:#裁判文书
                if sffx_list[0] != 0:
                    self.web.find_element_by_xpath('//*[@id="judicial_risk"]/div[1]/p[2]').click()
                    time.sleep(2)
                    try:
                        Cpws_page_path='//*[@id="Cpws"]/div[8]/div/a'
                        Cpws_page_path_len=self.web.find_elements_by_xpath(Cpws_page_path)
                        print('page')
                        time.sleep(2)
                        self.web.find_element_by_xpath('//*[@id="Cpws"]/div[8]/div/a[7]').click()
                        #self.web.find_element_by_xpath(Cpws_page_path+'['+str(len(Cpws_page_path_len)-2)+']').click()#翻到最后一页
                        time.sleep(4)
                        last_page_num_path='//*[@id="Cpws"]/div'    #[7]/i'
                        last_page_num_path_len=self.web.find_elements_by_xpath(last_page_num_path)
                        last_page_num=self.web.find_element_by_xpath(last_page_num_path+'['+str(len(last_page_num_path_len)-1)+']/i')#找到最后一页最后一页序号
                        time.sleep(3)
                        print(last_page_num.text)
                        assert sffx_list[1]==last_page_num.text#与上面统计的对比


                    except:
                        print('only one page')
                        last_page_num_path = '//*[@id="Cpws"]/div'#[2]/i'
                        last_page_num_path_len = self.web.find_elements_by_xpath(last_page_num_path)
                        last_page_num = self.web.find_element_by_xpath(last_page_num_path + '[' + str(len(last_page_num_path_len)-1) + ']/i')  # 找到最后一条序号
                        time.sleep(3)

                        assert sffx_list[1] == last_page_num.text#与上面统计的对比
                else:
                    print('该标签数量为0')
            else:
                print('该标签数量为0')

            if a == 2:
                if sffx_list[2] != 0:
                    try:
                        Bzx_page_path='//*[@id="Bzxr"]/div[11]/div/a'
                        Bzx_page_path_len=self.web.find_elements_by_xpath(Bzx_page_path)
                        self.web.find_element_by_xpath(Bzx_page_path+'['+str((Bzx_page_path_len)-2)+']').click()#翻到最后一页
                        time.sleep(3)
                        last_page_num_path='//*[@id="Bzxr"]/div'            #[10]/i'
                        last_page_num_path_len=self.web.find_elements_by_xpath(last_page_num_path)
                        last_page_num=self.web.find_element_by_xpath(last_page_num_path+'['+str(len(last_page_num_path_len)-1)+']/i')
                        time.sleep(3)
                        assert sffx_list[2]==last_page_num.text
                        print(last_page_num)
                    except:
                        print('only one page')
                        last_page_num_path='//*[@id="Bzxr"]/div'
                        last_page_num_path_len = self.web.find_elements_by_xpath(last_page_num_path)
                        last_page_num = self.web.find_element_by_xpath(last_page_num_path + '[' + str(len(last_page_num_path_len)-1) + ']/i')  # 找到最后一条序号
                        time.sleep(3)
                        assert sffx_list[2] == last_page_num.text  # 与上面统计的对比
                else:
                    print('该标签数量为0')
            else:
                print('该标签数量为0')




    def test_qlfx_tj1(self):
        self.qlfx('乐视云计算有限公司')

if __name__ == "__main__":
    unittest.main()



