# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerary',
            name='year',
            field=models.SmallIntegerField(default='2017'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='geopoint',
            name='itinerary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='geoPoints', to='api.Itinerary'),
        ),
        migrations.AlterField(
            model_name='note',
            name='geoPoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='api.GeoPoint'),
        ),
    ]
