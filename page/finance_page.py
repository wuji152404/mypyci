# -*- coding:utf-8 -*-
# Author : zhuke
# Data : 2019/12/14 13:55

from page.base_page import BasePage
from selenium.webdriver.common.by import By

class FinancePage(BasePage):

    payables_navi_locator=(By.XPATH,'/html/body/div[5]/div[1]/ul/li[1]/a/text()')
    addpayables_button_locator=(By.XPATH,'/html/body/div[5]/div[2]/div[1]/div[3]/a[1]')
