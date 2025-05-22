# Створюємо клас Car, який описує автомобіль
class Car:
    # Конструктор, який задає початкові значення
    def __init__(self, brand, model, year, color):
        self.brand = brand     # Марка авто
        self.model = model     # Модель авто
        self.year = year       # Рік випуску
        self.color = color     # Колір авто

    # Метод, який виводить повну інформацію про автомобіль
    def show_info(self):
        print(f"{self.brand} {self.model}, {self.year} року, колір: {self.color}")

    # Метод, який дозволяє змінити колір авто
    def repaint(self, new_color):
        print(f"Автомобіль перефарбовано з {self.color} на {new_color}")
        self.color = new_color

# Створюємо об'єкт класу Car
my_car = Car("Toyota", "Corolla", 2015, "білий")

# Виводимо інформацію про авто
my_car.show_info()

# Змінюємо колір авто
my_car.repaint("червоний")

# Перевіряємо зміни
my_car.show_info()
