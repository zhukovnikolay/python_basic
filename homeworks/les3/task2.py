"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

user_template = {
    'first_name': ('Имя пользователя: ', str),
    'last_name': ('Фамилия пользователя: ', str),
    'birth_year': ('Год рождения пользователя: ', int),
    'city': ('Город проживания пользователя: ', str),
    'email': ('E-mail пользователя: ', str),
    'phone': ('Телефон пользователя: ', str)
}


def print_user(first_name, last_name, birth_year, city, email, phone):
    print(f'{first_name} {last_name}, {birth_year} года рождения, '
          f'город проживания: {city}, email: {email}, телефон: {phone}')


user = {}

for key, value in user_template.items():
    while True:
        user_value = input(f'{value[0]}\n')
        try:
            user_value = value[1](user_value)
        except ValueError:
            print(f'Неверное значение данных')
            continue
        user[key] = user_value
        break

print_user(
    first_name=user['first_name'],
    last_name=user['last_name'],
    city=user['city'],
    birth_year=user['birth_year'],
    email=user['email'],
    phone=user['phone']
)
