# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0054_realm_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='size',
            field=models.IntegerField(null=True),
        ),
    ]
