#Traemos el sistema de Backgrounds
from background_task import background
from django.core import mail
from django.template.loader import render_to_string

#Import Personales
from .models import Mails, Mensajes

#Primer tarea
@background(schedule=60)
def crear_100_mails(lista_mails):
    crear_mails = list()
    for mail in lista_mails:
        crear_mails.append(Mails(email=str(mail)))
        Mails.objects.bulk_create(crear_mails)
    print("Tarea Realizada, ultimo mail creado: " + str(lista_mails[-1]))

@background(schedule=60)
def enviar_50_mails(msj_id, lista_mails):
    #Obtenemos el mensaje:
    mensaje = Mensajes.objects.get(pk=msj_id)
    #Abrimos el envio de correos
    connection = mail.get_connection()
    connection.open()
    #Instanciamos el objeto email
    msj_cuerpo = render_to_string('email_base.html', {
                'mensaje': mensaje,
                })
    print(msj_cuerpo)
    email = mail.EmailMessage(mensaje.titulo, msj_cuerpo, 'coindear2019@jujuy.gob.ar',
                          lista_mails, connection=connection)
    #Lo mandamos
    email.send()
