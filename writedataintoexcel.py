#import commands
from openpyxl import Workbook

#Excel file path
path="C:/Users/dvandhar/PycharmProjects/pythonProject/PDFFileNameData/FileName.xlsx"

#Initiate the workbook
workbook=Workbook()
workbook['Sheet'].title='Sheet'
Sheet=workbook.active

#Declare the worksheet headers
Sheet['A1'].value='Name'
Sheet['B1'].value='Description'
Sheet['C1'].value='Result'
#Declare the worksheet 1st row values
Sheet['A2'].value='Durga'
Sheet['B2'].value='AAA'
Sheet['C2'].value='Pass'
#Declare the worksheet 2nd row values
Sheet['A3'].value='Vandharani'
Sheet['B3'].value='BBB'
Sheet['C3'].value='Fail'

#Save the results in the excel
workbook.save(path)