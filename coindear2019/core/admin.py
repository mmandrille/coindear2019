from django.contrib import admin

#Incluimos modelos
from .models import Faq, Texto
# Register your models here.
admin.site.register(Texto)
admin.site.register(Faq)