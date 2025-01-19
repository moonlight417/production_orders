from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Drawing

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

    from rest_framework.views import APIView
    from rest_framework.response import Response
    from rest_framework import status
    from .models import Drawing

    class AddDrawingView(APIView):
        def post(self, request):
            data = request.data
            doc_name = data.get("doc_name")
            parent_id = data.get("parent")  # ID родителя
            mass = data.get("mass")
            comment = data.get("comment", "")  # По умолчанию пустая строка
            assembly_unit = data.get("assembly_unit", False)  # По умолчанию False

            # Проверка обязательных полей
            if not doc_name or not mass:
                return Response({
                    "error": "Поля 'doc_name' и 'mass' обязательны.",
                    "doc_name": doc_name,
                    "mass": mass,
                }, status=status.HTTP_400_BAD_REQUEST)

            # Получение объекта родителя (если указан)
            parent = None
            if parent_id:
                try:
                    parent = Drawing.objects.get(id=parent_id)
                except Drawing.DoesNotExist:
                    return Response({
                        "error": f"Родитель с ID {parent_id} не найден."
                    }, status=status.HTTP_400_BAD_REQUEST)

            # Создание чертежа
            drawing = Drawing.objects.create(
                doc_name=doc_name,
                parent=parent,
                mass=mass,
                comment=comment,
                assembly_unit=assembly_unit,
            )

            return Response({
                "drawing_id": drawing.id,
                "message": "Данные чертежа успешно сохранены."
            }, status=status.HTTP_201_CREATED)

