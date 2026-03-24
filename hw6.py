#1. Напиши функцию copy_file(source: str, destination: str) -> bool которая читает 
# содержимое файла source и записывает его в destination. Возвращает True если успешно. 
# Проверь что файл-копия создался.

import os

def copy_file(source: str, destination: str) -> bool:
    try:
        with open(source, 'r', encoding='utf-8') as src:
            content = src.read()
            
        with open(destination, 'w', encoding='utf-8') as dest:
            dest.write(content)
            
        return os.path.exists(destination)
    
    except Exception:
        return False

if __name__ == "__main__":
    with open("test_source.txt", "w", encoding="utf-8") as f:
        f.write("Привет! Это данные для копирования.")

    if copy_file("test_source.txt", "test_destination.txt"):
        print("Успех: Файл скопирован и существует!")
    else:
        print("Ошибка: Что-то пошло не так.")

#2. Создай файл grades.txt где каждая строка содержит имя студента и его оценку через запятую:
#Анна,85
#Иван,72
#Петр,91
#Напиши код который читает файл и добавляет в конец каждой строки статус: 'отлично' если оценка >= 90, 
# 'хорошо' если >= 75, иначе 'удовлетворительно'. Сохрани результат в новый файл grades_with_status.txt.

with open('grades.txt', 'w', encoding='utf-8') as f:
    f.write("Анна,85\n")
    f.write("Иван,72\n")
    f.write("Петр,91\n")

with open('grades.txt', 'r', encoding='utf-8') as infile, \
     open('grades_with_status.txt', 'w', encoding='utf-8') as outfile:
    
    for line in infile:
        name, grade_str = line.strip().split(',')
        grade = int(grade_str)
        
        if grade >= 90:
            status = 'отлично'
        elif grade >= 75:
            status = 'хорошо'
        else:
            status = 'удовлетворительно'
         
        outfile.write(f"{name},{grade},{status}\n")

print("Файл grades_with_status.txt успешно создан!")

#3. Напиши функцию age_calculator(birth_date_str: str) -> int которая принимает дату рождения 
# в формате 'dd/mm/yyyy' (input)  и возвращает полных лет. 

from datetime import datetime

def age_calculator(birth_date_str: str) -> int:
    birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
    
    today = datetime.today()
    
    age = today.year - birth_date.year
    
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
        
    return age

date_input = input("Введите дату рождения (дд/мм/гггг): ")
print(f"Полных лет: {age_calculator(date_input)}")


#4.Напиши модуль file_utils.py с тремя полностью аннотированными функциями:

#def read_lines(filename): ...
#def write_lines(filename, lines): ...
#def count_words(filename): ... # count_words считает сколько раз каждое слово встречается в файле 
# и возвращает словарь. 
#В main.py импортируй и протестируй все три.

import file_utils

def main():
    file_name = "test.txt"
    test_data = ["Привет мир", "Python это круто", "Мир любит Python", "мир!"]

    file_utils.write_lines(file_name, test_data)
    print(f"1. Данные записаны в {file_name}")

    lines = file_utils.read_lines(file_name)
    print(f"2. Прочитано строк: {len(lines)}")

    stats = file_utils.count_words(file_name)
    print("3. Статистика слов:")
    for word, count in stats.items():
        print(f"   - {word}: {count}")

if __name__ == "__main__":
    main()

#5. Напиши функцию password_checker(correct_password) которая возвращает вложенную функцию check(password). 
# Вложенная принимает пароль и возвращает True если совпадает, иначе False.

def password_checker(correct_password):
    def check(password):
        return password == correct_password
    
    return check

my_check = password_checker("secret123")

print(my_check("admin"))      
print(my_check("secret123")) 
