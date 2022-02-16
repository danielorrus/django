from contextvars import Context
from pipes import Template
from pydoc import doc
from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
    doc_externo = open("/home/mint20/Documentos/Python/Django/Proyecto1/Proyecto1/plantillas/miplantilla.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

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