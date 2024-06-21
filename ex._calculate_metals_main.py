import openpyxl

# открываю файл
xlsx_name = r'2024 05 22 p.xlsx'
wb = openpyxl.load_workbook(xlsx_name)

# создается объект с заданного листа книги
xlsx_sheet_name = r'Conc. in Sample Units'
sheet = wb[xlsx_sheet_name]

# получаю номера последнего ряда и последней колонки
row_count = sheet.max_row
column_count = sheet.max_column

# листы для работы переменные
samples = []  # а нужен ли? он же будет в словаре, как ключи
samples_dict = {}
metals_columns = {'As': 'L', 'Cd': 'V', 'Cu': 'AB', 'Ni': 'AS', 'Pb': 'AU', 'Zn': 'BM'}  # Связь металлов и столбцов

print(f"A bond between metals and columns: {metals_columns}")

for i in range(1, row_count + 1):
    sample_name = sheet.cell(i, 2).value
    # print(f'i={i}, {sheet.cell(i, 2).coordinate} = {sample_name}')
    sample_code_with_prefix = sheet.cell(i, 2).value.split()[0]  # переписать по получение списка из слов в ячейке
    sample_code = sample_code_with_prefix[2:]
    if sample_code_with_prefix[:2] == "p-":

        sample_suffix = sheet.cell(i, 2).value.split()[1]  # получаю суффикс пробы
        samples_dict[sample_code] = {sample_suffix: {}}  # записал суффикс в словарь

        # Записываю значения по металлам в словарь
        for metal in metals_columns:
            samples_dict[sample_code][sample_suffix][metal] = \
                {sheet.cell(i, sheet[metals_columns[metal] + str(i)].column).value}

        samples.append(sample_code)   # список для проб мне сейчас не актуален
        # samples_dict[sample_code[2:]] = 0
print(f"A list of samples from the file: {samples}", f"A samples dictionary: {samples_dict}\n", sep='\n')

# Сохраняю книгу в файл и закрываю
wb.save(xlsx_name)
wb.close()
