# Lab 4-9 Part 1 by Chris Reutz
from openpyxl import Workbook

WB_NAME = 'lab4-9.xlsx'

# open workbook
wb = Workbook()

# open sheet
ws = wb.active

# enter a row of data in the sheet
row_data = ['Linux Server-Side Dev', 'COMP 644']
ws.append(row_data)

# write to the workbook
wb.save(WB_NAME)
print('File written: ', WB_NAME)