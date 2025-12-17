def calculate_salary(employees):
    print("\n--- Розрахунок зарплати ---")
    for name, data in employees.items():
        salary_rate = data['salary']
        days_worked = data['days']
        
        # Формула з завдання 1.2
        monthly_salary = (salary_rate / 30) * days_worked
        
        print(f"Співробітник: {name}")
        print(f"  Ставка: {salary_rate}")
        print(f"  Відпрацьовано днів: {days_worked}")
        print(f"  Нараховано: {monthly_salary:.2f} грн")
        print("-" * 20)