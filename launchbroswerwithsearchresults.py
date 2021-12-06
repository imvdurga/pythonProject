from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import openpyxl

#To Open chrome browser
driver=webdriver.Chrome(executable_path="C:/Users/dvandhar/PycharmProjects/pythonProject/Chrome/chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://google.com/")
driver.find_element(By.)

time.sleep(5)
driver.quit()
