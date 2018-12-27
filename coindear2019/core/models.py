from __future__ import unicode_literals
import datetime
from django.db import models
from tinymce.models import HTMLField
#Agregar Modulos personales

#Elementos del FAQ
class Faq(models.Model):
    orden = models.IntegerField()
    pregunta = models.CharField('Titulo', max_length=200)
    respuesta = HTMLField()
    def __str__(self):
        return self.pregunta