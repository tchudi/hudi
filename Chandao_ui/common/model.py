#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'


import unittest
from page.login_page import Login_Page
from selenium import webdriver


class Model(unittest.TestCase):
    '''unittest框架用例模板（打开浏览器登录、关闭浏览器），其他测试用例继承该类'''
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.l=Login_Page(cls.driver)
        cls.l.login_action()

    @classmethod
    def tearDownClass(cls):
        cls.l.close()