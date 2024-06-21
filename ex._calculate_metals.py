import openpyxl

xlsx_name = r'2024 05 22 p.xlsx'
wb = openpyxl.load_workbook(xlsx_name)

xlsx_sheet_name = r'Conc. in Sample Units'
sheet = wb[xlsx_sheet_name]

row_count = sheet.max_row
column_count = sheet.max_column

samples = []
samples_dict = {}
metals_columns = {'As': 'L', 'Cd': 'V', 'Cu': 'AB', 'Ni': 'AS', 'Pb': 'AU', 'Zn': 'BM'}
print(f"A bond between metals and columns: {metals_columns}")

sample_name = sheet.cell(5, 2).value
sample_code_with_prefix = sample_name.split()[0]
print(f'A sample_name: {sample_name}')
print("sample_code_with_suffix for the sample:", sample_code_with_prefix)
# print(sample_code[:1])  # такой срез дает префикс названия пробы

# sheet.cell(i, 2).value  # покажет названия проб
for i in range(1, row_count + 1):
    sample_name = sheet.cell(i, 2).value
    # print(f'i={i}, {sheet.cell(i, 2).coordinate} = {sample_name}')
    sample_code_with_prefix = sheet.cell(i, 2).value.split()[0]  # переписать по получение списка из слов в ячейке
    if sample_code_with_prefix[:2] == "p-":
        # Добавить получение суффикса
        # добавить получение значений по металлам, т.к. у меня пока что есть номер строки
        samples.append(sample_code_with_prefix[2:])   # список для проб мне сейчас не актуален
        samples_dict[sample_code_with_prefix[2:]] = {}
print(f"A list of samples from the file: {samples}", f"A samples dictionary: {samples_dict}\n", sep='\n')
# print(sheet.cell(1, 20).coordinate, sheet['AU1'].column)  # показывает координаты и столбец ячейки

# тренируюсь грузить данные в словарь
sample_name = sheet.cell(5, 2).value
sample_cell_name = sample_name.split()
sample_suffix = sample_cell_name[1]
print(f'A suffix for a sample: {sample_suffix}')
samples_dict_2 = samples_dict
print(f'\nA sample dict before: {samples_dict_2}')
samples_dict_2[sample_cell_name[0][2:]] = {sample_suffix: {}}
print(f'A sample dict after: {samples_dict_2}')

# пробую грузить в словарь


# проверка правильных названий столбцов

# sheet.cell(1, i).value  # покажет названия столбцов
# for i in range(1, column_count + 1):
#     print(f'i={i}, column={sheet.cell(1, i).value}')

wb.save(xlsx_name)
wb.close()
