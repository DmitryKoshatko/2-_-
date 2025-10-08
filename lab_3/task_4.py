def main():
    text = input("Введите текст: ")
    vowels = consonants = others = 0
    vowel_set = "аеёиоуыэюяaeiou"


    while text:
        char = text[0].lower()
        if char.isalpha():
            if char in vowel_set:
                vowels += 1
            else:
                consonants += 1
        else:
            others += 1
        text = text[1:]

    print(f"\nГласных: {vowels}")
    print(f"Согласных: {consonants}")
    print(f"Остальных символов: {others}")


if __name__ == "__main__":
    main()