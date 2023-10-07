from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import contact, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, categories

# Настраиваем пути для главной страницы и страницы с обратной связью пользователя

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/product/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/product/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    path('contacts/', contact),
    path('categories/', categories, name='categories'),
    path('product/<int:pk>',cache_page(60)(ProductDetailView.as_view()), name='product_detail')
]

