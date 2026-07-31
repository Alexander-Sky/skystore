# Skystore

Интернет-магазин на Django для продажи плагинов и примеров кода.

## Технологии
- Python 3.14
- Django 6.0.6
- SQLite (разработка) / PostgreSQL (продакшен)
- Poetry
- Bootstrap 5
- Pillow
- python-dotenv
- Class-Based Views (CBV)
- Django Forms с валидацией
- Redis (кэширование)
- Аутентификация и права доступа

## Функциональность

### Каталог (`catalog`)
- Полный CRUD для продуктов:
  - Создание (`/create/`)
  - Чтение (`/` и `/<int:pk>/`)
  - Редактирование (`/<int:pk>/update/`)
  - Удаление (`/<int:pk>/delete/`)
- Валидация форм:
  - Запрещённые слова в названии и описании
  - Цена не может быть отрицательной
- Стилизация форм через Bootstrap (метод `__init__`)
- Загрузка и отображение изображений продуктов

### Кэширование (Redis)
- Страница продукта кэшируется на 15 минут (`cache_page`)
- Список продуктов в категории кэшируется на 10 минут
- Низкоуровневое кэширование через сервисный слой

### Права доступа и модерация
- Поле `is_published` (статус публикации продукта)
- Кастомное право `can_unpublish_product`
- Группа **"Модератор продуктов"** с правами:
  - `can_unpublish_product`
  - `delete_product`
- Поле `owner` – автоматически заполняется при создании продукта
- Проверки в контроллерах:
  - Редактирование и удаление доступны только владельцу или модератору
- Кнопки редактирования/удаления отображаются только для владельца или модератора

### Блог (`blog`)
- Полный CRUD для блоговых записей
- Счётчик просмотров
- Фильтрация по публикации

### Аутентификация
- Регистрация с E-Mail-подтверждением
- Login/Logout
- Zugriffsschutz für CRUD-Operationen (nur eingeloggte Benutzer)

### Benutzerprofil
- Erweiterte Benutzermodell mit:
  - Avatar
  - Telefon
  - Land

## Установка и запуск

```bash
git clone https://github.com/Alexander-Sky/skystore.git
cd skystore
poetry install
Настройка базы данных
Создай файл .env в корне проекта:

env
DB_NAME=skystore
DB_USER=postgres
DB_PASSWORD=твой_пароль
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=твой_секретный_ключ
DEBUG=True
Или используй SQLite (для разработки):

python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
Примени миграции:

bash
poetry run python manage.py migrate
Создай суперпользователя:

bash
poetry run python manage.py createsuperuser
Настройка Redis (для кэширования)
Установи Redis (локально или через Docker).

В settings.py добавь:

python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
Проверь работу:

bash
redis-cli ping  # должно вернуть PONG
Запуск сервера
bash
poetry run python manage.py runserver
Открыть: http://127.0.0.1:8000/

Загрузка тестовых данных
Для наполнения базы тестовыми данными:

bash
poetry run python manage.py load_test_data
Структура шаблонов
Каталог
catalog/base.html – базовый шаблон

catalog/product_list.html – список продуктов

catalog/product_detail.html – детали продукта

catalog/product_form.html – форма создания/редактирования

catalog/product_confirm_delete.html – подтверждение удаления

catalog/category_products.html – список продуктов по категории (с кэшированием)

Блог
blog/blog_list.html – список статей

blog/blog_detail.html – детали статьи

blog/blog_form.html – создание/редактирование

blog/blog_confirm_delete.html – подтверждение удаления

Скриншоты
В папке screenshots/ находятся скриншоты выполнения запросов в Django Shell и работы интерфейса.

Автор
Александр Шишкин