# Generated by Django 4.2.7 on 2023-11-30 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoMovil', '0009_alter_asistencias_alumno'),
    ]

    operations = [
        migrations.AddField(
            model_name='clases',
            name='estado',
            field=models.CharField(max_length=50, null=True),
        ),
    ]