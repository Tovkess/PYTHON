from CsvReader import CsvReader
from DataPreprocessor import DataPreprocessor
from DataAnalyzer import DataAnalyzer
from DatabaseInitializer import DatabaseInitializer
from DataUploader import DataUploader
from DatabaseQueries import DatabaseQueries
import os

if __name__ == "__main__":
    csv_url = "https://informer.com.ua/dut/python/import/129-indeksi-tsin-na-zhitlo.csv"
    db_name = "house_prices.db"

    # 1. Читання
    print("--- 1. Читання даних ---")
    csv_reader = CsvReader()
    data = csv_reader.read_data(csv_url)
    print(f"Зчитано {len(data)} рядків.")

    # 2. Обробка
    print("\n--- 2. Обробка даних ---")
    preprocessor = DataPreprocessor(data)
    processed_data = preprocessor.add_index_ids()

    # 3. Аналіз (підготовка списків)
    print("\n--- 3. Аналіз даних ---")
    analyzer = DataAnalyzer(processed_data)
    indices = analyzer.get_indices()
    periods = analyzer.get_periods()
    print(f"Підготовлено {len(indices)} індексів та {len(periods)} унікальних періодів.")

    # Видаляємо стару БД, якщо вона є (щоб не дублювати дані при повторному запуску)
    if os.path.exists(db_name):
        os.remove(db_name)

    # 4. Створення БД
    print("\n--- 4. Створення Бази Даних ---")
    db_initializer = DatabaseInitializer(db_name)
    db_initializer.create_tables()
    db_initializer.close()
    print("Таблиці створено.")

    # 5. Завантаження даних в БД
    print("\n--- 5. Завантаження даних в БД ---")
    uploader = DataUploader(db_name)
    uploader.upload_indices(indices)
    uploader.upload_periods(periods)
    uploader.close()
    print("Дані завантажено.")

    # 6. Виконання запитів
    print("\n--- 6. Виконання запитів ---")
    queries = DatabaseQueries(db_name)
    
    # Пошук за конкретним періодом
    target_period = "2016 Q1"
    found_indices = queries.find_indices_by_period(target_period)
    print(f"Індекси за періодом '{target_period}':", found_indices)

    # Середні значення (приклад виводу перших 3 результатів)
    average_indices = queries.get_average_index_by_period()
    print("Середні значення індексів за періодами (перші 3):", average_indices[:3])

    queries.close()