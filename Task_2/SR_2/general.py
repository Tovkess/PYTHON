def print_employees_recursive(names_list, index=0):
    # Базовий випадок: якщо індекс виходить за межі списку
    if index >= len(names_list):
        return
    
    # Виводимо поточне ім'я
    print(f"- {names_list[index]}")
    
    # Рекурсивний виклик для наступного елемента
    print_employees_recursive(names_list, index + 1)