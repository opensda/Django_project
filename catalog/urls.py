from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contact, product_by_pk, all_products

# Настраиваем пути для главной страницы и страницы с обратной связью пользователя

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contact),
    path('product/', all_products, name='all_products'),
    path('product/<pk>', product_by_pk),
]
