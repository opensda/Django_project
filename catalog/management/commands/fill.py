from django.core.management import BaseCommand

from catalog.models import Category

"""Кастомная команда для наполнения БД"""

class Command(BaseCommand):
    def handle(self, *args, **options):

        # Предварительно очищаем БД

        Category.objects.all().delete()

        # Формируем необходимые данные для записи

        categories = [
            {'category_name': "Кондитерка",'description': "просто кондитерка" },
            {'category_name': "Молочка", 'description': "просто молочка"}
        ]

        category_to_fill = []
        for category in categories:
            category_to_fill.append(Category(**category))


        # Записываем данные

        Category.objects.bulk_create(category_to_fill)
