from django.core.cache import cache
from .models import Product

def get_products_by_category_with_cache(category_id):
    cache_key = f'category_{category_id}_products'
    products = cache.get(cache_key)
    if products is None:
        products = list(Product.objects.filter(category_id=category_id))
        cache.set(cache_key, products, 60 * 10)  # 10 Minuten
    return products