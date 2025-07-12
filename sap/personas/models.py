from django.db import models

# Modelo de Domicilio
class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    colonia = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio {self.id}: {self.calle} {self.numero} {self.colonia} {self.municipio} {self.estado} {self.pais}'


# Modelo de Persona
class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Persona {self.id}: {self.nombre} {self.apellido} {self.email}'
