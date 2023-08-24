from django.db import models 

# Create your models here.

from django.db import models

class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()
    imagen = models.ImageField(upload_to='vehiculos/')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.marca} {self.modelo}"
 
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre

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
