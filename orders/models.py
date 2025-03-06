from django.db import models
from employees.models import Employee


class Customer(models.Model):
    organization_name = models.CharField(max_length=255)

from django.db import models

class Task(models.Model):
    invoice_number = models.CharField(max_length=100)
    order_invoice_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('new', 'New'), ('opened', 'Opened')], default='new')

class Order(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    order_date = models.DateField()
    production_acceptance_date = models.DateField(null=True, blank=True)
    order_file = models.FileField(upload_to='orders/')
    label_file = models.FileField(upload_to='labels/', null=True, blank=True)
    status = models.CharField(max_length=1, null=True, blank=True)

class TaskEmployee(models.Model):
    order = models.ForeignKey(Task, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)



