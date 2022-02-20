from contextvars import Context
from pipes import Template
from pydoc import doc
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request):
    nombre = "Juanillo"
    apellido = "Pérecillo"
    P1 = Persona(nombre, apellido)
    temasdelcurso = ["plantillas", "modelos", "formularios", "vistas", "despliegue"]

    ahora = datetime.datetime.now()
    
    # las que tienen una sola almohadilla son la primera versión
    # las que tienen dos almohadillas son la segunda


    #doc_externo = open("/home/mint20/Documentos/Python/Django/Proyecto1/Proyecto1/plantillas/miplantilla.html")
    #plt = Template(doc_externo.read())
    #doc_externo.close()
    ##doc_externo = loader.get_template('miplantilla.html') #la carpeta de las plantillas está indicada en el archivo settings.py

    #ctx = Context({"nombre_persona": P1.nombre, "apellido_persona": P1.apellido, "momento_actual": ahora, "temas": temasdelcurso})
    ##documento = doc_externo.render({"nombre_persona": P1.nombre, "apellido_persona": P1.apellido, "momento_actual": ahora, "temas": temasdelcurso})
    ##return HttpResponse(documento)

    # el render de abajo es django.shortcuts.render
    return render(request, "miplantilla.html", {"nombre_persona": P1.nombre, "apellido_persona": P1.apellido, "momento_actual": ahora, "temas": temasdelcurso})

def despedida(request):
    return HttpResponse("<h1>me cago en tu puta madre</h1>")

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """
    <html>
        <body>
            <h1>Me cago en vuestra puta madre el %s</h1>
        </body>
    </html>
    """ % fecha_actual
    return HttpResponse(documento)

def calculaEdad(request, edad, agno):
    edadFutura = edad + agno - 2022
    documento = "<html><body><h2>En el año %s tendrás %s años</h2></body></html>" %(agno, edadFutura)
    return HttpResponse(documento)


def cursoc(request):
    fecha_actual = datetime.datetime.now()

    return render(request, "cursoc.html",{"dameFecha": fecha_actual})


def cursocss(request):
    fecha_actual = datetime.datetime.now()

    return render(request, "cursocss.html",{"dameFecha": fecha_actual})