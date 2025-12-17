def input_product():
    products = {}
    while True:
        name = input("Введіть назву товару або 'stop' щоб закінчити: ")
        if name.lower() == 'stop':
            break
        try:
            price = float(input("Введіть ціну товару: "))
            stock = int(input("Введіть залишок товару на складі: "))
            products[name] = {'Ціна': price, 'Залишок': stock}
        except ValueError:
            print("Будь ласка, введіть коректні числові значення.")
    return products