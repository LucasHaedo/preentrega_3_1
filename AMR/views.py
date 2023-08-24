from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import Compra, Vehiculo, Cliente
from .forms import CompraForm, VehiculoForm, ClienteForm
from django.contrib import messages 
from PIL import Image

class CompraCreate(CreateView):
    model = Compra
    form_class = CompraForm
    template_name = 'compra_form.html'
    success_url = '/tienda_online/' 

class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculo_form.html'
    success_url = '/vehiculos/' 
    def form_valid(self, form):
     response = super().form_valid(form)
     messages.success(self.request, 'Cargado satisfactoriamente')
     return response

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = '/clientes/' 
    def form_valid(self, form):
     response = super().form_valid(form)
     messages.success(self.request, 'Cargado satisfactoriamente')
     return response

class IndexView(TemplateView):
    template_name = 'AMR/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener el último vehículo cargado
        ultimo_vehiculo = Vehiculo.objects.last()
        
        # Pasar el último vehículo cargado al template
        context['ultimo_vehiculo'] = ultimo_vehiculo
        return context


def mostrar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    context = {'vehiculos': vehiculos}
    return render(request, 'mostrar_vehiculos.html', context)

def historia_empresa(request):
    return render(request, 'historia_empresa.html') 

def tienda_online(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            return redirect('success_url')
    else:
        form = CompraForm()
    return render(request, 'tienda_online.html', {'form': form}) 

def comprar(request, vehiculo_id):
    # Obtener el vehículo seleccionado por el usuario
    vehiculo = Vehiculo.objects.get(id=vehiculo_id)
    
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save()
            messages.success(request, 'Compra realizada con éxito')
            return redirect('index')
    
    # Si el usuario accede a la página por primera vez o el formulario no es válido
    else:
        # Crear un formulario de compra vacío
        form = CompraForm()
        # Asignar el vehículo seleccionado al campo correspondiente del formulario
        form.fields['vehiculo'].initial = vehiculo
    
    # Renderizar la plantilla de compra con el formulario y el vehículo
    return render(request, 'compra_form.html', {'form': form, 'vehiculo': vehiculo}) 

def cargar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES)
        if form.is_valid():
            vehiculo = form.save(commit=False)
            imagen = form.cleaned_data['imagen']
            # Abrir la imagen utilizando Pillow
            img = Image.open(imagen)
            # Redimensionar la imagen al tamaño deseado
            img = img.resize((800, 600))
            # Guardar la imagen redimensionada en el servidor
            img.save('media/vehiculos/' + imagen.name)
            vehiculo.imagen = 'vehiculos/' + imagen.name
            vehiculo.save()
            return redirect('mostrar_vehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'cargar_vehiculo.html', {'form': form})