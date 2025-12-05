number = int(input("введите любое целое положительное число: "))
i = 0
clone_number = number

while clone_number > 0:
    digit = clone_number % 10
    if digit > i:
        i = digit

    else:
        digit = i
        clone_number = clone_number // 10

print(f"в числе {number}")
print(f"самая большая цифра {digit}")
