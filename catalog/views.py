from django.shortcuts import render
from catalog.models import Category, Product
from django.views.generic import ListView, DetailView


# class ProductListView(ListView):
#     model = Product
#     template_name = 'catalog/index.html'


def index(request):
    products_list = Product.objects.all()
    context = {
        'objects_list': products_list,
        'title': 'SkyStore'
    }
    return render(request, 'catalog/index.html', context=context)




def contact(request):
    """
    Контролеер для отображения страницы с контактами

    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'catalog/contacts.html')


def all_products(request):
    products = Product.objects.all()
    context = {
        'objects_list': products
    }

    return render(request, 'catalog/all_products.html', context=context)



class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'

# def product_by_pk(request, pk):
#     product = Product.objects.get(pk=pk)
#     context = {
#         'product': product
#     }
#
#     return render(request, 'catalog/product.html', context=context)