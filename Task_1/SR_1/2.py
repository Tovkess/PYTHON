import math


x_input = input("Введіть останню цифру вашого порядкового номера у списку групи (x): ")
x = int(x_input)
t = 1  


denominator = math.sqrt(t) - abs(math.sin(t))

if denominator == 0:
    Z = "Знаменник дорівнює нулю, обчислення неможливе."
else:
   
    numerator = 9 * math.pi * t + 10 * math.cos(x)
   
    Z_value = (numerator / denominator) * math.exp(x)
    Z = f"{Z_value:.2f}"

print(f"Значення x: {x}, Значення t: {t}")
print(f"Значення Z: {Z}")
