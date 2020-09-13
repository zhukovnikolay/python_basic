"""
2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
user_list = []
idx = 1
while True:
    user_elem = input(f'Введите элемент {idx}. Для окончания заполнения списка нажмите Enter\n')
    if user_elem == '':
        break
    else:
        user_list.append(user_elem)
        idx += 1
print(f'Введенный список: {user_list}')

idx = 0
while idx < len(user_list):
    if idx + 2 <= len(user_list):
        user_list[idx], user_list[idx + 1] = user_list[idx + 1], user_list[idx]
        idx += 2
    else:
        idx += 1

print(f'Измененный список: {user_list}')
