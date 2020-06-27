#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'

from selenium import webdriver
from page.login_page import Login_Page
from page.addbug_page import Addbug_page
import unittest


class Add_bug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.l=Login_Page(cls.driver)
        cls.l.login_action()
        cls.a=Addbug_page(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.a.close()

    def test_01(self):
        '''添加用例'''

        self.a.add_bug()
        result=self.a.sucess_result()
        self.assertTrue(result)


if __name__=="__main__":
    unittest.main()