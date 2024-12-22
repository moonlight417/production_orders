from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=15, unique=True)  # Название роли
    password = models.CharField(max_length=10)  # Хэшированный пароль

    def __str__(self):
        return self.name

class Employee(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    position = models.CharField(max_length=20)
