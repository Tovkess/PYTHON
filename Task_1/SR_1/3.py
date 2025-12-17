import math

x_input = input("Введіть значення x для функції f(x): ")
x = float(x_input)

# Перша гілка: x >= 0 [cite: 24]
if x >= 0:
    # f(x) = 0.5 - (4/2)*sqrt(|x|)
    f_x = 0.5 - 2 * math.sqrt(abs(x))
# Друга гілка: x < 0 [cite: 24]
else:
    # f(x) = sin^2(x^2) / |x+1|
    
    # Перевірка знаменника
    denominator = abs(x + 1)
    if denominator == 0:
        f_x = "Знаменник |x+1| дорівнює нулю (при x=-1), обчислення неможливе."
    else:
        # sin(x^2)
        sin_val = math.sin(x ** 2)
        # sin^2(x^2)
        numerator = sin_val ** 2
        
        f_x = numerator / denominator

print(f"Для x = {x}, значення функції f(x) дорівнює: {f_x}")