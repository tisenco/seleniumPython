import os
import sys
#curpath=os.path.abspath(os.getcwd())
sys.path.append(os.getcwd())
import unittest
from test_case import *
suite=unittest.TestSuite()
import HTMLTestRunner
import time
now_time=time.strftime('%Y-%m-%d %H.%M.%S')

aa=[one.Baidu]
for i in aa:
    suite.addTest(unittest.makeSuite(i))
    filepa='C:/pyproject/report/'+now_time+'.html'
    fp=open(filepa,'wb')
    htmla=HTMLTestRunner.HTMLTestRunner(stream=fp,description='描述',title='测试百度')
    htmla.run(suite)