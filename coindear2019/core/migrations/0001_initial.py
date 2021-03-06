# Generated by Django 2.1.3 on 2018-12-27 03:46

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField()),
                ('pregunta', models.CharField(max_length=200, verbose_name='Titulo')),
                ('respuesta', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Texto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField()),
                ('texto', tinymce.models.HTMLField()),
            ],
        ),
    ]
