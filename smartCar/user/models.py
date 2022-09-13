from django.contrib.auth.models import User
from django.db import models


class Userextend(User):
    gender_choices = (('male', 'Male'), ('female', 'Female'))
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=7, choices=gender_choices)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
