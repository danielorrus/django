from django.http import HttpResponse
import datetime

def saludo(request):
    documento = "<h1>que te den por culo</h1>"
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