#1. Используя filter() и lambda, отфильтруйте из списка [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] только нечетные числа.

def task_1():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

    print(f"Исходный список: {numbers}")
    print(f"Нечетные числа: {odd_numbers}")

#2. Напишите функцию apply_operations(numbers, *operations), которая принимает список чисел и произвольное количество lambda-функций, 
# последовательно применяя каждую ко всему списку.

def apply_operations(numbers, *operations):
    for op in operations:
        numbers = list(map(op, numbers))
    
    return numbers

def task_2():
    initial_numbers = [1, 2, 3, 4, 5]

    result = apply_operations(initial_numbers, lambda x: x**2, lambda x: x + 15)

    print(f"Исходные числа: {initial_numbers}")
    print(f"После операций (x**2 затем +15): {result}")

#3. Напишите генератор chunked(lst, size), который разбивает список на куски заданного размера и поочередно их выдает. 
# Например, chunked([1,2,3,4,5], 2) → [1,2], [3,4], [5].

def chunked(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

def task_3():
    data = [1, 2, 3, 4, 5]

    print(f"Исходный список: {data}")
    
    generator = chunked(data, 2)
    
    print("Кусочки:")

    for chunk in generator:
        print(chunk)

#4. Напишите генератор prime_numbers(), который бесконечно генерирует простые числа. Выведите первые 20.

def prime_numbers():
    n = 2

    while True:
        is_prime = True

        for i in range(2, int(n**0.5) + 1):

            if n % i == 0:
                is_prime = False
                break

        if is_prime:
            yield n
        n += 1

generator = prime_numbers()

print("Первые 20 простых чисел:")

for _ in range(20):

    print(next(generator), end=" ")

#5. Напишите функцию safe_convert(value, type_func), которая пытается преобразовать value с помощью переданной функции (например, int, float). 
# При ошибке возвращает None.

def safe_convert(value, type_func):

    try:
        
        return type_func(value)
    
    except (ValueError, TypeError):
        
        return None

def task_5():

    print(f"Конвертация '123' в int: {safe_convert('123', int)}")
    
    print(f"Конвертация 'abc' в int: {safe_convert('abc', int)}")
    
    print(f"Конвертация '12.5' в float: {safe_convert('12.5', float)}")

#6. Создайте собственный класс исключения NegativeNumberError. 
# Напишите функцию sqrt_safe(n), которая считает квадратный корень из числа, но при отрицательном n выбрасывает NegativeNumberError 
# c понятным сообщением.

import math #или необходимо в начале файла?

class NegativeNumberError(Exception):
    pass

def sqrt_safe(n):
    if n < 0:
        raise NegativeNumberError(f"Ошибка! Нельзя извлечь корень из отрицательного числа: {n}")
    
    return math.sqrt(n)

def task_6():
    test_values = [16, 12, -7, 36]
    
    for val in test_values:
        try:
            result = sqrt_safe(val)

            print(f"Корень из {val} равен {result}")

        except NegativeNumberError as e:
            
            print(e)

#7. Напишите функцию-калькулятор calculator(a, b, op), где op — строка ("+", "-", "*", "/"). 
# Обработайте все возможные исключения: деление на ноль, неизвестная операция, некорректные типы аргументов.

def calculator(a, b, op):
    try:
        
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Аргументы a и b должны быть числами")

        
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            
            if b == 0:
                raise ZeroDivisionError("На ноль делить нельзя")
            
            return a / b
        
        else:
            raise ValueError(f"Неизвестная операция: {op}")

    except (ZeroDivisionError, TypeError, ValueError) as e:
        
        return f"Ошибка: {e}"

def task_7():
    print(calculator(10, 5, "+"))      # Успех: 15
    print(calculator(10, 0, "/"))      # Ошибка: На ноль делить нельзя
    print(calculator(10, "5", "+"))    # Ошибка: Должны быть числами
    print(calculator(10, 5, "^"))      # Ошибка: Неизвестная операция

if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    task_5()
    task_6()
    task_7()