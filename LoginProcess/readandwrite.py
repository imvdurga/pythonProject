#Importing libraries
import pytest as pytest
from openpyxl import Workbook, load_workbook
from selenium import webdriver
import time

@pytest.fixture()
def test_setup():
    print("fixture")

    # global TestCaseName
    # global Description
    # global Directory
    # global Execution
    # global driver
    # global UseCase
    # global test
    # #Testcase Configurations
    # TestCaseName = "readandwrite"
    # Description = "My Name is Durga"
    # Directory = "LoginProcess"
    # Execution = "Yes"
    # UseCase = "durga"
    # test = "C:/Users/dvandhar/PycharmProjects/pythonProject/execute.xlsx"
    #
    #
    # #If Execution is YES working with Webbrowser
    # if Execution in "Yes":
    #     print("Execution of the process "+Execution)
    #     driver = webdriver.Chrome(executable_path="C:/Users/dvandhar/PycharmProjects/pythonProject/Chrome/chromedriver.exe")
    #     driver.implicitly_wait(5)
    #     driver.maximize_window()
    #     driver.get("https://www.facebook.com/")
    #     driver.find_element_by_xpath(
    #         "//div[@class='_8iep _8icy _9ahz _9ah-']/div[1]/form/div[1]/div[1]/input").send_keys(9963636739)
    #     driver.find_element_by_xpath(
    #         "//div[@class='_8iep _8icy _9ahz _9ah-']/div[1]/form/div[1]/div[2]/div/input").send_keys("imvdurga@13Prasad")
    #     driver.find_element_by_xpath(
    #         "//div[@class='_8iep _8icy _9ahz _9ah-']/div[1]/form/div[2]/button").click()
    #     time.sleep(5)
    #
    # #If Execution is NO will skip the testcase
    # else:
    #     print("test")
    #     # Initiate the worksheet for Excel
    #     path = "C:/Users/dvandhar/PycharmProjects/pythonProject/PDFFileNameData/FileName.xlsx"
    #     wb = load_workbook(filename=path)
    #     sheet = wb.worksheets[1]
    #     sheet.cell(row=1, column=1).value = TestCaseName
    #     sheet.cell(row=1, column=6).value = "Skip"
    #     sheet.cell(row=1, column=4).value = Description
    #     sheet.cell(row=1, column=3).value = Directory
    #     wb.save(path)
    yield
    print("yield")
    # if Execution == "Yes":
    #     print("Checking yield execution YES")
    # else:
    #     print("Checking yield execution NO")
    # driver.close()
@pytest.mark.smoke
def test_readandwrite(test_setup):
    print("testcase")
    # print("Printing")
    #
    # #Initiate the worksheet for Excel
    # wb1 = load_workbook(filename = test)
    # sheet1 = wb1.worksheets[0]
    # print(sheet1.title)
    #
    # #For-loop for Iterating complete Excel file
    # for r in range(1,11):
    #     print("first loop"+str(r))
    #     if sheet1.cell(r,1).value == None:
    #         print("loop is empty")
    #         break
    #     else:
    #         if sheet1.cell(r,1).value in UseCase:
    #             print("Use Case Is Correct " +sheet1.cell(r,1).value)
    #             if sheet1.cell(r,2).value in "Yes":
    #                 print("Can perform the Execution because its failing with Yes: " +sheet1.cell(r,2).value)
    #                 Execution = "Yes"
    #                 sheet1.cell(row=r, column=3).value = "Correct"
    #                 sheet1.cell(row=r, column=4).value = "Test Case is Passed"
    #             elif sheet1.cell(r,2).value in "No":
    #                 print("Can't perform the Execution because it satisfies with No: " +sheet1.cell(r,2).value)
    #                 Execution = "No"
    #                 sheet1.cell(row=r, column=3).value = "InCorrect"
    #                 sheet1.cell(row=r, column=4).value = "Test Case is Failed"
    # print()
    #
    # #Saving Excel file
    # wb1.save(test)
