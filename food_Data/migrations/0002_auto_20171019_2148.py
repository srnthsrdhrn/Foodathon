# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-19 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_Data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='state',
            field=models.IntegerField(choices=[(0, 'Andhra Pradesh'), (1, 'Arunachal Pradesh'), (2, 'Assam'), (3, 'Bihar'), (4, 'Chhattisgarh'), (5, 'Chandigarh'), (6, 'Dadra and Nagar Haveli'), (7, 'Daman and Diu'), (8, 'Delhi'), (9, 'Goa'), (10, 'Gujarat'), (11, 'Haryana'), (12, 'Himachal Pradesh'), (13, 'Jammu and Kashmir'), (14, 'Jharkhand'), (15, 'Karnataka'), (16, 'Kerala'), (17, 'Madhya Pradesh'), (18, 'Maharashtra'), (19, 'Manipur'), (20, 'Meghalaya'), (21, 'Mizoram'), (22, 'Nagaland'), (23, 'Orissa'), (24, 'Punjab'), (25, 'Pondicherry'), (26, 'Rajasthan'), (27, 'Sikkim'), (29, 'Tamil Nadu'), (28, 'Tripura'), (29, 'Uttar Pradesh'), (30, 'Uttarakhand'), (31, 'West Bengal')], default=0),
            preserve_default=False,
        ),
    ]
