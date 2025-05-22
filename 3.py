# Створюємо клас BankAccount, який моделює банківський рахунок
class BankAccount:
    # Конструктор задає початкові дані
    def __init__(self, owner, account_number, balance):
        self.owner = owner                # Ім'я власника
        self.account_number = account_number  # Номер рахунку
        self.balance = balance            # Поточний баланс

    # Метод для поповнення рахунку
    def deposit(self, amount):
        self.balance += amount
        print(f"Поповнення на {amount} грн. Поточний баланс: {self.balance} грн.")

    # Метод для зняття коштів з рахунку
    def withdraw(self, amount):
        # Перевірка чи достатньо коштів на рахунку
        if amount > self.balance:
            print("Помилка: недостатньо коштів на рахунку!")
        else:
            self.balance -= amount
            print(f"Знято {amount} грн. Залишок: {self.balance} грн.")

    # Метод для перевірки балансу
    def check_balance(self):
        print(f"Баланс рахунку: {self.balance} грн.")

# Створюємо об'єкт банківського рахунку
account1 = BankAccount("Іван Петрович", "UA1234567890", 1000)

# Перевіряємо баланс
account1.check_balance()

# Поповнюємо рахунок
account1.deposit(500)

# Намагаємося зняти більше, ніж є на рахунку
account1.withdraw(2000)

# Знімаємо допустиму суму
account1.withdraw(300)

# Перевіряємо фінальний баланс
account1.check_balance()
