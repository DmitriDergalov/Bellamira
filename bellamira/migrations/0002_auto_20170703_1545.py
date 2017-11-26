# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bellamira', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suit',
            name='default_rent_price',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='suit',
            name='gender',
            field=models.CharField(max_length=1, choices=[(b'M', b'Cavalier'), (b'F', b'Dame')]),
        ),
        migrations.AlterField(
            model_name='suit',
            name='rent_price_partners',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='suit',
            name='rent_price_person',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='suit',
            name='rent_price_students',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='suit',
            name='sebest',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='suit',
            name='sizes',
            field=models.CharField(max_length=5),
        ),
    ]
