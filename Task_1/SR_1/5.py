# Введення трьох чисел
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

# Знаходження мінімального та максимального
min_val = min(num1, num2, num3)
max_val = max(num1, num2, num3)

# Виведення результатів 
print(f"\nВведені числа: {num1}, {num2}, {num3}")
print(f"Мінімальне число: {min_val}")
print(f"Максимальне число: {max_val}")