import sys

def calc_delivery(weight: float, rate_per_kg: float, express_fee: float) -> float:
    return weight * rate_per_kg + express_fee

def main():

    if len(sys.argv) != 4:
        print("Ввод необходимо сделать в следующем формате: "
              "python скрипт_рассчёта_стоимости_доставки.py <вес> <стоимость за кг> <доплата за скорость>")
        sys.exit(1)

    try:
        weight = float(sys.argv[1])
        rate_per_kg = float(sys.argv[2])
        express_fee = float(sys.argv[3])

    except ValueError:
        print("вводимые значения должны быть числами")
        sys.exit(1)

    if weight < 0 or rate_per_kg < 0 or express_fee < 0:
        print("значения не могут быть отрицательными")
        sys.exit(1)

    delivery = calc_delivery(weight, rate_per_kg, express_fee)
    print(f"вес посылки составляет: {weight} кг")
    print(f"стоимость за кг составляет: {rate_per_kg}")
    print(f"надбавка за срочность: {express_fee} р")
    print(f"итого: {delivery:.2f} р")

if __name__ == "__main__":
    main()