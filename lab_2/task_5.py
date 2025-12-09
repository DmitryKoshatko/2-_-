def task5():
    july = input("Город в июле: ").strip()
    august = input("Город в августе: ").strip()

    # Условие: (июль == "Тула" или август == "Пенза") и не оба одновременно
    condition = (july == "Тула" and august != "Пенза") or (july != "Тула" and august == "Пенза")

    if condition:
        print("ДА")
    else:
        print("НЕТ")


if __name__ == "__main__":
    task5()