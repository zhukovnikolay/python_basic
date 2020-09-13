"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""
my_rating = [8, 6, 4, 4, 1]
print(f'Изначальный список рейтингов: {my_rating}')
while True:
    user_rating = input('Введите значение рейтинга:\n')
    if user_rating.isdigit():
        user_rating = int(user_rating)
        break
    else:
        print('Некорректное значение (нужно натуральное число)')

idx = 0
if user_rating in my_rating:
    my_rating.insert(my_rating.count(user_rating) + my_rating.index(user_rating), user_rating)
elif user_rating > my_rating[0]:
    my_rating.insert(0, user_rating)
elif user_rating < my_rating[-1]:
    my_rating.append(user_rating)
else:
    while not my_rating[idx + 1] < user_rating < my_rating[idx]:
        idx += 1
    my_rating.insert(idx + 1, user_rating)
print(f'Список с добавленным рейтингом: {my_rating}')
