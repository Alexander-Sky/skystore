from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """Главная страница"""
    return render(request, 'catalog/home.html')


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