from django.shortcuts import render
from django.http import HttpResponse
from .models import CarsBrand, CarsInfo

# 1. Функція для автоматичного заповнення бази (Install)
def install(request):
    # Демо-дані з завдання [cite: 538-545]
    brands_data = [
        {"BRAND_NAME": "Toyota", "BRAND_COUNTRY": "Japan", "BRAND_RATING": 9},
        {"BRAND_NAME": "Ford", "BRAND_COUNTRY": "USA", "BRAND_RATING": 8},
        {"BRAND_NAME": "BMW", "BRAND_COUNTRY": "Germany", "BRAND_RATING": 9}
    ]
    
    cars_data = [
        {"CAR_NAME": "Corolla", "CAR_MODEL": "2023", "CAR_PRICE": 20000, "CAR_BRAND": "Toyota"},
        {"CAR_NAME": "Mustang", "CAR_MODEL": "2022", "CAR_PRICE": 35000, "CAR_BRAND": "Ford"},
        {"CAR_NAME": "X5", "CAR_MODEL": "2023", "CAR_PRICE": 60000, "CAR_BRAND": "BMW"}
    ]

    response_text = ""

    # Додаємо бренди
    for b_data in brands_data:
        # get_or_create перевіряє наявність, щоб уникнути дублікатів [cite: 536]
        brand, created = CarsBrand.objects.get_or_create(
            BRAND_NAME=b_data["BRAND_NAME"],
            defaults={
                "BRAND_COUNTRY": b_data["BRAND_COUNTRY"],
                "BRAND_RATING": b_data["BRAND_RATING"]
            }
        )
        if created:
            response_text += f"Brand {b_data['BRAND_NAME']} created.<br>"
        else:
            response_text += f"Brand {b_data['BRAND_NAME']} already exists.<br>"

    # Додаємо машини
    for c_data in cars_data:
        # Знаходимо бренд для машини
        brand = CarsBrand.objects.get(BRAND_NAME=c_data["CAR_BRAND"])
        
        car, created = CarsInfo.objects.get_or_create(
            CAR_NAME=c_data["CAR_NAME"],
            CAR_BRAND=brand,
            defaults={
                "CAR_MODEL": c_data["CAR_MODEL"],
                "CAR_PRICE": c_data["CAR_PRICE"]
            }
        )
        if created:
            response_text += f"Car {c_data['CAR_NAME']} created.<br>"
        else:
            response_text += f"Car {c_data['CAR_NAME']} already exists.<br>"

    return HttpResponse(response_text)

# 2. Функція відображення (Display)
def show_cars(request):
    cars = CarsInfo.objects.all()
    return render(request, 'duikt_task_gordienko/index.html', {'cars': cars})