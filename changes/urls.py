from django.urls import path
from . import views

urlpatterns = [
    path('', views.changes_1, name='changes'),
]