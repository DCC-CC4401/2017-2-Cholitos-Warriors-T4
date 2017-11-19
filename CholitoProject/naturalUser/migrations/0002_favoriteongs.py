# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-19 00:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0002_auto_20171118_2141'),
        ('naturalUser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteONGs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ongs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ong.ONG')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naturalUser.NaturalUser')),
            ],
        ),
    ]
