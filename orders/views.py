from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Task
# from .serializers import CustomerSerializer, TaskSerializer

class AddCustomerAndTaskView(APIView):
    def post(self, request):
        data = request.data
        organization_name = data.get("organization_name")
        invoice_number = data.get("invoice_number")
        order_date = data.get("order_date")

        if not all([organization_name, invoice_number, order_date]):
            return Response({
                "error": "Поля заказчика и задания обязательны.",
                "organization_name": organization_name,
                "invoice_number": invoice_number,
                "order_date": order_date,
            }, status=status.HTTP_400_BAD_REQUEST)

        # Создаём заказчика или находим существующего
        customer, _ = Customer.objects.get_or_create(organization_name=organization_name)

        # Создаём задание
        task = Task.objects.create(
            customer=customer,
            invoice_number=invoice_number,
            order_invoice_date=order_date
        )

        return Response({
            "customer_id": customer.id,
            "task_id": task.id,
            "message": "Данные заказчика и задания успешно сохранены."
        }, status=status.HTTP_201_CREATED)


# from django.shortcuts import render
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .serializers import TaskSerializer, CustomerSerializer
# from .models import Order
#
# class AddTaskView(APIView):
#     def post(self, request):
#         try:
#             invoice_number = request.data.get('invoice_number')
#             order_invoice_date = request.data.get('order_invoice_date')
#             data = {
#                 'order_invoice_date': order_invoice_date,
#                 'invoice_number': invoice_number,
#
#             }
#
#             serializer = TaskSerializer(data=data)
#
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({"message": "Task added successfully!"}, status=status.HTTP_201_CREATED)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
# class AddCustomerView(APIView):
#     def post(self, request):
#         organization_name = request.data.get['organization_name']
#
#         # data = request.data.get('data_customer')
#
#
#         data = {'organization_name': organization_name,}
#         print(data)
#
#         serializer = CustomerSerializer(data=data)
#
#         if serializer.is_valid():  # Проверка данных
#             serializer.save()  # Сохраняем данные в базе данных
#             return Response({"message": "Customer added successfully!"}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
