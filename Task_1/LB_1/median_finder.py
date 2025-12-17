def find_median(user_input):
    numbers_list = [int(item) for item in user_input.split(',')]
    numbers_list.sort()
    n = len(numbers_list)

    if n % 2 == 1:
        median = numbers_list[n // 2]
    else:
        median = (numbers_list[n // 2 - 1] + numbers_list[n // 2]) / 2
    
    return median

user_input = input("Будь ласка, введіть список чисел, розділених комами: ")
median_result = find_median(user_input)
print(f"Медіана: {median_result}")