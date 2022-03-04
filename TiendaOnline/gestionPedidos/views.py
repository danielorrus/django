from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    mensaje = "Artículo buscado: %r" %request.GET["prd"]
    return HttpResponse("<h1>" + mensaje + "</h1>")