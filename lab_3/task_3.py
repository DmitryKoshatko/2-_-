def main():
    sequence = 1


    while True:
        try:
            num = int(input('{sequence}-число: '
                             .format(sequence=sequence)))
            sequence += 1
            if num == 0:
                break
            if num % 3 == 0 and num % 7 == 0:
                print("Караул!")
                break
            elif num % 3 == 0:
                print("Кратно 3")
            elif num % 7 == 0:
                print("Кратно 7")
            else:
                print(num)

        except ValueError:
            print('ОШИБКА: "Число должно иметь только цифры!"')
            continue


if __name__ == "__main__":
    main()