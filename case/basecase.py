# -*- coding:utf-8 -*-
# Author : zhuke
# Data : 2019/12/11 14:46

import unittest
from selenium import webdriver
from model import driver
import os,sys


curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(111111111111)
    def setUp(self):
        self.driver=driver.getchrome()
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()