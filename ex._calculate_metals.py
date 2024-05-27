import openpyxl

xlsx_name = r'2024 05 22 p.xlsx'
wb = openpyxl.load_workbook(xlsx_name)

xlsx_sheet_name = r'Conc. in Sample Units'
sheet = wb[xlsx_sheet_name]

row_count = sheet.max_row
column_count = sheet.max_column

# sheet.cell(i, 2).value - покажет названия проб
for i in range(1, row_count + 1):
    print(f'i={i}, cell={sheet.cell(i, 2).value}')

# sheet.cell(1, i).value - покажет названия столбцов
for i in range(1, column_count + 1):
    print(f'i={i}, column={sheet.cell(1, i).value}')

wb.save(xlsx_name)
wb.close()
