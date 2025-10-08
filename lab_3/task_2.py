def main():
    shortest = None
    sequence = 1


    while True:
        word = str(input('{sequence}-слово: '
                         .format(sequence=sequence)))
        has_digit = False
        for chek in word:
            if chek.isdigit():
                has_digit = True
                break
        if has_digit:
            print('ОШИБКА: "Слово должно иметь только буквы!"')
            continue
        sequence += 1

        if word == "стоп":
            break
        if shortest is None or len(word) < len(shortest):
            shortest = word


    print('\nСамое короткое слово:', shortest)


if __name__ == "__main__":
    main()