@echo off
REM Активируем виртуальное окружение
CALL .venv\Scripts\activate

REM Переходим в директорию с проектом, если необходимо
CD /D "E:\Programming\production_orders"

REM Экспортируем переменную окружения DJANGO_SETTINGS_MODULE, если она еще не установлена
IF "%DJANGO_SETTINGS_MODULE%"=="" (
    SET "DJANGO_SETTINGS_MODULE=base.settings"
)

REM start /B python manage.py runserver


REM Запускаем сервер разработки Django в свернутом окне
start "" /MIN cmd /c "python manage.py runserver"

REM Запускаем сервер разработки Django
REM python manage.py runserver

REM Активируем виртуальное окружение
CALL E:\Programming\production_orders\.venv\Scripts\activate

REM Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE
SET "DJANGO_SETTINGS_MODULE=base.settings" 

REM Устанавливаем переменную окружения PYTHONPATH, если необходимо
SET "PYTHONPATH=%PYTHONPATH%;E:\Programming\production_orders"

REM Переходим в директорию проекта
CD /D "E:\Programming\production_orders"

REM Запускаем приложение
REM start "" /MIN cmd /c python windows\start_window.py  

start /B pythonw windows\start_window.py
exit

REM Деактивируем виртуальное окружение после завершения работы
CALL deactivate  

