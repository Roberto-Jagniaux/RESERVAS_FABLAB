# Generated by Django 4.1 on 2023-11-26 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloque', '0006_remove_stock_cante'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bloque',
            old_name='idstock',
            new_name='idE',
        ),
    ]
