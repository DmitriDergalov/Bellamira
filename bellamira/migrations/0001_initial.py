# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('set', models.TextField()),
                ('renter_info', models.TextField()),
                ('event_date', models.DateField()),
                ('event_info', models.TextField()),
                ('price', models.SmallIntegerField()),
                ('giving_date', models.DateField()),
                ('return_date', models.DateField()),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Suit',
            fields=[
                ('code', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
                ('style', models.CharField(max_length=20)),
                ('sizes', models.CommaSeparatedIntegerField(max_length=20)),
                ('description', models.TextField()),
                ('sebest', models.PositiveIntegerField()),
                ('person', models.CharField(max_length=40)),
                ('default_rent_price', models.SmallIntegerField()),
                ('rent_price_partners', models.SmallIntegerField()),
                ('rent_price_students', models.SmallIntegerField()),
                ('rent_price_person', models.SmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='rent',
            name='suit',
            field=models.ForeignKey(to='bellamira.Suit'),
        ),
        migrations.AddField(
            model_name='accessory',
            name='suits',
            field=models.ManyToManyField(to='bellamira.Suit'),
        ),
    ]
