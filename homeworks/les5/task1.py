"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open('task1.txt', 'a', encoding='UTF-8') as user_file:
    str_num = 1
    while True:
        user_str = input(f'Введите строку {str_num} для записи в файл. Окончание ввода - пустая строка.\n')
        if not user_str:
            break
        user_file.write(user_str + '\n')
        str_num += 1
