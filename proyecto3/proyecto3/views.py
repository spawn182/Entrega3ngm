from django.http import HttpResponse
from django.template import Template, Context


def saludar(request):
    return HttpResponse("Hola mundo!")

def segundaVista(request):
    return HttpResponse("<h1>Segunda vista!</h1>")

def saludo_con_nombre(request,nombre):
    return HttpResponse(f"<h1>Hola {nombre} cómo estás?</h1>")

def probandoHTML(request):
    diccionario={"nombre":"Nico", "apellido":"González", "edad":"30"}

    archivo = open(r"C:\Users\Usuario\Documents\Curso Python Coder\Entrega_trabajo3\proyecto3\plantillas\template1.html")
    contenido=archivo.read()
    archivo.close()
    template= Template(contenido)
    contexto = Context(diccionario)
    documento = template.render(contexto)
    return HttpResponse(documento)

def tercera(request):
    return HttpResponse("prueba")

