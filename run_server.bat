@echo off
REM Активируем виртуальное окружение
CALL .venv\Scripts\activate

REM Переходим в директорию с проектом, если необходимо
CD /D "E:\Programming\production_orders"

REM Экспортируем переменную окружения DJANGO_SETTINGS_MODULE, если она еще не установлена
IF "%DJANGO_SETTINGS_MODULE%"=="" (
    SET "DJANGO_SETTINGS_MODULE=base.settings"
)

REM Запускаем сервер разработки Django в свернутом окне
start "" /MIN cmd /c "python manage.py runserver"

REM Ждем завершения работы (например, нажатия любой клавиши)
echo Сервер Django запущен. Нажмите любую клавишу для остановки...
pause

REM Останавливаем сервер Django
REM Поскольку сервер запущен в отдельном окне, нам нужно найти и остановить его процесс

REM Получаем идентификатор процесса сервера Django
for /f "tokens=2" %%a in ('tasklist ^| findstr /i "python manage.py runserver"') do set PID=%%a

REM Останавливаем процесс
if defined PID (
    echo Останавливаем процесс с PID %PID%...
    taskkill /PID %PID% /F
) else (
    echo Процесс сервера Django не найден.
)

REM Деактивируем виртуальное окружение после завершения работы
CALL deactivate
