# from HTMLTestRunner import HTMLTestRunner
# import unittest,time,sys
# sys.path.append('D:/kyb_ui')
#
#
# if __name__=='__main__':
#     casePath='./testcases/'
#     now=time.strftime('%Y-%m-%d %H-%M-%S')
#     reportName='./reports/'+now+'.html'
#     discover=unittest.defaultTestLoader.discover(casePath,pattern='*.py')
#     fp=open(reportName,"wb")
#     run=HTMLTestRunner(stream=fp,title='考研帮自动化测试报告',description='用例执行情况')
#     run.run(discover)
#     fp.close()


from HTMLTestRunner import HTMLTestRunner
import time,unittest
import sys
sys.path.append('D:/kyb_ui/')

if __name__=="__main__":
    casepath="./testcases/"
    reportpathname="./reports/"+time.strftime("%Y%m%d-%H%M%S")+".html"
    discover=unittest.defaultTestLoader.discover(casepath,"*.py")
    fp=open(reportpathname,"wb")
    run=HTMLTestRunner(stream=fp,title="自动化测试报告",description="用例执行情况")
    run.run(discover)
    fp.close()