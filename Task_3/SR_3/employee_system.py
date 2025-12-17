# 1. Створення класу "Співробітник"
class Employee:
    # 1.2 та 2.2 Ініціалізація атрибутів (з 4.1 робимо їх захищеними через підкреслення)
    def __init__(self, name, salary, days_worked, bonus_percentage=0):
        self._name = name
        self._salary = salary
        self._days_worked = days_worked
        self._bonus_percentage = bonus_percentage

    # 4.2 Геттери та сетери (Інкапсуляція)
    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @property
    def days_worked(self):
        return self._days_worked

    @property
    def bonus_percentage(self):
        return self._bonus_percentage

    @bonus_percentage.setter
    def bonus_percentage(self, value):
        if 0 <= value <= 100:
            self._bonus_percentage = value
        else:
            print("Відсоток бонусу має бути від 0 до 100")

    # 2.1 Метод розрахунку місячної зарплати
    def calculate_salary(self):
        # Формула: (заробітна_плата / 30) * кількість_відпрацьованих_днів
        return (self._salary / 30) * self._days_worked

    # 2.3 Метод розрахунку бонусу
    def calculate_bonus(self):
        # Формула: (Заробітна_плата / 100) * відсоток_бонуса
        return (self._salary / 100) * self._bonus_percentage

    def __str__(self):
        return f"Співробітник: {self._name}"


# 3. Наслідування: Клас Менеджер
class Manager(Employee):
    # 3.2 Розмір премії (встановлюється в класі для всіх один)
    _manager_bonus_size = 200  # Наприклад, 200 грн за кожного підлеглого

    def __init__(self, name, salary, days_worked, subordinates_count, bonus_percentage=0):
        super().__init__(name, salary, days_worked, bonus_percentage)
        self._subordinates_count = subordinates_count

    # Геттер для кількості підлеглих
    @property
    def subordinates_count(self):
        return self._subordinates_count

    # 3.3 Метод звіту
    def generate_report(self):
        return f"Менеджер {self._name} керує {self._subordinates_count} співробітниками."

    # 5. Поліморфізм: Перевизначення методу розрахунку бонусу
    def calculate_bonus(self):
        # 5.1 Формула: бонус співробітника + (кількість_підлеглих * розмір_премії)
        base_bonus = super().calculate_bonus()
        manager_extra = self._subordinates_count * self._manager_bonus_size
        return base_bonus + manager_extra

    def __str__(self):
        return f"Менеджер: {self._name}"


# 6. Робота з об'єктами (main)
if __name__ == "__main__":
    # 7.1 Створення об'єктів
    emp1 = Employee("Іван Петренко", 30000, 20, 10)  # Зарплата 30к, 20 днів, 10% бонус
    emp2 = Employee("Олена Сидоренко", 32000, 22, 5)
    
    mgr1 = Manager("Анна Коваленко", 50000, 20, 5, 15) # 5 підлеглих, 15% бонус
    mgr2 = Manager("Дмитро Бондар", 55000, 15, 10, 20) # 10 підлеглих

    # 7.2 Додавання до списку
    staff_list = [emp1, emp2, mgr1, mgr2]

    # 7.3 Демонстрація розрахунків
    print("--- Відомість по зарплаті ---")
    for person in staff_list:
        salary = person.calculate_salary()
        bonus = person.calculate_bonus()
        
        print(f"{person}")
        if isinstance(person, Manager):
            print(f"  {person.generate_report()}")
        print(f"  Відпрацьовано днів: {person.days_worked}")
        print(f"  Зарплата: {salary:.2f} грн")
        print(f"  Бонус: {bonus:.2f} грн")
        print(f"  РАЗОМ: {salary + bonus:.2f} грн")
        print("-" * 30)