from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, prac_score, prac_count, exam_scr):
        self.name = name
        self.age = age
        self.prac_score = prac_score
        self.prac_count = prac_count
        self.exam_scr = exam_scr

    def avg_practice_score(self):
        if self.prac_count != 0:
            return self.prac_score / self.prac_count
        else:
            return 0

    def display_info(self):
        print(f"Ім'я: {self.name}")
        print(f"Вік: {self.age}")
        print(f"Середній бал за практичні: {self.avg_practice_score()}")

    @abstractmethod
    def total_score(self):
        pass