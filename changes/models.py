from django.db import models


class Change(models.Model):
    order = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    change_number = models.IntegerField()
    change_date = models.DateField()
    description = models.TextField()

# class Status(models.Model):
#     name = models.CharField(max_length=255)
#     color = models.CharField(max_length=7)


