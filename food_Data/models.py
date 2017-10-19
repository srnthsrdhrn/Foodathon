# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.


class Recipe(models.Model):
    states = ((0, "Andhra Pradesh"), (1, "Arunachal Pradesh"),
              (2, "Assam"),
              (3, "Bihar"),
              (4, "Chhattisgarh"),
              (5, "Chandigarh"),
              (6, "Dadra and Nagar Haveli"),
              (7, "Daman and Diu"),
              (8, "Delhi"),
              (9, "Goa"),
              (10, "Gujarat"),
              (11, "Haryana"),
              (12, "Himachal Pradesh"),
              (13, "Jammu and Kashmir"),
              (14, "Jharkhand"),
              (15, "Karnataka"),
              (16, "Kerala"),
              (17, "Madhya Pradesh"),
              (18, "Maharashtra"),
              (19, "Manipur"),
              (20, "Meghalaya"),
              (21, "Mizoram"),
              (22, "Nagaland"),
              (23, "Orissa"),
              (24, "Punjab"),
              (25, "Pondicherry"),
              (26, "Rajasthan"),
              (27, "Sikkim"),
              (29, "Tamil Nadu"),
              (28, "Tripura"),
              (29, "Uttar Pradesh"),
              (30, "Uttarakhand"),
              (31, "West Bengal"),)
    cuisines = ((0, "Traditional"), (1, "Lost"), (2, "Continental"))
    name = models.CharField(max_length=1000)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True)
    recipe = RichTextField(blank=True, null=True)
    benefits = RichTextField(blank=True, null=True)
    cuisine = models.IntegerField(choices=cuisines)
    state = models.IntegerField(choices=states)
