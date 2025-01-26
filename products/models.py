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


class Drawing(models.Model):
    # Ссылка на основной документ
    main_document = models.ForeignKey(
        'MainDocument',
        on_delete=models.CASCADE,
        related_name='drawings',
        null=True,
        blank=True  # Основной документ может быть необязательным
    )

    # Ссылка на родительский чертеж
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True,  # Родительский документ может быть необязательным
        verbose_name="Родительский чертеж"
    )

    doc_name = models.CharField(max_length=255, null=False, blank=False, default="Untitled")
    mass = models.FloatField()
    assembly_unit = models.BooleanField(default=False, verbose_name="СБ")

    def clean(self):
        # Если основной документ отсутствует, то либо название, либо родитель должны быть заполнены
        if not self.main_document and not self.parent:
            raise ValidationError(
                "Чертеж должен быть связан либо с основным документом, либо с родительским чертежом."
            )

    def __str__(self):
        return f"{self.doc_name} ({self.id})"

    class Meta:
        verbose_name = "Чертеж"
        verbose_name_plural = "Чертежи"


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


