def main():
    first_max = second_max = float('-inf')
    sequence = 1


    while True:
        try:
            num = int(input('{sequence}-число: '
                            .format(sequence=sequence)))
            sequence += 1
            if num == 0:
                break
            if num > first_max:
                second_max, first_max = first_max, num
            elif num > second_max:
                second_max = num

        except ValueError:
            print('ОШИБКА: "Число должно иметь только цифры!"')
            continue


    print('\nПредпоследнее максимальное число:', second_max)


if __name__ == "__main__":
    main()