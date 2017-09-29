# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.


class Recipe(models.Model):
    cuisines = ((0, "Traditional"), (1, "Lost"), (2, "Continental"))
    name = models.CharField(max_length=1000)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True)
    recipe = RichTextField(blank=True, null=True)
    benefits = RichTextField(blank=True, null=True)
    cuisine = models.IntegerField(choices=cuisines)
    state = models.CharField(max_length=500, null=True, blank=True)
