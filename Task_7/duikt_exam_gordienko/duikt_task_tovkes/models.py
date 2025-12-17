from django.db import models

class CarsBrand(models.Model):
    brand_name = models.CharField(max_length=100, name='BRAND_NAME')
    brand_country = models.CharField(max_length=100, name='BRAND_COUNTRY')
    brand_rating = models.IntegerField(name='BRAND_RATING')

    def __str__(self):
        return self.BRAND_NAME

class CarsInfo(models.Model):
    car_name = models.CharField(max_length=100, name='CAR_NAME')
    car_model = models.CharField(max_length=100, name='CAR_MODEL')
    car_price = models.FloatField(name='CAR_PRICE')
    # Зв'язок "Один-до-багатьох" [cite: 532]
    car_brand = models.ForeignKey(CarsBrand, on_delete=models.CASCADE, name='CAR_BRAND')

    def __str__(self):
        return f"{self.CAR_BRAND.BRAND_NAME} {self.CAR_NAME}"