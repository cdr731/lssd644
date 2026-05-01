# Lab 4-9 Part 1b by Chris Reutz
from openpyxl import load_workbook

WB_NAME = 'lab4-9.xlsx'

# open workbook
wb = load_workbook(WB_NAME)

# open sheet
ws = wb.active
cell_data = []

# read in the rows
print(f'='*20)
for row in ws.values:
    for datum in row:
        cell_data.append(datum)
        print(f'{cell_data[-1]}')
print(f'='*20)
print(f'XL file read from {WB_NAME}')