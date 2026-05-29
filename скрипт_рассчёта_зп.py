import sys

def calc_price(hours: float, hourly_rate: float, bonus: float) -> float:
    return hours * hourly_rate + bonus

def main():
    
    if len(sys.argv) != 4:
        print("Необходимо ввести: <python скрипт_рассчёта_ЗП.py> <часы> <размер ставки> <размер бонуса>")
        sys.exit(1)

    try:

        hours = float(sys.argv[1])
        hourly_rate = float(sys.argv[2])
        bonus = float(sys.argv[3])
    
    except ValueError:

        print("Часы, ставка и бонусы должны быть числами")
        sys.exit(1)
    
    if hours<0 or hourly_rate<0 or bonus<0:
        print("Вводимые значения не могут быть отрицательными, идиот!")
        sys.exit(1)
    
    price = calc_price(hours, hourly_rate, bonus)

    print(f"Количество отработанных часов - {hours}")
    print(f"Ставка в час - {hourly_rate}")
    print(f"Бонусы - {bonus}")
    print(f"Заработная птата - {price:.2f}")


if __name__ == "__main__":
    main()
