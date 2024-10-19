from django.db import models

# Create your models here.
class Menu(models.Model):
    dish_name=models.CharField(max_length=20)
    price=models.CharField(max_length=20)
    type=models.CharField(max_length=20)
    def __str__(self):
        return self.dish_name