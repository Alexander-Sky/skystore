from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = 'Создаёт группы и назначает права'

    def handle(self, *args, **kwargs):
        # Группа "Модератор продуктов"
        moderator_group, created = Group.objects.get_or_create(name='Модератор продуктов')

        # Права
        content_type = ContentType.objects.get_for_model(Product)

        # Право на отмену публикации
        can_unpublish, _ = Permission.objects.get_or_create(
            codename='can_unpublish_product',
            name='Может отменять публикацию продукта',
            content_type=content_type,
        )

        # Право на удаление продукта (стандартное)
        delete_permission = Permission.objects.get(
            codename='delete_product',
            content_type=content_type,
        )

        # Назначаем права группе
        moderator_group.permissions.add(can_unpublish, delete_permission)

        self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" создана и настроена!'))