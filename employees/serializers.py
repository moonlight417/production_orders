from rest_framework import serializers
from .models import Employee
from .models import Role

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'role', 'last_name', 'first_name', 'middle_name', 'position']

class RolePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['role', 'password']

class ChangePasswordSerializer(serializers.Serializer):
    role = serializers.CharField(max_length=15)
    current_password = serializers.CharField(max_length=15)
    new_password = serializers.CharField(max_length=15)

