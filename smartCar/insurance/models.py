from django.db import models
from car.models import Car


class Insurance(models.Model):
    sum = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE, default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.end_date}'
