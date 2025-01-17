from django.db import models
from orders.models import Task
from materials.models import SheetForm, RodForm


class Drawing(models.Model):
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children'
    )
    mass = models.FloatField()
    assembly_unit = models.CharField(max_length=255)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.assembly_unit} ({self.id})"


class DrawingSheet(models.Model):
    drawing = models.ForeignKey(
        Drawing,
        on_delete=models.CASCADE,
        related_name='sheets'
    )
    file = models.FileField(upload_to='drawings/')
    sheet_number = models.PositiveIntegerField()  # Номер листа

    def __str__(self):
        return f"Sheet {self.sheet_number} of Drawing {self.drawing.id}"


class Product(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    drawing = models.ForeignKey(Drawing, null=True, blank=True, on_delete=models.CASCADE)
    rod_blank = models.ForeignKey(RodForm, null=True, blank=True, on_delete=models.SET_NULL)
    sheet_blank = models.ForeignKey(SheetForm, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    quantity_in_task = models.IntegerField()
    quantity_to_produce = models.IntegerField(null=True, blank=True)

class TaskProduct(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
