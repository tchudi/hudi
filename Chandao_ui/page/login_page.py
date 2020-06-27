#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'

from common.panduan import Panduan
#from selenium import webdriver


class Login_Page(Panduan):
    username_loc=('id','account')
    password_loc=('name','password')
    submit_loc=('id','submit')

    user_loc=('class name','user-name')


    def login(self,username='hudi',password='Hd123456'):
        '''登录操作'''
        self.input(self.username_loc,username)
        self.input(self.password_loc,password)
        self.click(self.submit_loc)

    def login_action(self,username='hudi',password='Hd123456'):
        '''封装登录'''
        self.openbrowser()
        self.input(self.username_loc, username)
        self.input(self.password_loc, password)
        self.click(self.submit_loc)

    def sucess_result(self,text):
        '''登录成功'''
        return self.text_in_element(self.user_loc,text)

    def fail_result(self):
        '''登录失败，有弹框'''
        return self.alert_is()

if __name__=="__main__":
    driver=webdriver.Chrome()
    l=Login_Page(driver)
    l.openbrowser()
    # l.login()
    # print(l.sucess_result('胡迪'))
    l.login('adddd','Hd123456')
    print(l.fail_result())



