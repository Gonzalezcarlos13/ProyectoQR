# Generated by Django 4.2.7 on 2023-11-24 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoMovil', '0002_alter_asistencias_table_alter_clases_table_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesores',
            name='apellido',
            field=models.CharField(max_length=100),
        ),
    ]
