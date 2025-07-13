"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from personas.views import detallePersona, nuevaPersona, editar_persona, eliminar_persona
from webapp.views import bienvenido, mvm

urlpatterns = [
     path('', bienvenido),
     path('mvt', mvm,name='listado_personas'),
     path('detalle_persona/<int:id>',  detallePersona),
     path('nuevaPersona',  nuevaPersona),
     path('editar_persona/<int:id>',  editar_persona ,name='editar_persona'),
     path('eliminar_persona/<int:id>', eliminar_persona ,name='eliminar_persona'),
     path('admin/', admin.site.urls),

]
