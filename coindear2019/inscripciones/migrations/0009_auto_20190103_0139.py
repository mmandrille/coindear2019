# Generated by Django 2.1.3 on 2019-01-03 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0008_auto_20190102_2356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mails',
            old_name='email_laboral',
            new_name='email',
        ),
    ]
