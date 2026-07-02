# Skystore

Интернет-магазин на Django для продажи плагинов и примеров кода.

## Технологии
- Python 3.14
- Django 6.0.6
- SQLite / PostgreSQL
- Poetry
- Bootstrap 5
- Pillow
- python-dotenv
- Class-Based Views (CBV)
- CRUD для блога

## Функциональность
### Каталог (`catalog`)
- Главная страница со списком всех товаров
- Страница детального просмотра товара (`/products/<int:pk>/`)
- Обрезанное описание товара (до 100 символов) на главной
- Базовый шаблон (`base.html`) с общей шапкой и подвалом
- Подшаблон меню (`menu.html`) для навигации

### Блог (`blog`)
- Полный CRUD для блоговых записей:
  - Создание (`/blog/new/`)
  - Чтение (`/blog/<int:pk>/`)
  - Редактирование (`/blog/<int:pk>/edit/`)
  - Удаление (`/blog/<int:pk>/delete/`)
- Счётчик просмотров для каждой статьи
- Фильтрация: отображаются только опубликованные статьи (`is_published=True`)
- Превью (изображение) для каждой статьи

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

В settings.py замени блок DATABASES на:

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

catalog/menu.html – подшаблон меню

catalog/home.html – главная страница

catalog/product_detail.html – страница товара

catalog/contacts.html – страница контактов

Блог
blog/blog_list.html – список статей

blog/blog_detail.html – детали статьи

blog/blog_form.html – создание/редактирование

blog/blog_confirm_delete.html – подтверждение удаления

Скриншоты
В папке screenshots/ находятся скриншоты выполнения запросов в Django Shell.

Автор
Александр Шишкин