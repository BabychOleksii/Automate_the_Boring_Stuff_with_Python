import openpyxl

workbook = openpyxl.load_workbook('book.xlsx')
print(type(workbook))
sheet = workbook['Sheet1']
print(type(sheet))
print(workbook.sheetnames)

cell = sheet['B3']
print(cell.value)

print(sheet['E3'].value)

print(sheet.cell(row=4, column=10))

for i in range(4, 8):
    print(1, sheet.cell(row=i, column=5).value)
