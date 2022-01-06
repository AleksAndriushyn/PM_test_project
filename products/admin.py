from django.contrib import admin
from . import models

admin.site.register(models.Screw)
admin.site.register(models.Category)
admin.site.register(models.Subgroup)
admin.site.register(models.Subsubgroup)
