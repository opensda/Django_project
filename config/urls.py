from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from catalog.views import product_by_pk, all_products

# Настраиваем URL для приложения catalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls', namespace='catalog')),
    path('product/<pk>', product_by_pk),
    path('product/', all_products)
              ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
