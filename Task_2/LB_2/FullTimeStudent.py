from Person import Person

class FullTimeStudent(Person):
    def __init__(self, name, age, prac_score, prac_count, exam_scr, attend_pct):
        super().__init__(name, age, prac_score, prac_count, exam_scr)
        self.attend_pct = attend_pct

    def total_score(self):
        # Формула: 0.6 * S_pr + 0.3 * S_ex + 0.1 * S_att
        S_pr = self.avg_practice_score()
        return 0.6 * S_pr + 0.3 * self.exam_scr + 0.1 * self.attend_pct

    def display_info(self):
        print(f"\nСтудент (Очна форма):")
        super().display_info()
        print(f"Загальний бал: {self.total_score():.1f}")