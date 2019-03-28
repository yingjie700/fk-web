import pymysql as pymysql
from selenium import webdriver
import unittest
import time
class MySql(unittest.TestCase):
    def setUp(self):
        print('1')
    def tearDownClass(self):
        print('2')
    def mysql(self):
            # 连接数据库
            hostvalue = '10.1.1.40'
            uservalue = 'gsuser'
            passwordvalue = 'tHguyhQ3mAhsT3X0'
            dbvalue = 'gs'
            portvalue = 3306
            connection = pymysql.connect(host=hostvalue, user=uservalue, password=passwordvalue, db=dbvalue,
                                port=portvalue, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            # 通过cursor创建游标
            cursor = connection.cursor()
            # 创建sql 语句，并执行
            sqlvalue = "SELECT entname , FROM `gs`.`enterprisebaseinfocollect` WHERE `id` = '2'"
            cursor.execute(sqlvalue)
            result = cursor.fetchone()  # 查询数据库单条数据
            #result = cursor.fetchall() #查询数据库多条数据
            # 提交sql
            connection.commit()
            return result

    def test_check_mysql1(self):
        self.mysql()

if __name__ == "__main__":
    unittest.main()
