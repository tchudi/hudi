#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'

from selenium import webdriver
from page.login_page import Login_Page
from page.bugsearch_page import Bugsearch_page
import unittest

class Bugsearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.login=Login_Page(cls.driver)
        cls.login.login_action()
        cls.b=Bugsearch_page(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.b.close()

    def test_search(self):
        '''bug搜索'''
        self.b.search()
        result=self.b.sucess_result()
        self.assertTrue(result)

if __name__=="__main__":
    unittest.main()