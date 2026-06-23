# Skystore

Интернет-магазин на Django для продажи плагинов и примеров кода.

## Технологии
- Python 3.14
- Django 6.0.6
- PostgreSQL
- Poetry
- Bootstrap 5
- Pillow
- python-dotenv

## Установка и запуск

```bash
git clone https://github.com/Alexander-Sky/skystore.git
cd skystore
poetry install
Настройка базы данных
Установи PostgreSQL и создай базу данных skystore.

Создай файл .env в корне проекта со следующим содержимым:

env
DB_NAME=skystore
DB_USER=postgres
DB_PASSWORD=твой_пароль
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=твой_секретный_ключ
DEBUG=True
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
Скриншоты
В папке screenshots/ находятся скриншоты выполнения запросов в Django Shell.

Автор
Александр Шишкин