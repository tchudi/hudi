#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'

import unittest
from selenium import webdriver
from page.logout_page import Logout_Page
from page.login_page import Login_Page



class Logout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.logout=Logout_Page(cls.driver)
        cls.login=Login_Page(cls.driver)
        cls.login.login_action()

    @classmethod
    def tearDownClass(cls):
        cls.logout.close()

    def test_logout(self):
        '''退出'''
        self.logout.logout()
        result=self.logout.sucess_result()
        self.assertTrue(result)

if __name__=='__main__':
    unittest.main()