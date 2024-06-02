import openpyxl

xlsx_name = r'2024 05 22 p.xlsx'
wb = openpyxl.load_workbook(xlsx_name)

xlsx_sheet_name = r'Conc. in Sample Units'
sheet = wb[xlsx_sheet_name]

row_count = sheet.max_row
column_count = sheet.max_column

samples = []
samples_dict = {}
metals = {'As': 'L', 'Cd': 'V', 'Cu': 'AB', 'Ni': 'AS', 'Pb': 'AU', 'Zn': 'BM'}

sample_name = sheet.cell(4, 2).value
sample_code = sample_name.split()[0]
print('sample_code for blank:', sample_code)
# print(sample_code[:1])

# sheet.cell(i, 2).value  # покажет названия проб
for i in range(1, row_count + 1):
    sample_name = sheet.cell(i, 2).value
    # print(f'i={i}, {sheet.cell(i, 2).coordinate} = {sample_name}')
    sample_code = sheet.cell(i, 2).value.split()[0]
    if sample_code[:2] == "p-":
        samples.append(sample_code[2:])
        samples_dict[sample_code[2:]] = 0
print(f'Samples list: {samples}', f'Samples dictionary: {samples_dict}', sep='\n')
# print(sheet.cell(1, 20).coordinate, sheet['AU1'].column)  # показывает координаты и столбец ячейки

# проверка правильных названий столбцов

# sheet.cell(1, i).value  # покажет названия столбцов
# for i in range(1, column_count + 1):
#     print(f'i={i}, column={sheet.cell(1, i).value}')

wb.save(xlsx_name)
wb.close()
