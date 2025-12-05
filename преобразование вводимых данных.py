# Пользователь вводит строку из нескольких слов, разделённых пробелами.

# user_type = (input("Enter your type: "))  - вариант 1

# words = (user_type.split())

# Вывести каждое слово с новой строки.

# tower = str("\n".join(words))

# Строки необходимо пронумеровать.

# for index, line in enumerate(words, start=1):

# Если в слово длинное, выводить только первые 10 букв в слове.

#    if len(line) > 10:

#        print(f"{index} {line[:10]}""...")

#    else:

#       print(f"{index} {line}")

user_type = (input("Enter your type: ")).split()  # - вариант 2

for n, i in enumerate(user_type, 1):

    print(n, i) if len(i) <=10 else print(n, i[:10]+"...")


