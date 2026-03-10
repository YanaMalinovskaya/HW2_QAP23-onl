#exercise1

a = -1.6
b = 2.99
a = int(a) 
b = int(b)
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
    {"1" : 27,
    "2" : 28,
    "3" : 30,
    "4" : 25,
    "5" : 29,
    "6" : 24,
    "7" : 25,
    "8" : 31,
    "9" : 27,
    "10" : 26},
]
print(school)

#exercise7 

clothes = ["T-shirt", 345, "Jeans", "Dress", "Sweater"]
print(clothes[1])

#exercise8

word1 = "businessman"
word2 = "nes"
is_inside = word2 in word1
print(is_inside)

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