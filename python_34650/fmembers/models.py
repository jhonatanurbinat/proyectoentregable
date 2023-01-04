from django.db import models

# Create your models here.


class Fmembers(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    isfamily = models.BooleanField()
    relation = models.CharField(max_length=50)

