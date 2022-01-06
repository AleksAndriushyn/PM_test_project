from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from .models import Screw, Category, Subgroup, Subsubgroup
from django.shortcuts import render
from django.shortcuts import get_object_or_404


class CategoriesList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoriesSerializer


class CategoriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoriesSerializer


class ScrewsList(generics.ListCreateAPIView):
    queryset = Screw.objects.all()
    serializer_class = serializers.ScrewSerializer


class ScrewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Screw.objects.all()
    serializer_class = serializers.ScrewSerializer


def get_screw_categories(request):
    category = Category.objects.all()
    return render(request, "screws/allscrews.html", {"categories": category})


def select_group(request):
    id = request.GET.get('id')
    subgroup_screws = Screw.objects.filter(sub_group=id).values('id', 'name', 'material', 'coating', 'head', 'spline',
                                               'bit_size', 'carving_type', 'field_of_use', 'base', 'diameter',
                                               'length', 'image', 'sub_group', 'subsub_group')
    category = subgroup_screws[0]['sub_group']
    subgroup_name = Subgroup.objects.filter(id=category).values('id', 'category', 'name')[0]['name']
    category_name = Category.objects.filter(id=id).values('id', 'name')[0]['name']
    return render(request, "screws/selectedgroup.html",
                  {"screws": subgroup_screws, 'category_name': category_name, 'subgroup_name': subgroup_name})


def select_screw(request):
    id = request.GET.get('id')
    screw = Screw.objects.filter(id=id).values('id', 'name', 'group_standard', 'material', 'coating', 'head', 'spline',
                                               'bit_size', 'carving_type', 'field_of_use', 'base', 'diameter',
                                               'length', 'image', 'sub_group', 'subsub_group')
    category = screw[0]['sub_group']
    subgroup_category_name = Category.objects.filter(id=category).values('id', 'name')[0]['name']
    subgroup_name = Subgroup.objects.filter(id=category).values('id', 'category', 'name')[0]['name']
    subsub_name = Subsubgroup.objects.filter(id=category).values('id', 'category', 'name')[0]['name']
    return render(request, "screws/selectedscrew.html",
                  {"screws": screw, 'category_name': subgroup_category_name, 'subgroup_name': subgroup_name,
                   'subsub_name': subsub_name})
