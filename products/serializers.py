from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'task', 'name', 'quantity_in_task']


# from rest_framework import serializers
# from .models import Product
#
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'