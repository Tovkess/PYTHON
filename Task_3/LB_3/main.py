class Person:
    def __init__(self, first_name, last_name, grade=1):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade

    def get_info(self):
        return f"Студент: {self.first_name} {self.last_name}, Оцінка: {self.grade}"

    def __del__(self):
        print(f"Ви отримали стипендію {self.first_name} {self.last_name}")

student1 = Person("Іван", "Петренко", 5)
student2 = Person("Марія", "Ковальчук", 4)
student3 = Person("Олег", "Сидоренко")

print("--- Інформація про студентів ---")
print(student1.get_info())
print(student2.get_info())
print(student3.get_info())

print("\n--- Нарахування стипендій (видалення об'єктів) ---")
del student1
del student2
del student3

print("\n")
input("Натисніть Enter для виходу...")