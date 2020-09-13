"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
goods_template = {
    'name': 'Введите наименование товара',
    'price': 'Введите цену товара',
    'quantity': 'Введите кол-во товара',
    'unit': 'Введите единицы измерения'
}

goods_list = []
goods_dict = {}
idx = 1
user_answer = ''
while user_answer != 'stop':  # выход по вводу команды stop
    print(f'Вводим параметры товара {idx}')
    for key, ask in goods_template.items():
        if key != 'price' and key != 'quantity':  # вводим нечисловые параметры
            goods_dict[key] = input(ask + ':\n')
        else:   # вводим пока количество и цена не будут числом
            while True:
                goods_dict[key] = input(ask + ':\n')
                if goods_dict[key].isdigit():
                    goods_dict[key] = int(goods_dict[key])
                    break
                else:
                    print('Введено некорректное значение.')
    goods_list.append((idx, goods_dict.copy()))    # заполняем список параметрами введенного товара
    print(f'Ввод товара {idx} завершен.')
    user_answer = input('Наберите stop для окончания ввода товаров или любой символ для продолжения\n')
    idx += 1
print('Перечень введенных товаров:', goods_list)

analytics_dict = {}
for good in goods_list:
    for goods_key, goods_value in good[1].items():
        if goods_key in analytics_dict:  # проверяем есть ли уже такой ключ в словаре аналитики
            if goods_value not in analytics_dict[goods_key]:  # избегаем дублирования значения, через set не получилось
                analytics_dict[goods_key].append(goods_value)
        else:
            analytics_dict[goods_key] = [goods_value]  # если ключа еще нет, создаем список с первым значением
print(analytics_dict)
