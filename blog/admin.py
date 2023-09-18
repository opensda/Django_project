from django.contrib import admin

from blog.models import Blog


# Register your models here.

@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content',)
    # list_filter = ('category',)
    # search_fields = ('product_name', 'description',)
