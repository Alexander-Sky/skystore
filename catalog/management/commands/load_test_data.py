from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.core.management import call_command

class Command(BaseCommand):
    help = "Загружает тестовые данные из фикстур"

    def handle(self, *args, **kwargs):
        # Шаг 1: Удаляем старые данные
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write("🗑️ Старые данные удалены.")

        # Шаг 2: Загружаем фикстуры
        try:
            call_command('loaddata', 'catalog/fixtures/categories.json', verbosity=0)
            call_command('loaddata', 'catalog/fixtures/products.json', verbosity=0)
            self.stdout.write(self.style.SUCCESS("✅ Данные успешно загружены!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Ошибка при загрузке данных: {e}"))