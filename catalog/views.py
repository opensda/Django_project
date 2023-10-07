from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.services import get_categories_cache


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()

        # Реализуем отображение версии продукта

        for product in products:
            product.active_version = product.versions.filter(is_active=True).first()
        context['products'] = products
        return context


class ProductDetailView(DetailView):
    model = Product



class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')



class ProductUpdateView(LoginRequiredMixin,UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        
        return super().form_valid(form)


def contact(request):
    """
    Контроллер для отображения страницы с контактами

    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'catalog/contacts.html')


def all_products(request):
    """
    Контроллер для отображения всех продуктов на отдельной странице
    """
    products = Product.objects.all()
    context = {
        'objects_list': products
    }

    return render(request, 'catalog/all_products.html', context=context)



class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер для удаления продукта
    """
    model = Product
    context_object_name = 'product'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('catalog:product_list')


def categories(request):
    '''
    Контроллер для отображения категорий
    '''

    context = {
        'object_list': get_categories_cache(),
        'title': 'Категории продуктов интернет-магазина'
    }
    return render(request, 'catalog/categories.html', context)



