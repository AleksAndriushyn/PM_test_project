from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    image = models.ImageField(upload_to='screws/images', blank=True)

    def __str__(self):
        return self.name


class Subgroup(models.Model):
    category = models.CharField(max_length=10)
    name = models.CharField(max_length=100)


class Subsubgroup(models.Model):
    sub_group = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=10)


class Screw(models.Model):
    category = models.ForeignKey(Category, related_name='screws', on_delete=models.CASCADE)

    name = models.CharField(max_length=200, verbose_name="Screw name")
    group_standard = models.IntegerField(verbose_name='Standard (group)', null=True)
    image = models.ImageField(upload_to='screws/images', blank=True)
    head = models.CharField(max_length=200, verbose_name="Head")
    material = models.CharField(max_length=50, verbose_name='Material')
    coating = models.CharField(max_length=50, verbose_name='Coating')
    length = models.CharField(max_length=50, verbose_name='Length, mm')
    diameter = models.CharField(max_length=50, verbose_name='Diameter, mm')
    carving_type = models.CharField(max_length=100, verbose_name='Carving')
    field_of_use = models.CharField(max_length=100, verbose_name='Usage')
    bit_size = models.CharField(max_length=50, verbose_name='Bit size')
    base = models.CharField(max_length=50, verbose_name='For what base')
    spline = models.CharField(max_length=50, verbose_name='Spline')
    sub_group = models.CharField(max_length=10)
    subsub_group = models.CharField(max_length=10)

    def __str__(self):
        return self.name
