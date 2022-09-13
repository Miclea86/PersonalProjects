from django.db import models

from user.models import User


class Car(models.Model):
    brand_choices = (('alfa romeo', 'Alfa Romeo'), ('audi', 'Audi'), ('b.m.w.', 'B.M.W'),
                     ('dacia', 'Dacia'), ('fiat', 'Fiat'), ('ford', 'Ford'), ('honda', 'Honda'),
                     ('mercedez-benz', 'Mercedez-Benz'), ('opel', 'Opel'), ('peugeot', 'Peugeot'),
                     ('renault', 'Renault'), ('seat', 'Seat'), ('skoda', 'Skoda'), ('smart', 'Smart'),
                     ('toyota', 'Toyota'), ('volkswagen', 'Volkswagen'), ('other', 'Other'))
    brand = models.CharField(max_length=20, choices=brand_choices)
    type_of_car = models.CharField(max_length=30, default='')
    num_plate = models.CharField(max_length=15)
    engine_size = models.IntegerField()
    year = models.IntegerField()
    is_electric = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.brand} {self.num_plate}'
