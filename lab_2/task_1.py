def task1():
    str1 = input("Введите первую строку: ").strip().lower()
    str2 = input("Введите вторую строку: ").strip().lower()

    # Проверяем, что обе строки являются либо "да", либо "нет"
    # И при этом они равны друг другу
    if (str1 == "да" or str1 == "нет") and (str2 == "да" or str2 == "нет"):
        if str1 == str2:
            print("ВЕРНО")
        else:
            print("НЕВЕРНО")
    else:
        print("НЕВЕРНО")


if __name__ == "__main__":
    task1()