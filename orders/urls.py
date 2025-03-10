from django.urls import path
from .views import AddCustomerAndTaskView, CustomerDataView, StartTaskView, NewTasksView, \
    UpdateTaskStatusView

urlpatterns = [
    path('add_customer_and_task/', AddCustomerAndTaskView.as_view(), name='add_customer_and_task'),
    path('customer_data/', CustomerDataView.as_view(), name='customer_data'),
    # path('orders/start_task/<int:task_id>/', StartTaskView.as_view(), name='start_task'),
    path('start_task/<int:task_id>/', StartTaskView.as_view(), name='start_task'),  # Добавляем маршрут для StartTaskView,
    # path('task_counter/', TaskCounterView.as_view(), name='task_counter'),
    path('new_tasks/', NewTasksView.as_view(), name='new_tasks'),  # Завершение маршрута для NewTasksView
    path('update_task_status/<int:task_id>/', UpdateTaskStatusView.as_view(), name='update_task_status'),
]

