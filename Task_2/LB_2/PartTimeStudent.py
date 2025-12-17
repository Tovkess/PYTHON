from Person import Person

class PartTimeStudent(Person):
    def __init__(self, name, age, prac_score, prac_count, exam_scr):
        super().__init__(name, age, prac_score, prac_count, exam_scr)

    def total_score(self):
        # Формула: 0.7 * S_pr + 0.3 * S_ex
        S_pr = self.avg_practice_score()
        return 0.7 * S_pr + 0.3 * self.exam_scr

    def display_info(self):
        print(f"\nСтудент (Заочна форма):")
        super().display_info()
        print(f"Загальний бал: {self.total_score():.1f}")