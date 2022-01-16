import openpyxl
from openpyxl.styles import Font , Style
from openpyxl import styles
wb=openpyxl.load_workbook("Book1.xlsx")
sheet=wb.get_by_sheet_name("Sheet1")
fontobj=Font(size=20,italic=True)
Styleobj=styles(font=fontobj)
sheet['A'].Style/Styleobj

#error!!