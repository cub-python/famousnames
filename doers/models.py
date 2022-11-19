from django.db import models


# Create your models here
class Doer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveBigIntegerField()
    place_of_birth = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.last_name} | {self.first_name} | {self.birthday_year} | {self.place_of_birth}'


class Biography(models.Model):
    text = models.TextField(null=True, blank=True)
    doer = models.OneToOneField(Doer, on_delete=models.CASCADE)


class Success(models.Model):
    name = models.TextField(max_length=64)
    doers = models.ManyToManyField(Doer)
