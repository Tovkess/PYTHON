class StudentFinder:
    def __init__(self, json_reader):
        self.json_reader = json_reader
        self.data = None

    def load_data(self, path):
        """Завантажує дані за допомогою JsonReader."""
        self.data = self.json_reader.read_data(path)

    def find_students_by_surname(self, surname):
        """Пошук студентів за прізвищем."""
        if not self.data:
            raise ValueError("Дані не завантажено. Спочатку викличте метод load_data.")
        # Шукаємо збіг по ключу 'Прізвище'
        return [student for student in self.data if student.get('Прізвище') == surname]

    def display_students_info(self, students):
        """Виведення інформації про студентів."""
        if not students:
            print("Студентів не знайдено.")
            return
            
        for student in students:
            pib = student.get('Прізвище', '') + " " + student.get('Ім\'я', '')
            print(f"ПІБ: {pib}")
            print("Завдання:")
            for key, value in student.items():
                if 'Завдання' in key:
                    print(f"  {key}: {value}")
            print("-----------")