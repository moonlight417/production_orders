from django.db import models
from employees.models import Employee


class Customer(models.Model):
    organization_name = models.CharField(max_length=255)

class Task(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_invoice_date = models.DateField()
    invoice_number = models.CharField(max_length=255)

class Order(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    order_date = models.DateField()
    production_acceptance_date = models.DateField(null=True, blank=True)
    order_file = models.FileField(upload_to='orders/')
    label_file = models.FileField(upload_to='labels/', null=True, blank=True)

class TaskEmployee(models.Model):
    order = models.ForeignKey(Task, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


