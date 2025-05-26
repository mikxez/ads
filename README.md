Ads Exchange Platform (DRF API)

Описание
REST API для платформы размещения объявлений и предложений обмена. Реализовано создание, редактирование, удаление объявлений и предложений, а также поиск и фильтрация.
Установка и запуск
1. Клонировать проект и перейти в директорию:
git clone <репозиторий>
cd <папка проекта>
2. Создать и активировать виртуальное окружение:
python -m venv venv
Windows: venv\Scripts\activate
3. Установить зависимости:
pip install django pillow django-jazzmin djangorestframework
4. Выполнить миграции:
python manage.py makemigrations
python manage.py migrate
5. Запустить сервер:
python manage.py runserver
Категории:
GET /api/v1/categories/ — список категорий
Объявления:
GET /api/v1/ads/ — список объявлений (с фильтрацией, поиском, пагинацией)
POST /api/v1/ads/ — создать объявление
GET /api/v1/ads/<id>/ — получить объявление по ID
PUT /api/v1/ads/<id>/ — обновить (автор)
DELETE /api/v1/ads/<id>/ — удалить (автор)
Предложения обмена:
GET /api/v1/exchange/ — список предложений (фильтрация по отправителю/получателю/статусу)
POST /api/v1/exchange/ — создать предложение обмена
PUT /api/v1/exchange/<id>/ — обновить статус (только участники)
Поиск и фильтрация:
Поиск по title и description: ?search=текст
Фильтрация по category и condition: ?category=<id>&condition=<значение>
Пагинация: ?page=2
Авторизация
Все пользователи могут просматривать.
Только авторы могут редактировать или удалять свои объявления.
python manage.py test
Используемые технологии
Python 3.x
Django
Django REST Framework
SQLite (по умолчанию)

Логин: admin
Пароль: 123

