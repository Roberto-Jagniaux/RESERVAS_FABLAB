# Generated by Django 4.1 on 2023-11-26 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bloque', '0003_remove_reserva_idstock_reserva_idstock'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='bloque',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bloque.bloque'),
        ),
    ]
