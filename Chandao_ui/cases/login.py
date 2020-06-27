#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'

from page.login_page import Login_Page
from selenium import webdriver
import unittest
import time

class Login(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.l=Login_Page(cls.driver)
        cls.l.openbrowser()

    @classmethod
    def tearDownClass(cls):
        cls.l.close()

    # def setUp(self):
    #     self.driver=webdriver.Chrome()
    #     self.l=Login_Page(self.driver)
    #     self.l.openbrowser()
    #
    # def tearDown(self):
    #     self.l.close()

    def test_02(self):
        '''正常登录'''
        time.sleep(3)
        self.l.alert_accept()
        self.l.login()
        result=self.l.sucess_result('胡迪')
        self.assertTrue(result)

    def test_01(self):
        '''账号错误'''
        self.l.login('hudiii','Hd123456')
        result=self.l.fail_result()
        self.assertTrue(result)

if __name__=="__main__":
    unittest.main()