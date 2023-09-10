from django.shortcuts import render
from catalog.models import Category, Product




def index(request):
    products_list = Product.objects.all()
    context = {
        'objects_list': products_list
    }
    return render(request, 'catalog/index.html', context)



# def index(request):
#     """
#     Контроллер для отображения домашней страницы
#     :param request: параметры пользователя
#     """
#     return render(request, 'catalog/index.html')


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


def product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }

    return render(request, 'catalog/product.html', context=context)
