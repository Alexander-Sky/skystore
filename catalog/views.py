from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


def contacts(request):
    """Страница контактов с формой обратной связи"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Выводим в консоль (для проверки)
        print(f"\n📬 Новое сообщение:")
        print(f"  Имя: {name}")
        print(f"  Телефон: {phone}")
        print(f"  Сообщение: {message}")
        print("=" * 50)

        return HttpResponse("Спасибо за ваше сообщение! Мы свяжемся с вами в ближайшее время.")

    return render(request, 'catalog/contacts.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})