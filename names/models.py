from django.db import models


# Create your models here
class Name(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveBigIntegerField()
    place_of_birth = models.CharField(max_length=64)
