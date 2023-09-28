from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

# Настраиваем пути для главной страницы и страницы с обратной связью пользователя

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/product/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/product/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    path('contacts/', contact),
    # path('products/', all_products, name='all_products'),
    path('product/<int:pk>', ProductDetailView.as_view())
]

