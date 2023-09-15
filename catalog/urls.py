from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact, all_products, ProductListView, ProductDetailView

# Настраиваем пути для главной страницы и страницы с обратной связью пользователя

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index1'),
    path('contacts/', contact),
    path('products/', all_products, name='all_products'),
    path('product/<pk>', ProductDetailView.as_view())
]

""" Добавляю следующий путь  path('',ProductListView.as_view(), name='index')
и все данные с главной страницы пропадают"""