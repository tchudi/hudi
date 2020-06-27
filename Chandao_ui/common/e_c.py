#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def find_element(dr,loc):
    try:
        element=WebDriverWait(dr,10).until(EC.presence_of_element_located(loc))
        return element
    except:
        print(loc,'元素未找到')
dr=webdriver.Chrome()

dr.get('https://www.baidu.com')
loc=('id','kw')
find_element(dr,loc).send_keys('python')

result=EC.presence_of_element_located(loc)(dr)
print(result)