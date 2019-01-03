# Generated by Django 2.1.3 on 2019-01-03 18:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0016_mensajes_progress_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progress_Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarea', models.CharField(max_length=50, verbose_name='Tarea')),
                ('inicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('progress_url', models.URLField(blank=True, null=True, verbose_name='Web')),
            ],
        ),
    ]
