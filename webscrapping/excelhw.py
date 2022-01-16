import openpyxl
wb=openpyxl.load_workbook('Book1.xlsx')
sheet=wb.get_sheet_by_name("Sheet1")
sheet['A1']="changed dimensions"
sheet.row_dimensions[1].height=50
# sheet.merge_cells("A1:B5")
wb.save("Book1_copy.xlsx")