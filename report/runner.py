# -*- coding:utf-8 -*-
# Author : zhuke
# Data : 2019/12/11 20:11
import sys

from BeautifulReport import BeautifulReport
import unittest , os
import time

print(os.path.abspath(os.path.dirname(__file__)))
case_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# 持续集成时不能用相对路径
report_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + '/report')
print(case_path)
print(report_path)
# discover=unittest.defaultTestLoader.discover(case_path, pattern='*_case.py')
# times=time.strftime('%Y%m%d%H%M%S')
# filename=times + 'result.html'
# BeautifulReport(discover).report('测试报告', filename=filename, report_dir=report_path)










