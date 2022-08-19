from django.db import models

# Create your models here.

class Clientes(models.Model):
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField(max_length=7)


class Productos(models.Model):
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=20)
    price = models.IntegerField()


class Pedidos(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    delivered = models.BooleanField()
