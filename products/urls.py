from django.urls import path
from .views import AddProductView

urlpatterns = [
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('add_drawings/', AddProductView.as_view(), name='add_drawings'),

]
