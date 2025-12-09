def task5():
    text = input("Введите строку: ").lower()

    vowels = "аяоёэеуюыи"
    count = 0

    # Удаляем лишние пробелы и объединяем слова
    words = text.split()

    for word in words:
        for char in word:
            if char in vowels:
                count += 1

    print(f"Количество гласных букв в строке: {count}")


if __name__ == "__main__":
    task5()