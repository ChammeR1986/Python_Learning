# Пользователь вводит месяц в виде целого числа от 1 до 12. # -вариант 1

# user_type = int(input("Enter number of the month 1 - 12: "))

# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

# if user_type == 1 or user_type == 2 or user_type == 12:

# print(user_type, "this month is winter")

# elif user_type == 3 or user_type == 4 or user_type == 5:

# print(user_type, "this month is spring")

# elif user_type == 6 or user_type == 7 or user_type == 8:

# print(user_type, "this month is summer")

# elif user_type == 9 or user_type == 10 or user_type == 11:

# print(user_type, "this month is autumn")

# else: print(user_type, "incorrect number")



# Пользователь вводит месяц в виде целого числа от 1 до 12. # - вариант 2

# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

# season_list = ["winter", "winter", "spring", "spring", "spring", "summer",
#               "summer", "summer", "autumn", "autumn", "autumn", "winter"]

# user_type = int(input("Enter number of the month 1 - 12: "))

# if 0 < user_type < 13:

#    answer = season_list[user_type-1]

#    print("this month is", answer)

# else:

#    print("incorrect input, please try again")



# Пользователь вводит месяц в виде целого числа от 1 до 12. # - вариант 3

# calendar = {
# 1: 'winter',
# 2: 'winter',
# 3: 'spring',
# 4: 'spring',
# 5: 'spring',
# 6: 'summer',
# 7: 'summer',
# 8: 'summer',
# 9: 'autumn',
# 10: 'autumn',
# 11: 'autumn',
# 12: 'winter',
# }

# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

# user_input = input("Enter month number (1 - 12): ")

# Используем .get() для безопасного доступа:

# если число не валидно, вернется "error, enter valid number"

# answer = calendar.get(int(user_input), "error, enter valid number")

# print(f"{answer}")

#user_input = int(input("Enter month number (1 - 12): "))



#my_dict = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer',   # вариант 4
#           7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}

#my_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer',
#           'autumn', 'autumn', 'autumn', 'winter']

#for key in my_dict:

#    if key == user_input:

#        print(f"{user_input}) this month is {my_dict[key]}")
#        print(f"{user_input}) this month is {my_list[user_input-1]}")

#    if user_input not in my_dict:

#        print('wrong input, please try again')

#        break



user_type = input('Enter Number of the Month: ')

while True:

    if user_type.isdigit() and 0 < int(user_type) <= 12:

        season_list = ['winter', 'spring', 'summer', 'autumn', 'winter']
        season_dict = {0: 'winter', 1: 'spring', 2: 'summer', 3: 'autumn', 4: 'winter'}

        print(f"This Month is: {season_list[int(user_type)//3]}\nThis Month is: {season_dict[int(user_type)//3]}")

    else:

        print("Please enter a valid number")

    break
