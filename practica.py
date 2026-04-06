name = input("Введите имя: ")
print (f"Привет, {name}")

num_1 = input("Введите первое число: ")
num_2 = input("Введите второе число: ")

sum_ = float(num_1) + float(num_2)
print (sum_)

number = int(float(input("Введите число: ")))

if number % 2 == 0:

    print ("Число четное")

else:

    print ("Число нечетное")

movies = ["Один дома", "Гарри Поттер", "Шрек"]

print(movies[1])
print(f"Всего фильмов: {len(movies)}")

resume = {
    "hero_name": "Yana",
    "power_level": 2,
    "is_flying": True,
    "enemies": ["Jira", "Kiki", "Piki"],
    "stats": {"health": "strong", "mana": "fire"}
}
print(f"Второй враг: {resume["enemies"][1]}")