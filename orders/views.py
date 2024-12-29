from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializer, CustomerSerializer
from .models import Order

class AddTaskView(APIView):
    def post(self, request):
        print("Request data:", request.data, flush=True)  # Убедитесь, что данные поступают
        try:
            invoice_number = request.data.get('invoice_number')
            order_invoice_date = request.data.get('order_invoice_date')
            print("Extracted invoice_number:", invoice_number, flush=True)

            data = {
                'invoice_number': invoice_number,
                'order_invoice_date': order_invoice_date,
            }

            serializer = TaskSerializer(data=data)
            print("Serializer data:", serializer.initial_data, flush=True)

            if serializer.is_valid():
                serializer.save()
                print("Data saved successfully!", flush=True)
                return Response({"message": "Task added successfully!"}, status=status.HTTP_201_CREATED)
            else:
                print("Serializer errors:", serializer.errors, flush=True)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("Error:", str(e), flush=True)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddCustomerView(APIView):
    def post(self, request):
        organization_name = request.data.get['organization_name']

        # data = request.data.get('data_customer')


        data = {'organization_name': organization_name,}
        print(data)

        serializer = CustomerSerializer(data=data)

        if serializer.is_valid():  # Проверка данных
            serializer.save()  # Сохраняем данные в базе данных
            return Response({"message": "Customer added successfully!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

