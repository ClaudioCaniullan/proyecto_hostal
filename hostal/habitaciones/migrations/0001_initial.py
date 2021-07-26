# Generated by Django 2.2.24 on 2021-07-26 21:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('estado', models.CharField(choices=[('D', 'Disponible'), ('O', 'Ocupado'), ('M', 'En Mantencion')], default='D', max_length=1)),
                ('image', models.ImageField(upload_to='habitaciones')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rutUsuario', models.CharField(default=None, max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(9, 'Ingresar dni en el siguiente formato 77111666-5'), django.core.validators.MaxLengthValidator(10, 'Ingresar dni en el siguiente formato 77111666-5')])),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('password2', models.CharField(max_length=10)),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habitaciones.Habitaciones')),
            ],
        ),
    ]
