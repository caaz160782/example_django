from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from personas.forms import PersonaForm
from personas.models import Persona

# Create your views here.
def detallePersona(request,id):
    #persona   = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona,pk=id)
    return render(request,'personas/PersonaInfoId.html',{'persona':persona})

#PersonaForm = modelform_factory(Persona,fields='__all__')

def nuevaPersona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_personas')
    else:
        form = PersonaForm()
    return render(request, 'personas/nuevaPersona.html', {'form': form})


def editar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('listado_personas')  # O redirige a la lista
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'personas/editar.html', {'form': form})

def eliminar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    if request.method == 'POST':
        persona.delete()
        return redirect('listado_personas')  # O a lista
    return render(request, 'personas/eliminar.html', {'persona': persona})