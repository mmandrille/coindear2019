from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
#Task Manager Models
from background_task.models import Task as bg_Tasks
from background_task.models_completed import CompletedTask as bg_CompletedTask
#decoradores
from django.contrib.admin.views.decorators import staff_member_required

#Import Personales
from .models import Inscriptos, Mensajes
from .ModelForm import InscriptoForm
from .tokens import account_activation_token
from .tasks import crear_mails, crear_progress_link

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
            return render(request, 'resultado.html', {'texto': 'Por Favor Confirme la creacion de su cuenta en el correo que recibio', })
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
        return render(request, 'resultado.html', {'texto': 'Excelente! Su inscripcion fue validada.', })
    else:
        return render(request, 'resultado.html', {'texto': 'El link de activacion es invalido!', })

def test_mail(request, msj_id):
    mail = Mensajes.objects.get(pk=msj_id)
    return render(request, 'email_base.html', {'mensaje': mail, })

@staff_member_required
def upload_csv_mails(request):
    count = 0
    data = {}
    if "GET" == request.method:
        return render(request, "upload_csv.html", data)
    # if not GET, then proceed
    csv_file = request.FILES["csv_file"]
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'File is not CSV type')
        return HttpResponseRedirect(reverse("inscripciones:upload_csv"))
        #if file is too large, return
    if csv_file.multiple_chunks():
        messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
        return HttpResponseRedirect(reverse("inscripciones:upload_csv"))
        
    file_data = csv_file.read().decode("utf-8")
    lines = file_data.split("\n")
    #loop over the lines and save them in db. If error , store as string and then display
    #llamar funcion cada 100 mails.
    count = 0
    new_queue = crear_progress_link("CrearMails:"+str(datetime.now()).replace(" ", ">")[0:16])
    while (count + 100) < len(lines):
        crear_mails(lines[count:count+100], schedule=int(count/10), queue=new_queue)
        count+=100
    crear_mails(lines[count:len(lines)], schedule=int(count/10), queue=new_queue)
    return render(request, 'upload_csv.html', {'count': len(lines), 'new_queue': new_queue })

def task_progress(request, queue_name):
    tareas_en_progreso = bg_Tasks.objects.filter(queue= queue_name)
    tareas_terminadas = bg_CompletedTask.objects.filter(queue= queue_name)
    return render(request, 'task_progress.html', {'tarea_queue': queue_name, 
                                                'tareas_totales': (len(tareas_en_progreso)+len(tareas_terminadas)) ,
                                                'tareas_en_cola': len(tareas_en_progreso), 
                                                'tareas_terminadas': len(tareas_terminadas),
                                                "refresh": True })

@staff_member_required
def mostrar_inscriptos(request):
    tipo_usuario = [True, False]
    inscriptos = Inscriptos.objects.all().order_by('-apellido')
    return render(request, 'inscriptos.html', {'inscriptos': inscriptos, 'tipo_usuario': tipo_usuario })
