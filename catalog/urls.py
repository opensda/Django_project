from django.urls import path

from catalog.views import index, contact

# Настраиваем пути для главной страницы и страницы с обратной связью пользователя

urlpatterns = [
    path('', index),
    path('contacts/', contact),
]
