from random import choices
from secrets import choice
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

hourly_rate_choices= [
        (15, '15'),
        (20, '20'),
        (30, '30'),
]

teams_choices= [
        (1, '1'),
        (2, '2'),
        (3, '3'),
]

class empolyee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.IntegerField(max_length=100)
    team = models.CharField(max_length=100, choices = teams_choices,)
    hourly_rate = models.IntegerField(choices=hourly_rate_choices)