# Generated by Django 4.1 on 2023-11-28 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-id'], 'verbose_name': 'perfil', 'verbose_name_plural': 'perfiles'},
        ),
    ]
