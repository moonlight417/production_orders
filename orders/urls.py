from django.urls import path
from .views import AddCustomerAndTaskView

urlpatterns = [
    path('add_customer_and_task/', AddCustomerAndTaskView.as_view(), name='add_customer_and_task'),
]