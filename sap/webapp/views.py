from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola mundo desde django')

def adios(request):
    return HttpResponse('adios django')

def contact(request):
    html = """
    <html>
        <head><title>Contacto</title></head>
        <body>
            <h1>Página de contacto</h1>
            <p>Email: contacto@ejemplo.com</p>
            <p>Teléfono: 555-1234</p>
        </body>
    </html>
    """
    return HttpResponse(html)