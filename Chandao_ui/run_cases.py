#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'


import unittest
import HTMLTestRunner_cn
import sys
import time

sys.path.append(r'D:/Chandao_ui')

if __name__=="__main__":
    casespath='./cases/'
    report='./reports/'+time.strftime('%Y%m%d%H%M%S',time.localtime())+'_report.html'
    discover=unittest.defaultTestLoader.discover(start_dir=casespath,
                                                 pattern='*.py')
    fp=open(report,'wb')
    runner=HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                            description='用例执行情况',
                                            title='禅道ui自动化测试报告')
    runner.run(discover)
