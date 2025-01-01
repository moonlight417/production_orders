from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
# from .serializers import ProductSerializer

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
