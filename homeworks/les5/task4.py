"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

eng_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('task4.txt', 'r', encoding='UTF-8') as file_read, open('task4_ed.txt', 'w', encoding='UTF-8') as file_write:
    for line in file_read:
        # Разбираем строку поэлементно, меняем элемент == ключу из словаря на его значение, собираем обратно
        print(' '.join([eng_dict[word] if word in eng_dict else word for word in line.split()]), file=file_write)
