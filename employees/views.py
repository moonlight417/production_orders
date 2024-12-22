from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Role
from .serializers import RolePasswordSerializer
from rest_framework import status
from django.contrib.auth.hashers import check_password





class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class CheckPasswordView(APIView):
    def post(self, request, role):
        print(f"Полученная роль: {role}, Полученный пароль: {request.data.get('password')}")  # Отладка

        try:
            role_instance = Role.objects.get(name=role)
        except Role.DoesNotExist:
            print("Роль не найдена")  # Отладка
            return Response({"error": "Role not found"}, status=status.HTTP_404_NOT_FOUND)

        entered_password = request.data.get('password')
        if entered_password == role_instance.password:  # Используем простое сравнение для тестирования
            return Response({"success": "Password is correct!"}, status=status.HTTP_200_OK)
        else:
            print("Пароль неверный")  # Отладка
            return Response({"error": "Incorrect password"}, status=status.HTTP_401_UNAUTHORIZED)

        # Проверяем пароль
        if check_password(entered_password, role_obj.password):
            return Response({"success": "Password is correct!"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Incorrect password"}, status=status.HTTP_401_UNAUTHORIZED)