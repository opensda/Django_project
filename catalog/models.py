from django.db import models


NULLABLE = {"null": True, "blank": True}

class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='имя')
    description = models.TextField(verbose_name='описание')
    


    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)



class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='имя')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    purchase_price = models.FloatField(verbose_name='цена покупки')
    created_date = models.DateField(verbose_name='дата создания')
    last_changed = models.DateField(verbose_name='дата изменения')

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)


