from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        is_owner = product.owner == request.user
        is_moderator = (
                request.user.has_perm('catalog.can_unpublish_product')
                or request.user.has_perm('catalog.delete_product')
        )
        if not (is_owner or is_moderator):
            raise PermissionDenied("У вас нет прав на это действие.")
        return super().dispatch(request, *args, **kwargs)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        is_owner = product.owner == request.user
        is_moderator = (
                request.user.has_perm('catalog.can_unpublish_product')
                or request.user.has_perm('catalog.delete_product')
        )
        if not (is_owner or is_moderator):
            raise PermissionDenied("У вас нет прав на это действие.")
        return super().dispatch(request, *args, **kwargs)