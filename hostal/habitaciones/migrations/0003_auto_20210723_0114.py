# Generated by Django 2.2.24 on 2021-07-23 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitaciones', '0002_habitaciones_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitaciones',
            name='estado',
            field=models.CharField(choices=[('D', 'Disponible'), ('O', 'Ocupado'), ('M', 'En Mantencion')], default='D', max_length=1),
        ),
    ]
