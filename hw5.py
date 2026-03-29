#1. Напиши код который выведет таблицу умножения до 10 на N (введенное с клавиатуры) в таком формате
#  3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 27

n = int(input("Введите число N: "))
result = " | ".join(str(n * i) for i in range(1, 10))
print(result)

#2. Попроси пользователя ввести имя и возраст. Выведи фразу: «Через 10 лет тебе будет <X> лет, <ИМЯ>!»

name_user = str(input("Введите имя: "))
age_user = int(input("Введите возраст: "))
print("Через 10 лет тебе будет {} лет, {}!".format(age_user + 10, name_user))

#3. Даны два списка цен в долларах и курс валюты. Используй map чтобы перевести все цены в рубли. 
# Затем используй zip чтобы создать словарь {товар: цена_в_рублях}
# PS Я взяла свои значения

items = ["Dress", "T-shirt", "Coat"]
price_usd = [300, 500, 700]
rate = 2.967

price_byn = list(map(lambda x: x * rate, price_usd))
result_dict = dict(zip(items, price_byn))

print(result_dict)


#4. Напиши функцию fizzbuzz(n) которая принимает число и возвращает строку: 
# 'Fizz' если делится на 3, 'Buzz' если делится на 5, 'FizzBuzz' если делится на оба, 
# иначе само число в виде строки. Вызови её для чисел от 1 до 20 через map.

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)
    
result = list(map(fizzbuzz, range(1, 21)))

print(result)

#5. Напиши функцию *args с именем my_stats которая принимает любое количество чисел 
# и возвращает сразу три значения — минимум, максимум и среднее. 

def my_stats(*args):
    minimum = min(args)
    maximum = max(args)
    average = sum(args) / len(args)
    return minimum, maximum, average

mn, mx, avg = my_stats(10, 20, 30, 40, 50, 60, 70, 80, 90)

print(f"Минимум: {mn}, Максимум: {mx}, Среднее: {avg}")

#6. Напиши функцию build_profile(**kwargs) которая принимает любые именованные аргументы 
# и возвращает словарь с этими данными плюс автоматически добавляет ключ 'registered': True. 
# Добавь к функции docstring.

def build_profile(**kwargs):
    """
    Создает профиль пользователя из произвольных именованных аргументов.
    Автоматически добавляет статус регистрации.
    """
    profile = kwargs
    profile['registered'] = True
    
    return profile

user = build_profile(name="Ivan", age=40, city="Minsk")

print(user)

#7. Создай модуль math_utils.py с тремя функциями: square(n) — возводит в квадрат, cube(n) — возводит в куб, 
# is_even(n) — возвращает True/False. В main.py импортируй модуль, попроси пользователя ввести число через input,
#  примени все три функции и выведи результаты. Защити вызовы конструкцией if __name__ == "__main__".

import math_utils

def main():
    number = int(input("Введите целое число: "))

    sq = math_utils.square(number)
    cb = math_utils.cube(number)
    even = math_utils.is_even(number)

    print(f"Результаты для числа {number}:")
    print(f"- Квадрат: {sq}")
    print(f"- Куб: {cb}")
    print(f"- Является четным: {even}")

if __name__ == "__main__":
    main()