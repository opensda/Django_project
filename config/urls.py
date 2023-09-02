from django.contrib import admin
from django.urls import path, include

# Настраиваем URL для приложения catalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls'))
]
