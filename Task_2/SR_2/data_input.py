def input_employees():
    employees = {}
    print("Введіть дані співробітників (або 'stop' для завершення):")
    while True:
        name = input("Ім'я співробітника: ")
        if name.lower() == 'stop':
            break
        try:
            salary = float(input("Заробітна плата (ставка): "))
            days = int(input("Кількість відпрацьованих днів: "))
            # Зберігаємо дані у словник за ключем (ім'я)
            employees[name] = {'salary': salary, 'days': days}
        except ValueError:
            print("Помилка! Будь ласка, вводьте числові значення для зарплати та днів.")
    return employees