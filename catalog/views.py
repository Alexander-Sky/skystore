from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import DetailView


class HomeView(ListView):
    """Главная страница"""
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ContactsView(TemplateView):
    """Страница контактов с формой обратной связи"""
    template_name = 'catalog/contacts.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'