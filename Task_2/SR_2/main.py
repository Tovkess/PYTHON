from data_input import input_employees
from salary_calc import calculate_salary
from general import print_employees_recursive

def main():
    
    employees_data = input_employees()
    
    if not employees_data:
        print("Список співробітників порожній.")
        return

    
    print("\n--- Список співробітників (Рекурсія) ---")
    names = list(employees_data.keys())
    print_employees_recursive(names)

    
    calculate_salary(employees_data)

if __name__ == "__main__":
    main()
