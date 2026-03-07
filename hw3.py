#exercise1

a = -1.6
b = 2.99
a = round(a) 
b = round(b)
print(a, b)

#exercise2

site = "www.my_site.com#about"
site = site.replace("#", "/")
print(site)

#exercise3

text = "stroka"
text += "ing" 
print(text)

#exercise4

username = "Ivanou Ivan"
step1 = username.split( )
step2 = " ".join(step1[::-1]) #срез [старт : стоп : шаг]
print(step2)

#exercise5

space = (" go to school ")
print(space.strip())

#exercise6

school = [
    {"class": "1a", "students": 27},
    {"class": "1b", "students": 28},
    {"class": "2a", "students": 30},
    {"class": "2b", "students": 25},
    {"class": "3a", "students": 29},
    {"class": "3b", "students": 24},
    {"class": "4a", "students": 25},
    {"class": "4b", "students": 31},
    {"class": "5a", "students": 27},
    {"class": "5b", "students": 26},
]
print(school)

#total students for exercise6

totalS = 0
for school_classes in school:
    totalS += school_classes["students"]
print(totalS)

#exercise7 
#variant1(Удаляет и возвращает (дает сохранить в переменную))

clothes = ["T-shirt", 345, "Jeans", "Dress", "Sweater"]
my_list = clothes.pop(1)
print(clothes)

#variant2(Ищет текст и удаляет его)

clothes = ["T-shirt", 345, "Jeans", "Dress", "Sweater"]
clothes.remove(345)
print(clothes)

#variant3(Просто стирает (ничего не возвращает))
clothes = ["T-shirt", 345, "Jeans", "Dress", "Sweater"]
del clothes[1]
print(clothes)

#exercise8

word = "bussnesman"
print(word.startswith("bussnes"))
print(word.endswith("bussnes"))

#exercise9 #y #nesgt
x = "My name is Agent Smith"
print(x[1])
print(x.find("t"))
print(x[3:16:3]) #срез [старт : стоп : шаг]

#exercise10* 1529291

#variant1

numbers = [1, 5, 2, 9, 2, 9, 1]
#запускаю цикл
for N in numbers:
#если число N в списке встречается 1 раз
        if numbers.count(N) == 1: 
#выводим уникальное число
            print(f"Уникальное число: {N}")
#останавливаем цикл
            break

#variant2
#^(XOR)
# Если применить его к двум одинаковым числам, получится 0. 
# Если применить его к числу и нулю, получится само число.
# В итоге все пары «уничтожат» друг друга, и останется только тот, у кого нет пары.

numbers = [1, 5, 2, 9, 2, 9, 1]
result = 0
for N in numbers:
     result ^= N
print(f"Уникальное число: {result}")