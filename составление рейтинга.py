# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.

# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

#my_list = [13, 9, 7, 5, 3, 3, 2]   # - вариант 1

#user_type = int(input("Введите новый элемент рейтинга: "))

# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

#if user_type > max(my_list):

#    my_list.insert(0, user_type)

#   print(my_list)

#elif user_type < min(my_list):

#    my_list.insert(0, user_type)

#    my_list.sort()

#    print(my_list[::-1])

#elif user_type in my_list:

#    match_index = my_list.index(user_type)

#    my_list.insert(match_index + 1, user_type)

#    print(my_list)

#else:

#    my_list.insert(0, user_type)

#    my_list.sort()

#    print(my_list[::-1])



my_list = [13, 9, 7, 5, 3, 3, 2]  # - вариант 2

user_type = int(input("Введите новый элемент рейтинга: "))

i = 0

for el in my_list:

    if user_type <= el:

        i += 1

my_list.insert(i, user_type)

print(my_list)
