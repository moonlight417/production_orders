from django.urls import path
from .views import AddCustomerAndTaskView, CustomerDataView

urlpatterns = [
    path('add_customer_and_task/', AddCustomerAndTaskView.as_view(), name='add_customer_and_task'),
    path('customer_data/', CustomerDataView.as_view(), name='customer_data'),
]