from django.db import models

# Create your models here.

class Clientes(models.Model):
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    email = models.EmailField(verbose_name="Email o Gmail")
    phone = models.IntegerField()
    comment = models.CharField(max_length=30,blank=True,null=True)

    #def __str__(self):
     #   return f'Cliente: {self.name} | Direc: {self.adress} | email: {self.email} | Phone: {self.phone} | Comentario: {self.comment}'


class Productos(models.Model):
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=20)
    price = models.IntegerField()

    #def __str__(self):
     #   return f"Producto: {self.name} | Sección: {self.section} | Precio: {self.price}"

class Pedidos(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    delivered = models.BooleanField()

    #def __str__(self):
     #   return f"Numero: {self.number} | Fecha: {self.date} | Entregado: {self.delivered}"


