from rest_framework import serializers
from .models import Customer, Task

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'organization_name']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'customer', 'order_invoice_date', 'invoice_number']


# from rest_framework import serializers
# from .models import Task, Customer
# from products.serializers import ProductSerializer
#
#
#
# class TaskSerializer(serializers.ModelSerializer):
#     # products = ProductSerializer(many=True, read_only=True)  # Привязанные продукты
#
#     class Meta:
#         model = Task
#         fields = ['order_invoice_date', 'invoice_number']
#
# class CustomerSerializer(serializers.ModelSerializer):
#     tasks = TaskSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Customer
#         fields = ['organization_name']
#
#
