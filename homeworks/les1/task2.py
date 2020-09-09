"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
user_sec = input('Введите время в секундах:\n')
while not user_sec.isdigit():
    user_sec = input('Введено некорректное значение. Введите время в секундах (целое число):\n')
else:
    user_sec = int(user_sec)
hours = user_sec // 3600
minutes = user_sec // 60 - hours * 60
sec = user_sec - hours * 3600 - minutes * 60
print(f'{hours:>02}:{minutes:>02}:{sec:>02}')
