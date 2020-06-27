#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver



class Base():
    '''对selenium进行二次封装，基类--其它类继承该类'''
    def __init__(self,driver,url='http://127.0.0.1:81/zentao/user-login.html'):
        self.driver=driver
        self.url=url


    def openbrowser(self):
        '''打开浏览器'''
        self.driver.maximize_window()
        self.driver.get(self.url)

    # def find_element(self,loc):
    #     '''元素定位'''
    #     try:
    #         WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*loc))
    #         return self.driver.find_element(*loc)
    #     except:
    #         print(loc,'元素未找到')

    def find_element(self,loc):
        '''元素定位 loc=('id','kw')'''
        try:
            element=WebDriverWait(self.driver,10).until(EC.presence_of_element_located(loc))
            return element
        except:
            print(loc,'元素未找到')


    def click(self,loc):
        '''点击'''
        return self.find_element(loc).click()

    def input(self,loc,value):
        '''输入文本'''
        self.find_element(loc).clear()
        return self.find_element(loc).send_keys(value)


    def switch_frame(self,loc):
        '''切换表单'''
        frame=self.find_element(loc)
        return self.driver.switch_to.frame(frame)

    def switch_default_frame(self):
        '''切换回主文档'''
        return self.driver.switch_to.default_content()


    def scroll_end(self):
        '''将滚动条拖到底部'''
        js='$(window).scrollTop(document.body.scrollHeight)'
        return self.driver.execute_script(js)


    def close(self):
        '''关闭浏览器'''
        return self.driver.quit()

if __name__=="__main__":
    driver=webdriver.Chrome()
    url='https://www.baidu.com'
    b=Base(driver,url)
    b.openbrowser()
    loc=('id','kw')
    b.input(loc,'python')
    submit=('id','su')
    b.click(submit)