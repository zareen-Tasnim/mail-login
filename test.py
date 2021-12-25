import openpyxl
import xlutils
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
PATH = "C:\\Program Files\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://account.protonmail.com/login')
time.sleep(5)
path = "D://Kinetic/datafile.xlsx"
rows = xlutils.getRowCount(path, 'Sheet1')
for r in range(2, rows+1):
    username = xlutils.readdata(path, "Sheet1", r, 1)
    password = xlutils.readdata(path, "Sheet1", r, 2)
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/main/div[2]/form/button").click()
    time.sleep(5)

    driver.find_element_by_class_name("logo").click()
    time.sleep(5)