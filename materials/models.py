from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=25)
    density = models.FloatField()
    standard = models.CharField(max_length=25)  # ГОСТ
    website_link = models.URLField()

class RodForm(models.Model):
    material = models.ForeignKey('Material', on_delete=models.CASCADE)
    section_shape = models.CharField(max_length=20)
    section_size1 = models.FloatField()
    section_size2 = models.FloatField(null=True, blank=True)
    bar_length = models.FloatField()
    standard = models.CharField(max_length=25)  # ГОСТ на прокат

class SheetForm(models.Model):
    material = models.ForeignKey('Material', on_delete=models.CASCADE)
    standard = models.CharField(max_length=25)  # ГОСТ
    thickness = models.FloatField()
    length = models.FloatField()
    width = models.FloatField()