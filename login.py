from selenium import webdriver
import time
# For Chrome Driver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:/Users/dvandhar/PycharmProjects/pythonProject/Chrome/chromedriver.exe")

driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath("//div[@class='_8iep _8icy _9ahz _9ah-']/div[1]/form/div[1]/div[1]/input").send_keys(9963636739)
driver.find_element_by_xpath("//div[@class='_8iep _8icy _9ahz _9ah-']/div[1]/form/div[1]/div[2]/div/input").send_keys(789)
driver.find_element_by_xpath("//div[@class='_8iep _8icy _9ahz _9ah-']/div[1]/form/div[2]/button").click()
driver.close()