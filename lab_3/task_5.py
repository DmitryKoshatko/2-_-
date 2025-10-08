def main():
    try:
        result = int(input("1-число: "))
        sequence = 2


        while True:
            op = input(f"{sequence}-операция: ")
            sequence += 1

            if op == "стоп":
                break
            if op not in ["+", "-", "*", "/"]:
                print('ОШИБКА: "Допустимы только +, -, *, /"')
                continue

            try:
                num = int(input(f"{sequence}-число: "))
                sequence += 1
            except ValueError:
                print('ОШИБКА: "Введите целое число!"')
                continue

            if op == "+":
                result += num
            elif op == "-":
                result -= num
            elif op == "*":
                result *= num
            elif op == "/":
                if num == 0:
                    print('ОШИБКА: "Деление на ноль!"')
                    continue
                result /= num

            print(f"Промежуточный результат: {result}")

        print(f"\nИтоговый результат: {result}")

    except ValueError:
        print('ОШИБКА: "Первое значение должно быть числом!"')


if __name__ == "__main__":
    main()