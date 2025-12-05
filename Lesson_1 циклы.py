number = int(input("enter number 0 - 9: "))
i = 0
while True:
    i += 1
    if i >= 10:
        break
    if i % 2 == 0:
        continue
    print(i)
