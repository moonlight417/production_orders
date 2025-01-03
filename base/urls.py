
from idlelib.configdialog import changes

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('changes/', include('changes.urls')),
    path('employees/', include('employees.urls')),
    # path('materials/', include('materials.urls')),
    path('orders/', include('orders.urls')),
    path('products/', include('products.urls')),
    # path('technology/', include('technology.urls')),
]


