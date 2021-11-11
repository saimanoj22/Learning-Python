# usage: py spreadsheetCellInverter.py myFile.xlsx
import sys, openpyxl

file = sys.argv[1]
wb = openpyxl.load_workbook(file)
sheet = wb.active
maxRow = sheet.max_row
maxCol = sheet.max_column

out_wb = openpyxl.Workbook()
out_sheet = out_wb.active

for i in range(1, maxRow + 1):
    for j in range(1, maxCol + 1):
        out_sheet.cell(row=j, column=i).value = sheet.cell(row=i, column=j).value
file = file.replace('.xlsx','')
out_wb.save(file+'_inverted.xlsx')