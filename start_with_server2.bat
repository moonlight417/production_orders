@echo off
REM Активируем виртуальное окружение
call .venv\Scripts\activate

REM Устанавливаем переменные окружения
set "DJANGO_SETTINGS_MODULE=base.settings"
set "PYTHONPATH=%PYTHONPATH%;E:\Programming\production_orders"

REM Переходим в директорию проекта
cd /D "E:\Programming\production_orders"

REM Запуск сервера Django в фоновом режиме и сохранение его PID
start /B python manage.py runserver
set "DJANGO_PID=%errorlevel%"

REM Запуск основного приложения и ожидание его завершения
python windows\start_window.py

REM Остановка сервера Django после завершения оконного приложения
taskkill /PID %DJANGO_PID% /F

REM Закрытие консоли
exit