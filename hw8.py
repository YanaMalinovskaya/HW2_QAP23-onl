#1. Напишите рекурсивную функцию palindrome(s), которая проверяет, является ли строка палиндромом. 
# Без срезов и reversed(), только рекурсия.

def palindrome(s, left=0, right=None):
    
    if right is None:
        right = len(s) - 1
    
    if left >= right:
        return True
    
    if s[left].lower() != s[right].lower():
        return False
    
    return palindrome(s, left + 1, right - 1)

def task_1():
    test_words = ["наган", "мешок", "дерево", "Лёша на полке клопа нашёл"]
    
    for word in test_words:
        clean_word = word.replace(" ", "")
        result = palindrome(clean_word)
        print(f"'{word}' — палиндром? {result}")

#2. Напишите функцию make_validator(min_val, max_val), которая возвращает функцию-валидатор. 
# Валидатор принимает число и возвращает True если оно в диапазоне, иначе False.

def make_validator(min_val, max_val):
    
    def validator(n):
        
        return min_val <= n <= max_val
    
    return validator

def task_2():

    age_validator = make_validator(18, 99)
    
    print(f"16 лет подходит? {age_validator(16)}")  # False
    print(f"19 лет подходит? {age_validator(19)}")  # True

#3. Напишите декоратор @retry(n), который при возникновении любого исключения повторяет вызов функции до n раз. 
# Если все попытки провалились — пробрасывает последнее исключение.

def retry(n):

    def decorator(func):

        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(1, n + 1):
                try:
                    return func(*args, **kwargs)
                
                except Exception as e:
                    last_exception = e

                    print(f"Попытка {attempt}/{n} не удалась: {e}")
            
            raise last_exception
        
        return wrapper
    
    return decorator

@retry(3)

def unstable_function():
    import random

    if random.random() < 0.7:  
        raise ValueError("Временный сбой сети")
    
    return "Данные успешно получены!"

def task_3():

    try:
        result = unstable_function()

        print(f"Результат: {result}")

    except Exception as e:

        print(f"Функция окончательно упала после всех попыток: {e}")

#4. Напишите декоратор @deprecated(message), который выводит предупреждение при вызове функции (через warnings.warn) и всё равно выполняет её. 
# Сохраняйте метаданные через functools.wraps.

# PS чет совсем не поняла

import functools
import warnings

def deprecated(message):

    def decorator(func):
        @functools.wraps(func)

        def wrapper(*args, **kwargs):
            warnings.warn(
                f"Функция '{func.__name__}' устарела: {message}", 
                category=DeprecationWarning, 
                stacklevel=2
            )
            
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator

@deprecated("используйте новую функцию new_login()")

def old_login():
    return "Вы вошли через старую систему"

def task_4():

    print(old_login())

#5. Напишите рекурсивную функцию binary_search(lst, target) (бинарный поиск числа в списке), оберните её декоратором @logger, 
# который логирует каждый вызов с параметрами.  
# PS сложно для меня пока что

import functools

def logger(func):
    @functools.wraps(func)

    def wrapper(*args, **kwargs):

        print(f"--> Вызов {func.__name__} | Аргументы: {args}")

        result = func(*args, **kwargs)
        
        print(f"<-- {func.__name__} вернул: {result}")

        return result
    
    return wrapper

@logger
def binary_search(lst, target, low=0, high=None):

    if high is None:
        high = len(lst) - 1
    
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if lst[mid] == target:
        return mid  
    elif lst[mid] > target:
        return binary_search(lst, target, low, mid - 1)
    else:
        return binary_search(lst, target, mid + 1, high)

def task_5():
    my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 15
    
    print(f"Ищем число {target} в списке {my_list}\n")
    index = binary_search(my_list, target)
    
    if index != -1:
        print(f"\nРезультат: Число найдено на индексе {index}")
    else:
        print("\nРезультат: Число не найдено")

if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    