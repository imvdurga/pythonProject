from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:/Users/dvandhar/PycharmProjects/pythonProject/Chrome/chromedriver.exe")
driver.get("https://www.google.co.in/")
print(driver.title)
driver.close()

