def main():
    while True:
        number = input("Введите номер телефона: ")

        if number == "СТОП":
            print("Ввод отменен")
            break

        # Проверка начала номера
        if not (number.startswith("+7") or number.startswith("8")):
            print('ОШИБКА: "Номер должен начинаться с +7 или 8"')
            continue

        # Проверка длины
        if len(number) != 11:
            print('ОШИБКА: "Номер должен состоять из 11 цифр"')
            continue

        # Проверка на только цифры (кроме + в начале)
        only_digits = True
        for i, char in enumerate(number):
            if i == 0 and char == '+':
                continue
            if not char.isdigit():
                only_digits = False
                break

        if not only_digits:
            print('ОШИБКА: "Номер должен содержать только цифры"')
            continue

        # Проверка последовательности 924 после +7
        if number.startswith("+7") and number[2:5] != "924":
            print('ОШИБКА: "После +7 должна быть последовательность 924"')
            continue

        print("Номер корректен!")
        break


if __name__ == "__main__":
    main()