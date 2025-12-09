def task3():
    # Исходные множества друзей
    friends_A = {"Иван", "Мария", "Петр", "Анна", "Сергей"}
    friends_B = {"Петр", "Анна", "Елена", "Дмитрий", "Сергей"}

    print("Множество A:", friends_A)
    print("Множество B:", friends_B)
    print()

    # 1. Общие друщи
    common_friends = friends_A & friends_B
    print("Общие друзья:", sorted(common_friends))

    # 2. Уникальные друзья каждого пользователя
    unique_to_A = friends_A - friends_B
    unique_to_B = friends_B - friends_A
    print("\nУникальные друзья A:", sorted(unique_to_A))
    print("Уникальные друзья B:", sorted(unique_to_B))

    # 3. Все знакомые (объединение)
    all_friends = friends_A | friends_B
    print("\nВсе знакомые:", sorted(all_friends))

    # Дополнительно: симметрическая разность
    symmetric_diff = friends_A ^ friends_B
    print("Друзья, которые есть только у одного пользователя:", sorted(symmetric_diff))


if __name__ == "__main__":
    task3()