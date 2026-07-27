# Skystore

Интернет-магазин на Django для продажи плагинов и примеров кода.

## Технологии
- Python 3.14
- Django 6.0.6
- SQLite (разработка)
- Poetry
- Bootstrap 5
- Pillow
- python-dotenv
- Class-Based Views (CBV)
- Django Forms с валидацией

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

### Блог (`blog`)
- Полный CRUD для блоговых записей
- Счётчик просмотров
- Фильтрация по публикации

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

Блог
blog/blog_list.html – список статей

blog/blog_detail.html – детали статьи

blog/blog_form.html – создание/редактирование

blog/blog_confirm_delete.html – подтверждение удаления

Скриншоты
В папке screenshots/ находятся скриншоты выполнения запросов в Django Shell и работы интерфейса.

Автор
Александр Шишкин