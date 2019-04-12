# Generated by Django 2.1.3 on 2019-03-21 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0019_auto_20190321_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensajes',
            name='id',
        ),
        migrations.RemoveField(
            model_name='progress_links',
            name='mensaje',
        ),
        migrations.AddField(
            model_name='mensajes',
            name='progress_url',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='inscripciones.Progress_Links'),
            preserve_default=False,
        ),
    ]