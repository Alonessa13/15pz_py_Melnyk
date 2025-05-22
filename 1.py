# Створюємо клас Person, який описує людину
class Person:
    # Конструктор класу — викликається при створенні нового об'єкта
    def __init__(self, name, age, city):
        self.name = name      # Ім'я людини
        self.age = age        # Вік людини
        self.city = city      # Місто проживання

    # Метод, який виводить коротку інформацію про людину
    def show_info(self):
        print(f"{self.name}, {self.age} років, проживає у місті {self.city}")

# Створюємо об'єкт класу Person
person1 = Person("Дар'я", 18, "Київ")

# Викликаємо метод, який виведе інформацію
person1.show_info()
