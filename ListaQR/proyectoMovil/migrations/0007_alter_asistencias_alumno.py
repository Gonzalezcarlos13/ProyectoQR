# Generated by Django 4.2.7 on 2023-11-29 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoMovil', '0006_alter_alumno_table_alter_asistencias_table_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencias',
            name='alumno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='proyectoMovil.profesores'),
        ),
    ]
