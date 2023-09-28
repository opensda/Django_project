from django import forms

from catalog.models import Product, Version


class StyleMixin:
    """
    Класс для единой стилистики форм
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(forms.ModelForm, StyleMixin):
    '''
    Форма для добавления продукта
    '''
    class Meta:
        model = Product
        fields = ('product_name', 'description', 'category',
                  'purchase_price', 'created_date', 'last_changed', 'image',)


    # Реализуем валидацию данных на недопустимые значения

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']

        if cleaned_data.lower() in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман',
                                    'полиция', 'радар']:
            raise forms.ValidationError('Введено недопустимое значение')

        return cleaned_data

class VersionForm(forms.ModelForm, StyleMixin):
    """
    Версия продукта
    """
    class Meta:
        model = Version
        fields = '__all__'
