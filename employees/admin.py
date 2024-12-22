from django.contrib import admin
from . import models
from .models import Role

admin.site.register(models.Employee)
admin.site.register(Role)