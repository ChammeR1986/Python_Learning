# Для заполнения списка элементов необходимо использовать функцию input().

my_list = list(input("enter any values: "))   # - вариант 2

# Реализовать в списке обмен значениями соседних элементов попарно.
# В случае нечётного числа значений, последний оставить на месте.

for el in range(1, len(my_list), 2):

    my_list[el-1], my_list[el] = my_list[el], my_list[el-1]

print("your changing values is: " , my_list)


user_type = input("Enter your type: ").split() # - вариант 2

x = 0

print(f"'Your type is: ' {user_type}")

while x + 1 < len(user_type):

    if x % 2 == 0:

        user_type.insert(x, user_type.pop(x+1))

    x += 1

print(f"'Your changing value is: ' {user_type}")