from django.shortcuts import redirect, render

# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import Compra
from .forms import CompraForm
from .models import Vehiculo
from .forms import VehiculoForm
from .models import Cliente
from .forms import ClienteForm
from .forms import CompraForm

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

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = '/clientes/' 


class IndexView(TemplateView):
    template_name = 'AMR/index.html'
def tienda_online(request):
    return render(request, 'tienda_online.html') 

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