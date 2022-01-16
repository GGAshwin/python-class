import importlib
from tkinter.ttk import Style
import openpyxl
wb=openpyxl.load_workbook('Book1.xlsx')
sh1=wb.get_sheet_by_name('Sheet1')
sh1.title="New"
print(sh1.title)
print(wb.get_sheet_names())
wb.save('Book1_copy.xlsx')
wb.create_sheet()
wb.remove_sheet(wb.get_sheet_by_name("New"))
wb.save('Book1_copy.xlsx')