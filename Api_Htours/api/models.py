from django.db import models

# Creacion de los modelos

class empleados(models.Model):
    name=models.CharField(max_length=50)
    edad=models.PositiveSmallIntegerField(max_length=50)