from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Task
# from .serializers import CustomerSerializer, TaskSerializer
from products.models import Product
from django.db.models import Q

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

        # # Обновляем счетчик новых заданий
        # task_counter, _ = TaskCounter.objects.get_or_create(id=1)  # Предполагаем, что у нас только один счетчик
        # task_counter.count += 1
        # task_counter.save()

        return Response({
            "customer_id": customer.id,
            "task_id": task.id,
            "message": "Данные заказчика и задания успешно сохранены."
        }, status=status.HTTP_201_CREATED)

    def get(self, request):
        # Фильтрация заданий по параметрам
        tasks = Task.objects.all()

        # Фильтры для поиска заданий
        customer_id = request.query_params.get("customer_id")
        invoice_number = request.query_params.get("invoice_number")
        order_date = request.query_params.get("order_date")

        if customer_id:
            tasks = tasks.filter(customer_id=customer_id)
        if invoice_number:
            tasks = tasks.filter(invoice_number__icontains=invoice_number)
        if order_date:
            tasks = tasks.filter(order_invoice_date=order_date)

        # Формирование ответа с данными заданий
        task_list = [{
            "task_id": task.id,
            "invoice_number": task.invoice_number,
            "order_invoice_date": task.order_invoice_date,
            "customer_name": task.customer.organization_name
        } for task in tasks]

        return Response({
            "tasks": task_list
        }, status=status.HTTP_200_OK)


class CustomerDataView(APIView):
    def get(self, request):
        customer_name = request.query_params.get("name", "").strip()
        if not customer_name:
            return Response({"error": "Имя заказчика не указано."}, status=400)

        try:
            customer = Customer.objects.get(organization_name__iexact=customer_name)
            tasks = Task.objects.filter(customer=customer)
            data = []
            for task in tasks:
                products = Product.objects.filter(task=task)
                products_data = [
                    {"name": product.name, "quantity": product.quantity_in_task} for product in products
                ]
                data.append({
                    "task_id": task.id,
                    "invoice_number": task.invoice_number,
                    "order_date": task.order_invoice_date,
                    "customer_name": customer.organization_name,
                    "products": products_data,
                })
            return Response(data, status=200)
        except Customer.DoesNotExist:
            return Response({"error": "Заказчик не найден."}, status=404)


class StartTaskView(APIView):
    def post(self, request, task_id):
        # Получаем задание
        task = Task.objects.get(id=task_id)

        # # Уменьшаем счетчик новых заданий
        # task_counter = TaskCounter.objects.get(id=1)
        # if task_counter.count > 0:
        #     task_counter.count -= 1
        #     task_counter.save()

        # Логика для начала работы над заданием
        # ...

        return Response({"message": "Задание начато."}, status=status.HTTP_200_OK)

# class TaskCounterView(APIView):
#     def get(self, request):
#         task_counter = TaskCounter.objects.get(id=1)  # Предполагаем, что у нас только один счетчик
#         return Response({"count": task_counter.count}, status=status.HTTP_200_OK)


class NewTasksView(APIView):
    def get(self, request):
        # Получаем новые задания из базы данных
        new_tasks = Task.objects.filter(status='new')  # Предполагаем, что у вас есть поле status
        tasks_data = []

        for task in new_tasks:
            # Получаем данные о заказчике
            customer_name = task.customer.organization_name if task.customer else "Неизвестно"

            # Получаем данные о продуктах
            products = Product.objects.filter(task=task)
            products_data = [{'name': product.name, 'quantity': product.quantity_in_task} for product in products]

            # Формируем данные о задании
            tasks_data.append({
                'id': task.id,  # Добавляем ID задания
                'invoice_number': task.invoice_number,
                'customer_name': customer_name,
                'order_invoice_date': task.order_invoice_date,
                'products': products_data
            })

        return Response(tasks_data)

class UpdateTaskStatusView(APIView):
    def post(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
            task.status = 'opened'  # Изменяем статус на 'opened'
            task.save()
            return Response({"message": "Статус задания обновлен."}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"error": "Задание не найдено."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)