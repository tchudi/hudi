#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'

from common.panduan import Panduan

class Logout_Page(Panduan):
    user_loc=('class name','user-name')
    logout_loc=('link text','退出')

    login_loc=('id','submit')
    def logout(self):
        '''退出操作'''
        self.click(self.user_loc)
        self.click(self.logout_loc)

    def sucess_result(self):
        '''退出是否成功'''
        return self.text_in_element(self.login_loc,'登录')



