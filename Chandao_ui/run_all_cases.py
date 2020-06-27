#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'


from BeautifulReport import BeautifulReport
import unittest,os
from tomorrow import threads
'''多线程跑测试用例，并生成一个测试报告'''


curpath=os.path.dirname(os.path.realpath(__file__))
casepath=os.path.join(curpath,'cases')

if not os.path.exists(casepath):
    print('测试用例放到case目录下')
    os.mkdir(casepath)

reportpath=os.path.join(curpath,'report')
if not os.path.exists(reportpath):
    os.mkdir(reportpath)


def add_case():
    discover=unittest.defaultTestLoader.discover(start_dir=casepath,
                                                 pattern='*.py')

    return discover

@threads(3)
def run(test_suit):
    result=BeautifulReport(test_suit)
    result.report(filename='report.html',
                  description='chandao_UI测试报告',
                  log_path='report')


if __name__=='__main__':
    cases=add_case()
    for i in cases:
        run(i)

