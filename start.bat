@echo off
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

REM Деактивируем виртуальное окружение
CALL deactivate


