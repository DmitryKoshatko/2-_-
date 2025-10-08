"""
Задание 4
"""
def main():
    distance = float(input("Введите расстояние поездки (км): "))
    fuel = float(input("Введите количество израсходованного топлива (л): "))
    price = float(input("Введите цену за литр бензина: "))

    consumption = (fuel / distance) * 100
    total_cost = fuel * price

    print(f"Средний расход топлива: {consumption:.2f} л/100 км")
    print(f"Стоимость всей поездки: {total_cost:.2f} руб.")


if __name__ == "__main__":
    main()