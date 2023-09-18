from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

# Настраиваем пути для главной страницы и страницы с обратной связью пользователя

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='blog-edit'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='blog-delete'),






    # path('contacts/', contact),
    # path('products/', all_products, name='all_products'),
    # path('product/<pk>', ProductDetailView.as_view())
]

# urlpatterns = [
#     path('create/', BlogCreateView.as_view(), name='create'),
#     path('', BlogListView.as_view(), name='list'),
#     # path('view/<int:pk>/', ..., name='view'),
#     # path('edit/<int:pk>/', ..., name='update'),
#     # path('delete/<int:pk>/', ..., name='delete'),
