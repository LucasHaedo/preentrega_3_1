from django import forms
from .models import Vehiculo, Cliente, Compra

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'anio']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'email'] 

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['cliente', 'vehiculo', 'fecha', 'cantidad', 'estado'] 
