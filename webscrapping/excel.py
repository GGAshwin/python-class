from sqlite3 import Row
import openpyxl
wb=openpyxl.load_workbook('Book1.xlsx')
# print(wb.get_sheet_names())
sh1=wb.get_sheet_by_name("Sheet1")
# print(sh1['A1'].value)

# for i in range(1,4):
#     print(i,sh1.cell(row=i,column=1).value)

# print(sh1['A1':'B3'])
# for i in sh1['A1':'B3']:
#     for k in i:
#         print(k.value)