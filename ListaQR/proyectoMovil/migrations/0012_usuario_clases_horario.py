# Generated by Django 4.2.7 on 2023-12-06 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoMovil', '0011_clases_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='clases',
            name='horario',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
