from django.urls import path
from .views import AddTaskView, AddCustomerView

urlpatterns = [
    path('add_task/', AddTaskView.as_view(), name='add_task'),
    path('add_customer/', AddCustomerView.as_view(), name='add_customer')
]