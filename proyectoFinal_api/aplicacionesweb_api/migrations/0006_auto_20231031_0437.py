# Generated by Django 2.2 on 2023-10-31 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacionesweb_api', '0005_auto_20231030_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='hora_final',
            field=models.TimeField(verbose_name='%H:%M'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='hora_inicio',
            field=models.TimeField(verbose_name='%H:%M'),
        ),
    ]
