# Generated by Django 4.1 on 2023-11-26 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bloque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bloque',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estados', models.CharField(choices=[('Reservado', 'Reservado'), ('Disponible', 'Disponible'), ('No Disponible', 'No Disponible')], default='No Disponible', max_length=15)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='reserva',
            fields=[
                ('idR', models.AutoField(primary_key=True, serialize=False)),
                ('nomA', models.CharField(max_length=25)),
                ('correo', models.CharField(max_length=50)),
                ('idB', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bloque.bloque')),
            ],
        ),
        migrations.CreateModel(
            name='stock',
            fields=[
                ('idE', models.AutoField(primary_key=True, serialize=False)),
                ('nomE', models.CharField(max_length=50)),
                ('cantE', models.CharField(max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='date',
        ),
        migrations.AddField(
            model_name='reserva',
            name='idStock',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bloque.stock'),
        ),
    ]
