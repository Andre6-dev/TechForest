# Generated by Django 3.2.9 on 2021-12-05 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_rename_planes_id_pagos_planes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diapositivos',
            old_name='usuario_id',
            new_name='usuarios',
        ),
        migrations.RenameField(
            model_name='errores',
            old_name='usuario_id',
            new_name='usuarios',
        ),
        migrations.RenameField(
            model_name='opciones',
            old_name='diapositivos_id',
            new_name='diapositivos',
        ),
        migrations.RenameField(
            model_name='valvula',
            old_name='diapositivos_id',
            new_name='diapositivos',
        ),
    ]
