from django.db import models

from names.models import Name


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=32, unique=True)
    names = models.ManyToManyField(Name)
    repository = models.URLField(blank=True)

    def __str__(self):
        return self.name


class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(Name, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
