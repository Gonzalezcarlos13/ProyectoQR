# Generated by Django 4.2.7 on 2023-11-29 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoMovil', '0004_alumno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencias',
            name='clases',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='proyectoMovil.clases'),
        ),
        migrations.AlterField(
            model_name='clases',
            name='seccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='proyectoMovil.seccion'),
        ),
        migrations.AlterField(
            model_name='seccion',
            name='profesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='proyectoMovil.profesores'),
        ),
    ]
