from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet
from .views import CheckPasswordView
from .views import ChangePasswordView

router = DefaultRouter()
router.register(r'mymodel', EmployeeViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('check_password/<str:role>/', CheckPasswordView.as_view(), name='check_password'),
    path('api/change_password/', ChangePasswordView.as_view(), name='change_password'),
]