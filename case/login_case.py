# -*- coding:utf-8 -*-
# Author : zhuke
# Data : 2019/12/11 16:41
import sys
import os
#集成时要先设置环境变量，才能引包如case,page
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from case.basecase import BaseCase
from page.login_page import LoginPage
from selenium.webdriver.common.by import By
from data import users
from model import driver
import ddt

@ddt.ddt
class LoginCase(BaseCase):
    # @ddt.data(*[{'username':'admin','password':'admin'}])
    # @ddt.data(*users.users)
    #    @ddt.data(*driver.get_table('user', 'Sheet1'))
    #    @ddt.unpack
    #    def test_login_case(self, username, password):
    #        lp=LoginPage(self.driver)
    #        lp.open()
    #        lp.login_submit(username, password)
    #        a=self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/a').text
    #        self.assertIn('admin', a)

    @ddt.file_data('../data/user.yaml')
    def test_login_case(self, **kwargs):
        print(kwargs)
        username=kwargs.get('username')
        password=kwargs.get('password')
        print(username)
        print(password)
        lp=LoginPage(self.driver)
        lp.open()
        lp.login_submit(username, password)
        a=self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/a').text
        self.assertIn('admin', a)

