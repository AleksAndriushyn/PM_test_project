from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    image = models.ImageField(upload_to='screws/images', blank=True)

    def __str__(self):
        return self.name


class Subgroup(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subsubgroup(models.Model):
    sub_group = models.ForeignKey(Subgroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Screw(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

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
    sub_group = models.ForeignKey(Subgroup, on_delete=models.CASCADE, null=True)
    subsub_group = models.ForeignKey(Subsubgroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
