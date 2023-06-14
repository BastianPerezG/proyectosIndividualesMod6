from django.db import models

# Create your models here.

class FormularioUsuariosDB(models.Model):
    rut              = models.CharField (max_length=12,   null=False, blank=False)
    nombreUsuario    = models.CharField (max_length=30,   null=False, blank=False)
    nombre           = models.CharField (max_length=30,   null=False, blank=False)
    apellido         = models.CharField (max_length=30,   null=False, blank=False)
    email            = models.EmailField(max_length=30,   null=False, blank=False)