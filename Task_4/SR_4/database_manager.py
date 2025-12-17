import sqlite3

class DatabaseManager:
    def __init__(self, db_name="students.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Створення таблиці students, якщо вона відсутня."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                group_number TEXT NOT NULL,
                birth_date TEXT
            )
        """)
        self.conn.commit()

    def add_student(self, student):
        """Додавання студента в БД."""
        self.cursor.execute("INSERT INTO students (full_name, group_number, birth_date) VALUES (?, ?, ?)",
                            (student.full_name, student.group_number, student.birth_date))
        self.conn.commit()
        print(f"Студента '{student.full_name}' додано.")

    def update_student_group(self, full_name, new_group):
        """Оновлення групи студента за ПІБ."""
        self.cursor.execute("UPDATE students SET group_number = ? WHERE full_name = ?", (new_group, full_name))
        self.conn.commit()
        print(f"Групу студента '{full_name}' оновлено на '{new_group}'.")

    def delete_student(self, full_name):
        """Видалення студента за ПІБ."""
        self.cursor.execute("DELETE FROM students WHERE full_name = ?", (full_name,))
        self.conn.commit()
        print(f"Студента '{full_name}' видалено.")

    def get_all_students(self):
        """Отримання всіх студентів."""
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()