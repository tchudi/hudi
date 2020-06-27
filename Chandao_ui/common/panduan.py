#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.base import Base
from selenium import webdriver


class Panduan(Base):
    def text_in_element(self, loc, text):
        '''判断元素是否等于文本'''
        try:
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(loc, text))
            return True
        except:
            return False

    def alert_is(self):
        '''判断是否有弹框'''
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            return True
        except:
            return False

    def alert_accept(self):
        '''弹框后点击确认'''
        if self.alert_is():
            return self.driver.switch_to.alert.accept()
        else:
            return None


if __name__ == "__main__":
    driver=webdriver.Chrome()
    p=Panduan(driver)
    p.openbrowser()
    username_loc=('id','account')
    pwd_loc=('name','password')
    p.input(username_loc,'hudi5')
    p.input(pwd_loc,'Hd123456')
    submit_loc=('id','submit')
    p.click(submit_loc)
    p.alert_accept()