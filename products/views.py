from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
# from .serializers import ProductSerializer
from orders.models import Task  # Проверка существования задания

class AddProductView(APIView):
    def post(self, request):
        data = request.data
        task_id = data.get("task_id")
        name = data.get("name")
        quantity = data.get("quantity")

        if not all([task_id, name, quantity]):
            return Response({"error": "Поля продукта обязательны."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            quantity = int(quantity)
        except ValueError:
            return Response({"error": "Количество должно быть числом."}, status=status.HTTP_400_BAD_REQUEST)

        # Создаём продукт
        product = Product.objects.create(task_id=task_id, name=name, quantity_in_task=quantity)

        return Response({
            "product_id": product.id,
            "message": "Продукт успешно добавлен."
        }, status=status.HTTP_201_CREATED)

    def get(self, request):
        # Получение списка продуктов по заданию
        task_id = request.query_params.get("task_id")

        if not task_id:
            return Response({"error": "task_id обязательно."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"error": "Задание с таким ID не существует."}, status=status.HTTP_404_NOT_FOUND)

        # Получаем все продукты для указанного задания
        products = Product.objects.filter(task=task)

        product_list = [{
            "product_id": product.id,
            "name": product.name,
            "quantity_in_task": product.quantity_in_task
        } for product in products]

        return Response({
            "task_id": task.id,
            "products": product_list
        }, status=status.HTTP_200_OK)
