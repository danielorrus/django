from django.http import HttpResponse

def saludo(request):
    return HttpResponse("<h1>que te den por culo</h1>")

def despedida(request):
    return HttpResponse("<h1>me cago en tu puta madre</h1>")