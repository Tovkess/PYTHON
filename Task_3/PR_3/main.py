from CsvToJsonConverter import CsvToJsonConverter
from JsonReader import JsonReader
from StudentFinder import StudentFinder

if __name__ == "__main__":
    csv_url = "https://informer.com.ua/dut/python/import/st_gt.csv"
    json_path = "students_data.json"  # Шлях до файлу, куди буде збережено JSON

    # 1. Конвертація з CSV до JSON
    converter = CsvToJsonConverter()
    converter.read_and_convert(csv_url, json_path)

    # 2. Створення об'єкта для читання JSON
    json_reader = JsonReader()

    # 3. Пошук та виведення інформації про студентів
    finder = StudentFinder(json_reader)
    finder.load_data(json_path)
    
    surname_to_find = "Барченко"  # Прізвище для пошуку (можна змінити)
    print(f"\nПошук студента за прізвищем: {surname_to_find}")
    
    found_students = finder.find_students_by_surname(surname_to_find)
    finder.display_students_info(found_students)