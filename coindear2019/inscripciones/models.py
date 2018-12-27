from django.db import models

#Creamos choices
CATEGORIA = (
        (1, 'ACTIVO'),
        (2, 'ADHERENTE'),
        (3, 'ESTUDIANTE')
    )
TIPO_DOC= (
        (1, 'Documento Nacional de Identidad'),
        (2, 'Cédula de Identidad'),
        (3, 'Libreta de Enrolamiento'),
        (4, 'Libreta Cívica'),
        (5, 'Pasaporte'),
    )

# Create your models here.
class Inscriptos(models.Model):
    tipo_doc = models.IntegerField(choices=TIPO_DOC, default=1)
    num_doc = models.CharField('Numero de Documento', max_length=50, blank=True)
    pais = models.CharField('Pais', max_length=50, blank=True)
    provincia = models.CharField('Provincia', max_length=50, blank=True)
    localidad = models.CharField('Localidad', max_length=50, blank=True)
    domicilio = models.CharField('Domicilio Particular', max_length=50, blank=True)
    telefono = models.CharField('Telefono', max_length=20, blank=True, null=True)
    fax = models.CharField('Fax', max_length=50, blank=True)
    email = models.EmailField('Correo Electronico', blank=True, null=True)
    profesion = models.CharField('Profesion', max_length=50, blank=True)
    ocupacion = models.CharField('Ocupacion', max_length=50, blank=True)
    lugar_trabajo = models.CharField('Lugar de Trabajo', max_length=50, blank=True)
    cargo =  models.CharField('Cargo/Funcion', max_length=50, blank=True)
    direccion_laboral = models.CharField('Direccion Laboral', max_length=50, blank=True)
    email_laboral = models.EmailField('Correo Electronico', blank=True, null=True)
    web = models.URLField('Web', blank=True, null=True)
    telefono_laboral = models.CharField('Telefono Laboral', max_length=20, blank=True, null=True)
    categoria = models.IntegerField(choices=CATEGORIA, default=1)
    