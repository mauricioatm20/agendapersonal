from django.db import models

# Create your models here.

class agendaPersonal(models.Model):
    name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    address = models.CharField(max_length=65)
    city = models.CharField(max_length=65)
    age = models.IntegerField()

    def __str__(self):
        return self.name