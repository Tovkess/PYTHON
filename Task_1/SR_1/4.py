# Введення трьох цілих чисел
a = int(input("Введіть перше ціле число (a): "))
b = int(input("Введіть друге ціле число (b): "))
c = int(input("Введіть третє ціле число (c): "))

# Введення верхньої межі інтервалу N 
N = int(input("Введіть верхню межу інтервалу (N): "))

print(f"\nІнтервал для перевірки: [1, {N}]")
print("Числа, що належать інтервалу:")

found_numbers = []

# Перевірка кожного числа
if 1 <= a <= N:
    found_numbers.append(a)
if 1 <= b <= N:
    found_numbers.append(b)
if 1 <= c <= N:
    found_numbers.append(c)

if found_numbers:
    print(found_numbers)
else:
    print("Жодне з чисел не належить заданому інтервалу.")