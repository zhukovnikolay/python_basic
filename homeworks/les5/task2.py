"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
from os import path

# Открываем созданный пользователем файл или работаем с заранее созданным
while True:
    user_file_name = input('Введите имя файла для чтения или нажмите Ввод для использования файла по умолчанию...\n')
    if not user_file_name:
        user_file_name = 'task2.txt'
        break
    if path.exists(user_file_name):
        break
    else:
        print(f"Файл с именем '{user_file_name}' отсутствует")

with open(user_file_name, 'r', encoding='UTF-8') as user_file:
    file_content = user_file.readlines()
    print(f'В файле {len(file_content)} строк.')
    for idx, line in enumerate(file_content):
        print(f'Кол-во слов в строке {idx + 1}: {len(line.split())}.')
