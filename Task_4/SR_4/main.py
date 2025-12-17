from student import Student
from performance import DesiredPerformance
from database_manager import DatabaseManager

def main():
    # 1. Створення об'єктів студентів
    student1 = Student("Іванов Іван Іванович", "КН-21", "2004-05-15")
    student2 = Student("Петренко Петро Петрович", "КН-21", "2003-11-20")

    # 2. Робота з успішністю (демонстрація класів)
    subjects = ["Math", "Programming", "History"]
    scores = [90, 85, 95]
    perf = DesiredPerformance(subjects, scores, desired_avg=95.0)
    print(f"Бажаний середній бал для {student1.full_name}: {perf.calculate_average_score()}")

    # 3. Робота з Базою Даних
    db = DatabaseManager("university.db")

    print("\n--- Додавання студентів ---")
    db.add_student(student1)
    db.add_student(student2)

    print("\n--- Список студентів ---")
    for row in db.get_all_students():
        print(row)

    print("\n--- Оновлення групи ---")
    db.update_student_group("Іванов Іван Іванович", "КН-22")

    print("\n--- Видалення студента ---")
    db.delete_student("Петренко Петро Петрович")

    print("\n--- Фінальний список ---")
    for row in db.get_all_students():
        print(row)

    db.close()

if __name__ == "__main__":
    main()