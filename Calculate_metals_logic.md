2024 06 02 - проработка логики для обработки результатов измерения металлов. Версия 1, м.б. и последняя.

Из текущей программы:
A bound between metals and columns: {'As': 'L', 'Cd': 'V', 'Cu': 'AB', 'Ni': 'AS', 'Pb': 'AU', 'Zn': 'BM'}
A list of samples from the file: ['blank', '14977', '14978', '15623', '15624', '15625', '15626', '15965', 'blank', '14977', '14978', '15623', '15624', '15625', '15626']
A samples dictionary: {'blank': 0, '14977': 0, '14978': 0, '15623': 0, '15624': 0, '15625': 0, '15626': 0, '15965': 0}

Примеры:
blank HCl
14977 HCl
14977 ac

Нахожу пробу, беру ее суффикс (HCl), записываю значение в словарь({14977: {HCl: value, ac: value}})
а вот что меня смущало. Нужен еще 1 параметр "металл". Тогда структура данных:
Проба 14977
вытяжка ac
металл As
значение 1,1

Проба 14977
вытяжка ac
металл Cd
значение 0,7

{14977:
	{ac: {As: 1.1, Cd: 0.7},
	HF: {},
	KCL: {},
	}
}

Нужно сделать словарь вытяжек:
	HF, AC, KCl, H2O, HCl
	чтобы не было возможности "изобретать" => обработать отсутствие суффиксов и те, которые не в списке
	сделать вложенные словари со стандартными наборами металлов для каждой вытяжки
Сколько знаков оставить для расчета?
Можно распределять по пробам, а можно - по вытяжкам
В каком формате выдать результат? 
	Пока план такой: отдельный лист(!) в том же файле, в первой строке - названия столбцов (имя пробы, металл, значения как для журнала - по ячейкам)
	Ячейки по порядку: имя металла, значение бланка(мг/л), значение 1(мг/л), значение 2(мг/л), значение(мг/кг)
Перед расчетом:
	значение менее нуля - заменить на ноль
Во время расчета:
	если проба меньше бланка, то считать ее, как ноль
Где в этой выдаче писать имя вытяжки?

Далее, обработка типичных ошибок:
	не правильное название вытяжки
	заменить нули на значок "<"
