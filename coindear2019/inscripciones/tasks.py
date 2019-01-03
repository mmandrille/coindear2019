#Traemos el sistema de Backgrounds
from background_task import background
from django.core import mail
from django.template.loader import render_to_string

#Import Personales
from .models import Mails, Mensajes
from .functions import delete_tags
#Primer tarea
@background(schedule=60)
def crear_100_mails(lista_mails):
    crear_mails = list()
    for mail in lista_mails:
        crear_mails.append(Mails(email=str(mail)))
        Mails.objects.bulk_create(crear_mails)
    print("Tarea Realizada, ultimo mail creado: " + str(lista_mails[-1]))

@background(schedule=60)
def enviar_mails(msj_id, lista_mails):
    #Obtenemos el mensaje:
    mensaje = Mensajes.objects.get(pk=msj_id)
    #Abrimos el envio de correos
    connection = mail.get_connection()
    connection.open()
    #Instanciamos el objeto email
    msj_simple = delete_tags(mensaje.cuerpo)
    email = mail.EmailMultiAlternatives(mensaje.titulo, msj_simple, 'coindear2019@jujuy.gob.ar',
                          bcc=lista_mails, connection=connection)
    msj_html = render_to_string('email_base.html', {
                'mensaje': mensaje,
                })
    email.attach_alternative(msj_html, "text/html")
    #Lo mandamos
    email.send()
