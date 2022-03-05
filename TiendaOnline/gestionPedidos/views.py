from django.http import HttpResponse
from django.shortcuts import render
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    if request.GET["prd"]:
        #mensaje = "Artículo buscado: %r" %request.GET["prd"]
        producto = request.GET["prd"]

        if len(producto) > 20:
            mensaje = "texto de búsqueda demasiado largo"
        else:
            articulos = Articulos.objects.filter(nombre__icontains = producto)
            return render(request, "resultados_busqueda.html", {"articulos":articulos, "query": producto})
    else:
        mensaje = "mete algo capullo"
    return HttpResponse("<h1>" + mensaje + "</h1>")

def contacto(request):
    if request.method == "POST":
        subject = request.POST["asunto"]
        message = request.POST["mensaje"] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["direccion@destino.com"]
        send_mail(subject, message, email_from, recipient_list)
        return render(request, "gracias.html")
    return render(request, "contacto.html")