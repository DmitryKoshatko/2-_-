def task3():
    # Исходные данные: словарь пользователей и их друзей
    social_network = {
        "Иван": ["Мария", "Петр", "Анна"],
        "Мария": ["Иван", "Петр", "Сергей"],
        "Петр": ["Иван", "Мария", "Анна", "Сергей"],
        "Анна": ["Иван", "Петр"],
        "Сергей": ["Мария", "Петр", "Елена"],
        "Елена": ["Сергей"]
    }

    print("Социальная сеть:")
    for user, friends in social_network.items():
        print(f"  {user}: {', '.join(friends)}")
    print()

    # 1. Находим взаимных друзей
    print("1. Взаимные друзья:")
    mutual_friends = {}

    for user1 in social_network:
        for user2 in social_network:
            if user1 != user2:
                if user2 in social_network[user1] and user1 in social_network[user2]:
                    pair = tuple(sorted([user1, user2]))
                    if pair not in mutual_friends:
                        mutual_friends[pair] = True
                        print(f"   {user1} ↔ {user2}")
    print()

    # 2. Пользователь с наибольшим количеством связей
    max_friends_user = max(social_network, key=lambda x: len(social_network[x]))
    max_friends_count = len(social_network[max_friends_user])

    print(f"2. Больше всего друзей у: {max_friends_user} ({max_friends_count} друзей)")
    print()

    # 3. Друзья друзей (расширенный круг) для каждого пользователя
    print("3. Расширенный круг общения (друзья друзей):")

    for user in social_network:
        friends_of_friends = set()

        # Для каждого друга пользователя
        for friend in social_network[user]:
            # Добавляем друзей этого друга
            friends_of_friends.update(social_network[friend])

        # Убираем самого пользователя и его прямых друзей
        friends_of_friends.discard(user)
        for friend in social_network[user]:
            friends_of_friends.discard(friend)

        if friends_of_friends:
            print(f"   {user}: {', '.join(sorted(friends_of_friends))}")
        else:
            print(f"   {user}: нет друзей друзей")


if __name__ == "__main__":
    task3()