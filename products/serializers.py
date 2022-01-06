from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Screw, Category, Subgroup, Subsubgroup


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ScrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screw
        fields = ['id', 'category', 'group_standard', 'name', 'material', 'coating', 'head', 'spline', 'bit_size', 'carving_type', 'field_of_use',
                  'base', 'diameter', 'length', 'image', 'sub_group', 'subsub_group']
