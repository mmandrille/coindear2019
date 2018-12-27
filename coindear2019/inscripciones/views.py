from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

#Import Personales
from .models import Inscriptos
from .ModelForm import InscriptoForm
from .tokens import account_activation_token

# Create your views here.
def inscripcion(request):
    if request.method == 'POST':
        form = InscriptoForm(request.POST)
        if form.is_valid():
            inscripto = form.save()
            mail_subject = 'Confirma tu Inscripcion a Coindear 2019.'
            message = render_to_string('acc_active_email.html', {
                'inscripto': inscripto,
                'token':account_activation_token.make_token(inscripto),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Por Favor Confirme la creacion de su cuenta en el correo que recibio')
    else:
        form = InscriptoForm()
    return render(request, 'inscripcion.html', {'form': form, })

def activate(request, inscripto_id, token):
    try:
        inscripto = Inscriptos.objects.get(pk=inscripto_id)
    except(TypeError, ValueError, OverflowError, Inscriptos.DoesNotExist):
        inscripto = None
    if inscripto is not None and account_activation_token.check_token(inscripto, token):
        inscripto.activo = True
        inscripto.save()
        return HttpResponse('Excelente! Su inscripcion fue validada.')
    else:
        return HttpResponse('El link de activacion es invalido!')