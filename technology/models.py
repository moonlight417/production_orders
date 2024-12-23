from django.db import models
from materials.models import RodForm
from materials.models import SheetForm
from products.models import Product

class ManufacturingOperation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sequence_number = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()

class RodBlank(models.Model):
    rod_form = models.ForeignKey(RodForm, on_delete=models.CASCADE)
    blank_length = models.FloatField()
    part_length = models.FloatField()
    complex_blank = models.BooleanField(default=False)
    total_bars = models.IntegerField()
    extra_length = models.FloatField(null=True, blank=True)
    usage_rate = models.FloatField()

class SheetBlank(models.Model):
    sheet_form = models.ForeignKey(SheetForm, on_delete=models.CASCADE)
    part_length = models.FloatField()
    part_width = models.FloatField()
    total_sheets = models.IntegerField()
    extra_length = models.FloatField(null=True, blank=True)
    extra_width = models.FloatField(null=True, blank=True)
    usage_rate = models.FloatField()
