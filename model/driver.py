# -*- coding:utf-8 -*-
# Author : zhuke
# Data : 2019/12/11 15:03

from selenium import webdriver
import xlrd, os

fa_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
data_path=os.path.abspath(os.path.join(fa_path, 'data'))
page_path=os.path.abspath(os.path.join(fa_path, 'page'))
model_path=os.path.abspath(os.path.join(fa_path, 'model'))
case_path=os.path.abspath(os.path.join(fa_path,'case'))
report_path=os.path.abspath(os.path.join(fa_path,'report'))
DRIVER_PATH = os.path.abspath(os.path.join(fa_path,'driver'))



def getchrome():
    # options=webdriver.ChromeOptions()
    #options.binary_location('C:\Users\65606\AppData\Local\Google\Chrome\Application\chrome.exe')
    # options.add_argument('disabled-inforbars')
    # driver=webdriver.Chrome(options=options)
    option=webdriver.ChromeOptions()
    option.binary_location=r'C:\Users\65606\AppData\Local\Google\Chrome\Application\chrome.exe'
    driver=webdriver.Chrome(options=option)
    #
    # driver=webdriver.Chrome(os.path.join(DRIVER_PATH,'chromedriver.exe'))
    return driver


def get_table(tablename, Sheetname):
    data=xlrd.open_workbook(data_path + tablename + '.xlsx')
    table=data.sheet_by_name(Sheetname)
    lis=[]
    # 去表头
    for row in range(1, table.nrows):
        lis.append(table.row_values(row))
    return lis


if __name__ == '__main__':
    # print(get_table('user', 'Sheet1'))
    print(DRIVER_PATH)