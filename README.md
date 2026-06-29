# Skystore

Интернет-магазин на Django для продажи плагинов и примеров кода.

## Технологии
- Python 3.14
- Django 6.0.6
- PostgreSQL / SQLite
- Poetry
- Bootstrap 5
- Pillow
- python-dotenv
- Кастомные команды Django
- Шаблонизация Django (наследование, include)

## Функциональность
- Главная страница со списком всех товаров
- Страница детального просмотра товара (`/products/<int:pk>/`)
- Обрезанное описание товара (до 100 символов) на главной
- Базовый шаблон (`base.html`) с общей шапкой и подвалом
- Подшаблон меню (`menu.html`) для навигации
- Контактная страница
- Административная панель Django

## Установка и запуск

```bash
git clone https://github.com/Alexander-Sky/skystore.git
cd skystore
poetry install
Настройка базы данных
Создай файл .env в корне проекта со следующим содержимым:

env
DB_NAME=skystore
DB_USER=postgres
DB_PASSWORD=твой_пароль
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=твой_секретный_ключ
DEBUG=True
Или используй SQLite (для разработки без установки PostgreSQL):

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
Создай суперпользователя для админки:

bash
poetry run python manage.py createsuperuser
Запуск сервера
bash
poetry run python manage.py runserver
Открыть: http://127.0.0.1:8000/

Загрузка тестовых данных
Для наполнения базы тестовыми данными выполни кастомную команду:

bash
poetry run python manage.py load_test_data
Структура шаблонов
catalog/base.html – базовый шаблон (шапка, подвал, стили)

catalog/menu.html – подшаблон с навигационным меню

catalog/home.html – главная страница со списком товаров

catalog/product_detail.html – страница товара

catalog/contacts.html – страница контактов

Скриншоты
В папке screenshots/ находятся скриншоты выполнения запросов в Django Shell.

Автор
Александр Шишкин