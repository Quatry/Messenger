# Messenger
## Описание
Messenger - это REST API мессенджер, реализованный с использованием Django Rest Framework (DRF) с поддержкой Redis. Проект предоставляет возможности для создания и управления пользователями, чатами (включая одиночные и групповые чаты), управления участниками чатов, отправки сообщений, а также отслеживания онлайн-статуса пользователей.

## Установка и запуск
Для установки и запуска проекта выполните следующие шаги:

1. ```git clone https://github.com/Quatry/Drf-Messenger.git```
2. ```pip install -r requirements.txt```
3. ```python manage.py migrate```
4. ```python manage.py runserver```
5. Перейти по ```http://localhost:8000/api```
### Использование
Проект Messenger предназначен для использования в качестве API.
### Зависимости
Список зависимостей проекта описан в файле requirements.txt и включает необходимые библиотеки и пакеты для работы с Django, DRF, Redis и другими компонентами проекта.
