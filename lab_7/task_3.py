def task3():
    social_network = {
        "Иван": {"Мария", "Петр", "Анна"},
        "Мария": {"Иван", "Петр", "Сергей"},
        "Петр": {"Иван", "Мария", "Анна", "Сергей"},
        "Анна": {"Иван", "Петр"},
        "Сергей": {"Мария", "Петр", "Елена"},
        "Елена": {"Сергей"}
    }

    print("Социальная сеть:")
    for user, friends in social_network.items():
        print(f"  {user}: {', '.join(sorted(friends))}")

    # 1. Взаимные друзья
    print("\n1. Взаимные друзья:")
    mutual = set()
    for user, friends in social_network.items():
        for friend in friends:
            if user in social_network[friend]:
                pair = frozenset([user, friend])
                mutual.add(pair)

    for pair in sorted(mutual, key=lambda x: sorted(x)):
        a, b = sorted(pair)
        print(f"   {a} ↔ {b}")

    # 2. Пользователь с наибольшим количеством друзей
    max_user = max(social_network, key=lambda x: len(social_network[x]))
    print(f"\n2. Больше всего друзей у: {max_user} ({len(social_network[max_user])} друзей)")

    # 3. Друзья друзей
    print("\n3. Расширенный круг общения:")
    for user in social_network:
        friends_of_friends = set()
        for friend in social_network[user]:
            friends_of_friends.update(social_network[friend])

        # Исключаем себя и прямых друзей
        friends_of_friends.difference_update({user})
        friends_of_friends.difference_update(social_network[user])

        result = ', '.join(sorted(friends_of_friends)) if friends_of_friends else "нет"
        print(f"   {user}: {result}")


if __name__ == "__main__":
    task3()