#!/usr/bin/env python
# -*- coding:utf-8 -*-
__auth__ = 'HUDI'

import unittest, time
import HTMLTestRunner_cn
from tomorrow import threads
import os

curpath = os.path.dirname(os.path.realpath(__file__))

casepath = os.path.join(curpath, 'cases')

reportpath = os.path.join(curpath, 'reports')


def add_cases():
    discover = unittest.defaultTestLoader.discover(start_dir=casepath,
                                                   pattern='*.py')
    return discover

@threads(2)
def run_case(all_cases,nth=0):
    report_file=os.path.join(reportpath,'result%s.html'%nth)
    fp=open(report_file,'wb')
    runner=HTMLTestRunner_cn.HTMLTestRunner(description='用例执行情况',
                                            title='chandao_ui',
                                            stream=fp)
    return runner.run(all_cases)


if __name__=="__main__":
    cases=add_cases()
    for i,j in zip(cases,range(len(list(cases)))):
        run_case(i,nth=j)

