#Import Standard
from django.forms import ModelForm
#Import Personales
from .models import Inscriptos

#creamos ModelForm
class InscriptoForm(ModelForm):
    class Meta:
        model = Inscriptos
        fields = ['nombres', 'apellido', 'tipo_doc', 'num_doc', 
                    'pais', 'provincia', 'localidad', 'domicilio',
                    'telefono', 'fax', 'email',
                    'profesion', 'ocupacion', 'cargo', 'lugar_trabajo', 'direccion_laboral',
                    'email_laboral', 'web', 'telefono_laboral',
                    'categoria' ]