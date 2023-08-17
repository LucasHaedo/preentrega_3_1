from django.db import models 

# Create your models here.

class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField() 

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha = models.DateField()
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Pagado', 'Pagado'), ('Cancelado', 'Cancelado')])
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()