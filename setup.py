from distutils.core import setup
import py2exe
import sys
import os

# Получаем текущую директорию
current_dir = os.path.dirname(os.path.abspath(__file__))

# Добавляем путь к проекту в sys.path, если необходимо
sys.path.insert(0, os.path.join(current_dir, 'windows'))
sys.path.insert(0, os.path.join(current_dir, 'products'))
sys.path.insert(0, os.path.join(current_dir, 'materials'))
sys.path.insert(0, os.path.join(current_dir, 'changes'))
sys.path.insert(0, os.path.join(current_dir, 'employees'))
sys.path.insert(0, os.path.join(current_dir, 'orders'))
sys.path.insert(0, os.path.join(current_dir, 'technology'))
sys.path.insert(0, os.path.join(current_dir, 'base'))

# Явно указываем пакеты для включения
packages = [
    'base',
    'orders',
    'changes',
    'windows',
    'products',
    'employees',
    'materials',
    'technology',
    'utils',
    # Добавьте другие пакеты, если необходимо
]

# Список скриптов для включения
scripts = ['windows/start_window.py']  # Замените на ваш скрипт запуска

# Список данных для включения
data_files = []

# Настройка сборки
setup(
    name='YourAppName',
    version='1.0',
    description='Описание вашего приложения',
    author='Ваше имя',
    author_email='ваш.email@example.com',
    windows=[{
        'script': 'windows/start_window.py',  # Укажите путь к вашему скрипту
        'icon_resources': [(1, 'binance_coin_bnb_crypto_icon_264360.ico')]  # Необязательно: добавьте иконку
    }],
    options={
        "py2exe": {
            "bundle_files": 1,
            "compressed": True,
            "optimize": 2,
            "packages": packages,  # Явно указываем пакеты
            "includes": [],  # Явно указываем модули, если необходимо
            "excludes": [],  # Исключаем ненужные модули
        }
    },
    data_files=data_files,
    zipfile=None,  # Убираем создание zip-файла
)