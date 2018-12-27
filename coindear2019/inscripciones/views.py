from django.shortcuts import render
from django.http import HttpResponse
#Import Personales
from .models import Inscriptos
from .ModelForm import InscriptoForm
# Create your views here.
def inscripcion(request):
    form = InscriptoForm()
    return render(request, 'inscripcion.html', {'form': form, })