from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("salads",'Salads'),
    ('starters','Starters'),
    ('main_dishes', 'Main Dishes'),
    ('desserts', 'Desserts')
)

STATUS = (
    (0,'available'),
    (1, 'unavailable')
)

class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=1000)
    price = models. DecimalField(max_digits=10,decimal_places=2)
    meal_type = models.CharField(max_length=200,choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status =models.IntegerField(choices=STATUS)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.meal