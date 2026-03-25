while True:
    try:
        x = int(input("enter first argument: "))
        y = int(input("enter second argument: "))

        p = 1
        for _ in range(abs(y)):
            p *= x

        ans = p if y >= 0 else 1 / p
        print(f"{ans:.3f}")
        break

    except ValueError:
        print("enter correct argument")
