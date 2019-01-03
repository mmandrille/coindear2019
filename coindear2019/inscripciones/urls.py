from django.conf.urls import url
from django.urls import path
#Import de modulos personales
from . import views

app_name = 'inscripciones'
urlpatterns = [
    url(r'^$', views.inscripcion, name='inscripcion'),
    url(r'^activate/(?P<inscripto_id>[0-9]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
    path('test_mail/<int:msj_id>', views.test_mail, name='test_mail'),
]