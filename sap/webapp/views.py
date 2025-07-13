from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona


# Create your views here.
def bienvenido(request):
    mensajes ={'msg1':'Pagina bienvendio template django'}
    return render(request,'bienvenido.html',mensajes)

def mvm(request):
    no_Personas= Persona.objects.count(),
    personas   = Persona.objects.all().order_by('id')
    return render(request,'Personainfo.html',{'no_Personas':no_Personas,'personas':personas})

