"""
URL configuration for concecionaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from AMR import views
from AMR.views import CompraCreate, IndexView, VehiculoCreateView, ClienteCreateView 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('comprar/<int:vehiculo_id>/', views.comprar, name='comprar'),
    path('vehiculos/', VehiculoCreateView.as_view(), name='cargar_vehiculo'),
    path('clientes/', ClienteCreateView.as_view(), name='cargar_cliente'), 
    path('',IndexView.as_view(), name='index'),
    path('mostrar_vehiculos/', views.mostrar_vehiculos, name='mostrar_vehiculos'), 
    path('historia_empresa/', views.historia_empresa, name='historia_empresa'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
