# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib import messages
from django.core import serializers
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from food_Data.forms import EntryForm
from food_Data.models import Recipe


# from rest_framework import serializers


def entry_view(request):
    form = EntryForm()
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully stored")
            form = EntryForm()
    return render(request, 'entry_form.html', {'form': form})


# class RecipeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Recipe
#         fields = '__all__'


class GetData(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        data = serializers.serialize('json', recipes)
        data = json.loads(data)
        return Response(data)
