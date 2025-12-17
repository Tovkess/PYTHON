from FullTimeStudent import FullTimeStudent
from PartTimeStudent import PartTimeStudent

# Створюємо об'єкти студентів
student1 = FullTimeStudent(name="KOLA", age=24, prac_score=910, prac_count=10, exam_scr=95, attend_pct=85)
student2 = FullTimeStudent("Klavdia Petrivna", 19, 930, 10, 99, 20)
student3 = PartTimeStudent("CHEEV", 22, 390, 4, 78)
student4 = PartTimeStudent("YAKTAK", 21, 480, 5, 82)

# Створюємо список навчального закладу
university_students = [student1, student2, student3, student4]

# Виведемо успішність кожного студента
for student in university_students:
    student.display_info()
    print("---------")