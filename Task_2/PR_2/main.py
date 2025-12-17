from data_input import input_product
from calculations import calculate_stock_value, calculate_discount
from general import print_product_names, find_product_by_name

def main():
    print("--- Етап 1: Введення товарів ---")
    products = input_product()
    print("\nВведені товари:", products)

    print("\n--- Етап 2: Вартість залишків ---")
    calculate_stock_value(products)

    print("\n--- Етап 3: Розрахунок знижок ---")
    calculate_discount(products)

    print("\n--- Етап 4: Список назв товарів ---")
    product_names = list(products.keys())
    print_product_names(product_names)

    print("\n--- Етап 5: Пошук товару ---")
    search_name = input("Введіть назву товару для пошуку: ")
    find_product_by_name(products, search_name)

if __name__ == "__main__":
    main()