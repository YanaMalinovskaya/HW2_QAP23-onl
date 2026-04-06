#1. Создай класс Library с атрибутом класса books = [] и методами add_book(title), remove_book(title) и show_books(). 
# Продемонстрируй, что список книг общий для всех объектов класса.

class Library:
    books = []

    def add_book(self, title):
        Library.books.append(title)

    def remove_book(self, title):
        if title in Library.books:
            Library.books.remove(title)

    def show_books(self):
        return Library.books
    
lib1 = Library()
lib2 = Library()

lib1.add_book("1994")
print(lib2.show_books())

#2. Создай иерархию: базовый класс Employee с атрибутами name и salary, методом get_info(). 
# Дочерние классы Manager (добавляет department) и Developer (добавляет language). Каждый переопределяет get_info().

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"Имя: {self.name}, Зарплата: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_info(self):
        return f"{super().get_info()}, Отдел: {self.department}"

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def get_info(self):
        return f"{super().get_info()}, Язык: {self.language}"
    
mgr = Manager("Иван", 120000, "QA")
dev = Developer("Анна", 150000, "Python")

print(mgr.get_info())
print(dev.get_info())

#3. Реализуй класс Stack (стек) с протектед атрибутом _items = [] и методами push(item), pop(), peek() (посмотреть верхний элемент), 
# is_empty() и size().

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop() if not self.is_empty() else "Стек пуст"

    def peek(self):
        return self._items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

my_stack = Stack()

my_stack.push("Тест 1")
my_stack.push("Тест 2")
my_stack.push("Тест 3")

print(f"Верхний элемент сейчас: {my_stack.peek()}")
print(f"Размер стека: {my_stack.size()}")

my_stack.pop() 
print(f"Осталось элементов: {my_stack.size()}")
print(f"Стек пустой? {my_stack.is_empty()}")

#4. Создай класс Vehicle с методом move(), выводящим "Moving...". Создай дочерние классы Car, Boat и Plane, 
# каждый переопределяет move() по-своему. Напиши функцию start_journey(vehicle), которая вызывает move() у любого переданного транспорта - 
# продемонстрируй полиморфизм.

class Vehicle:
    def move(self):
        print("Moving...")

class Car(Vehicle):
    def move(self):
        print("Едет по дороге")

class Boat(Vehicle):
    def move(self):
        print("Плывет по воде")

class Plane(Vehicle):
    def move(self):
        print("Летит в небе")

def start_journey(vehicle):
    vehicle.move()

start_journey(Car())   
start_journey(Plane()) 

#5. Создай класс Student с атрибутами name и grades (список оценок). 
# Добавь методы add_grade(grade), average() (средняя оценка), highest() и lowest(). 
# Защити grades через одиночное подчёркивание.

class Student:
    def __init__(self, name):
        self.name = name
        self._grades = []

    def add_grade(self, grade):
        if 1 <= grade <= 5:
            self._grades.append(grade)

    def average(self):
        return sum(self._grades) / len(self._grades) if self._grades else 0

    def highest(self):
        return max(self._grades) if self._grades else None

    def lowest(self):
        return min(self._grades) if self._grades else None

student = Student("Яна")
student.add_grade(5)
student.add_grade(4)
student.add_grade(3)

print(f"Студент: {student.name}")
print(f"Средний балл: {student.average():.2f}")
print(f"Лучшая оценка: {student.highest()}")
print(f"Худшая оценка: {student.lowest()}")