from django.db import models
from orders.models import Task
from materials.models import SheetForm, RodForm


# class Tag(models.Model):
#     name = models.CharField(max_length=50, unique=True)  # Уникальное название тега
#
#     def __str__(self):
#         return self.name
#
#
# class Drawing(models.Model):
#     parent = models.ForeignKey(
#         'self',
#         null=True,
#         blank=True,
#         on_delete=models.CASCADE,
#         related_name='children'
#     )
#     doc_name = models.CharField(max_length=255, null=False, blank=False, default="Untitled")
#     mass = models.FloatField()
#     assembly_unit = models.BooleanField(default=False, verbose_name="СБ")
#     comment = models.TextField(null=True, blank=True)
#     tags = models.ManyToManyField('Tag', related_name='drawings', blank=True)  # Связь с тегами
#
#     def __str__(self):
#         return f"{self.assembly_unit} ({self.id})"
#
#
# class DrawingSheet(models.Model):
#     drawing = models.ForeignKey(
#         'Drawing',
#         on_delete=models.CASCADE,
#         related_name='sheets'
#     )
#     file = models.FileField(upload_to='drawings/')
#     sheet_number = models.PositiveIntegerField()  # Номер листа
#     is_actual = models.BooleanField(default=True, verbose_name="Актуальность")  # Поле актуальности
#
#     def __str__(self):
#         return f"Sheet {self.sheet_number} of Drawing {self.drawing.id}"

# Модель для главного документа
from django.core.exceptions import ValidationError
from django.db import models


# Модель для основного документа
class MainDocument(models.Model):
    main_name = models.CharField(max_length=255, null=False, blank=False, default="Untitled")
    comment = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', related_name='main_documents', blank=True)  # Связь с тегами

    def __str__(self):
        return self.main_name


# Модель для тегов
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Уникальное название тега

    def __str__(self):
        return self.name


# Модель для чертежей
class Drawing(models.Model):
    main_document = models.ForeignKey(
        'MainDocument',
        on_delete=models.CASCADE,
        related_name='drawings',
        null=True
    )

    # Метод для проверки корректности данных
    def clean(self):
        # Валидация: если нет связанного документа, то должно быть заполнено название чертежа
        if self.main_document is None and not self.doc_name:
            raise ValidationError("Документ должен иметь связанный основной документ или название.")

    doc_name = models.CharField(max_length=255, null=False, blank=False, default="Untitled")
    mass = models.FloatField()
    assembly_unit = models.BooleanField(default=False, verbose_name="СБ")

    def __str__(self):
        return f"{self.doc_name} ({self.id})"


# Модель для листов чертежей
class DrawingSheet(models.Model):
    drawing = models.ForeignKey(
        'Drawing',
        on_delete=models.CASCADE,
        related_name='sheets'
    )
    file = models.FileField(upload_to='drawings/')
    sheet_number = models.PositiveIntegerField()  # Номер листа
    is_actual = models.BooleanField(default=True, verbose_name="Актуальность")  # Поле актуальности

    def __str__(self):
        return f"Sheet {self.sheet_number} of Drawing {self.drawing.doc_name}"

class Product(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    drawing = models.ForeignKey(MainDocument, null=True, blank=True, on_delete=models.CASCADE)
    rod_blank = models.ForeignKey(RodForm, null=True, blank=True, on_delete=models.SET_NULL)
    sheet_blank = models.ForeignKey(SheetForm, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    quantity_in_task = models.IntegerField()
    quantity_to_produce = models.IntegerField(null=True, blank=True)


class TaskProduct(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


