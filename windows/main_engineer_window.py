from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QStackedWidget, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from tasks_list import TasksList
from search_design_document import SearchDesignDoc
import requests
from test_new_tasks import NewTasks
from orders_archive import OrdersArchive

import sys
import os

from windows.customizing_materials import Materials
# from windows.order_dev.order_dev_main import OrderDev

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "e:/Programming/production_orders/")))
from windows.design_filling.design_document_filling_form import DesignDocumentFillingForm

class Ui_MainWindowEngineer(object):
    def setupUi(self, MainWindowEngineer):
        MainWindowEngineer.setObjectName("MainWindowManager")
        MainWindowEngineer.resize(1200, 700)
        MainWindowEngineer.setWindowTitle("Главное окно инженера")

        self.centralwidget = QtWidgets.QWidget(MainWindowEngineer)
        self.main_layout = QVBoxLayout(self.centralwidget)

        # Верхняя панель с кнопками (левая и правая части)
        self.top_panel = QHBoxLayout()

        # Левая часть верхней панели (основные кнопки)
        self.left_top_panel = QHBoxLayout()
        self.BtnViewTasks = QtWidgets.QPushButton("Задания")
        self.BtnOrderBase = QtWidgets.QPushButton("База заказов")
        self.BtnDrowingArchive = QtWidgets.QPushButton("Архив КД")
        self.BtnAddNewDesignDoc = QtWidgets.QPushButton("Новый КД")
        self.BtnMaterials = QtWidgets.QPushButton("Материалы")

        self.left_top_panel.addWidget(self.BtnViewTasks)
        self.left_top_panel.addWidget(self.BtnOrderBase)
        self.left_top_panel.addWidget(self.BtnDrowingArchive)
        self.left_top_panel.addWidget(self.BtnAddNewDesignDoc)
        self.left_top_panel.addWidget(self.BtnMaterials)

        # Правая часть верхней панели (лейбл)
        self.right_top_panel = QHBoxLayout()
        self.LbCheckOrders = QLabel()  # Лейбл с числом новых заданий
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.LbCheckOrders.setFont(font)
        self.LbCheckOrders.setAlignment(QtCore.Qt.AlignCenter)
        self.BtnCheckOrders = QPushButton("Открыть")
        self.BtnRoleSelection = QPushButton("К выбору роли")

        self.right_top_panel.addWidget(self.LbCheckOrders)
        self.right_top_panel.addWidget(self.BtnCheckOrders)

        # Добавляем левую и правую части в верхнюю панель
        self.top_panel.addLayout(self.left_top_panel)
        self.top_panel.addStretch()  # Отступ между левой и центральной частью
        self.top_panel.addLayout(self.right_top_panel)
        self.top_panel.addStretch()  # Отступ между центральной и правой частью
        self.top_panel.addWidget(self.BtnRoleSelection)

        # Стек для переключаемых окон
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # Добавляем все элементы в главный layout
        self.main_layout.addLayout(self.top_panel)
        self.main_layout.addWidget(self.stacked_widget)

        MainWindowEngineer.setCentralWidget(self.centralwidget)

class MainWindowEngineer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindowEngineer()
        self.ui.setupUi(self)

        # Создание таймера
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_new_tasks_count)  # Подключаем таймер к методу обновления
        self.timer.start(5000)  # Обновление каждые 5 секунд

        # Подключение кнопок к методам
        self.ui.BtnAddNewDesignDoc.clicked.connect(lambda: self.switch_window(self.design_document_filling_window))
        self.ui.BtnViewTasks.clicked.connect(lambda: self.switch_window(self.tasks_list_window))
        self.ui.BtnRoleSelection.clicked.connect(self.back_role_selection)
        self.ui.BtnDrowingArchive.clicked.connect(lambda: self.switch_window(self.search_design_doc_window))
        self.ui.BtnCheckOrders.clicked.connect(self.open_new_tasks)
        self.ui.BtnOrderBase.clicked.connect(lambda: self.switch_window(self.view_orders_window))
        self.ui.BtnMaterials.clicked.connect(lambda: self.switch_window(self.materials_window))

        # Получаем количество новых заданий
        self.new_tasks = self.get_new_tasks_count()  # Получаем количество новых заданий
        self.update_order_count_label()
        self.ui.BtnCheckOrders.setEnabled(self.new_tasks != 0)  # Включение/отключение кнопки

        # Создание экземпляров окон
        self.empty_window = QWidget()
        self.design_document_filling_window = DesignDocumentFillingForm()
        self.tasks_list_window = TasksList()
        self.search_design_doc_window = SearchDesignDoc(parent=None)
        # self.new_tasks_list_window = NewTasks(parent=self)  # Передаем ссылку на родительское окно
        self.view_orders_window = OrdersArchive()
        self.materials_window = Materials()
        # self.order_dev_window = OrderDev()  # Создаем экземпляр OrderDev

        self.new_tasks_list_window = NewTasks()  # Создаем экземпляр NewTasks
        # self.ui.stacked_widget.addWidget(self.new_tasks_list_window)  # Добавляем NewTasks в стек

        # Добавление окон в QStackedWidget
        self.ui.stacked_widget.addWidget(self.empty_window)
        self.ui.stacked_widget.addWidget(self.design_document_filling_window)
        self.ui.stacked_widget.addWidget(self.tasks_list_window)
        self.ui.stacked_widget.addWidget(self.search_design_doc_window)
        # self.ui.stacked_widget.addWidget(self.view_orders_window)
        self.ui.stacked_widget.addWidget(self.materials_window)
        # self.ui.stacked_widget.addWidget(self.new_tasks_list_window)
        # self.ui.stacked_widget.addWidget(self.order_dev_window)  # Добавляем OrderDev в стек

        # Устанавливаем пустое окно как текущее
        self.ui.stacked_widget.setCurrentWidget(self.empty_window)

    def update_new_tasks_count(self):
        """Обновление количества новых заданий"""
        self.new_tasks = self.get_new_tasks_count()  # Получаем новое количество
        self.update_order_count_label()  # Обновляем лейбл
        self.ui.BtnCheckOrders.setEnabled(self.new_tasks != 0)  # Обновляем состояние кнопки

    def switch_window(self, window):
        """Переключение на указанное окно"""
        self.ui.stacked_widget.setCurrentWidget(window)

    def update_order_count_label(self):
        """Обновление текста лейбла с числом заказов"""
        self.ui.LbCheckOrders.setText(str(f"Новых заданий: {self.new_tasks} "))

    def back_role_selection(self):
        """Переход к окну выбора роли"""
        try:
            from windows.start_window import StartWindow
            self.role_selection_window = StartWindow()
            self.role_selection_window.show()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось открыть окно выбора роли: {e}")

    def get_new_tasks_count(self):
        base_url = 'http://127.0.0.1:8000/'
        api_path = 'orders/new_tasks/'
        full_url = f'{base_url}{api_path}'

        response = requests.get(full_url)
        if response.status_code == 200:
            new_tasks = response.json()  # Получаем список новых заданий
            return len(new_tasks)  # Возвращаем количество новых заданий
        return 0

    def open_new_tasks(self):
        """Обработка нажатия кнопки 'Открыть' для просмотра новых заданий"""
        if self.new_tasks > 0:
            print("Открытие окна с новыми заданиями...")  # Отладочное сообщение

            # Создаем экземпляр NewTasks
            self.new_tasks_window = NewTasks()  # Создаем экземпляр NewTasks
            self.new_tasks_window.load_new_tasks()  # Загружаем новые задания
            self.new_tasks_window.show()  # Показываем окно

            # Уменьшаем количество новых заданий на 1
            self.decrement_new_tasks_count()  # Этот метод должен отправлять запрос на сервер

            # Обновляем счетчик новых заданий
            self.update_new_tasks_count()  # Обновляем счетчик на интерфейсе инженера

    # def open_new_tasks(self):
    #     """Обработка нажатия кнопки 'Открыть' для просмотра новых заданий"""
    #     if self.new_tasks > 0:
    #         print("Открытие окна с новыми заданиями...")  # Отладочное сообщение
    #         self.switch_window(self.new_tasks_list_window)
    #
    #         try:
    #             self.new_tasks_list_window.load_new_tasks()  # Загружаем новые задания
    #             print("Новые задания загружены.")  # Отладочное сообщение
    #         except Exception as e:
    #             print(f"Ошибка при загрузке новых заданий: {e}")  # Отладочное сообщение
    #             QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить новые задания: {str(e)}")
    #
    #         self.decrement_new_tasks_count()  # Этот метод должен отправлять запрос на сервер
    #         self.update_new_tasks_count()  # Обновляем счетчик на интерфейсе инженера

    def decrement_new_tasks_count(self):
        """Уменьшение количества новых заданий на сервере"""
        task_id = self.new_tasks_list_window.get_selected_task_id()  # Получаем ID выбранного задания
        if task_id:
            base_url = 'http://127.0.0.1:8000/'
            api_path = f'orders/start_task/{task_id}/'  # Путь к API для начала работы над заданием
            full_url = f'{base_url}{api_path}'

            response = requests.post(full_url)  # Отправляем POST-запрос на сервер
            if response.status_code == 200:
                self.new_tasks -= 1  # Уменьшаем локальное количество новых заданий
                self.update_order_count_label()  # Обновляем лейбл
                self.ui.BtnCheckOrders.setEnabled(self.new_tasks != 0)  # Обновляем состояние кнопки
            else:
                QMessageBox.critical(self, "Ошибка", "Не удалось начать задание.")

    def load_new_tasks(self):
        """Метод для загрузки и отображения новых заданий"""
        try:
            base_url = 'http://127.0.0.1:8000/'
            api_path = 'orders/new_tasks/'  # Предполагаем, что у вас есть этот маршрут
            full_url = f'{base_url}{api_path}'

            response = requests.get(full_url)
            if response.status_code == 200:
                new_tasks = response.json()  # Предполагаем, что сервер возвращает список новых заданий
                print(f"Полученные задания: {new_tasks}")  # Отладочное сообщение
                self.populate_task_list(new_tasks)  # Заполняем список заданий
            else:
                self.task_container.addWidget(QtWidgets.QLabel("Не удалось загрузить новые задания."))
        except Exception as e:
            self.task_container.addWidget(QtWidgets.QLabel(f"Произошла ошибка: {str(e)}"))

    def populate_task_list(self, tasks):
        """Метод для заполнения списка заданий в scrollArea"""
        try:
            # Очищаем предыдущие элементы в scrollArea
            for i in reversed(range(self.ui.verticalLayout_2.count())):
                widget = self.ui.verticalLayout_2.itemAt(i).widget()
                if widget is not None:
                    widget.deleteLater()

            # Добавляем новые задания в scrollArea
            for task in tasks:
                task_label = QLabel(f"Задание: {task['invoice_number']} - Дата: {task['order_invoice_date']}")
                self.ui.verticalLayout_2.addWidget(task_label)

            # Обновляем scrollArea
            self.ui.scrollArea.setWidget(self.ui.scrollAreaWidgetContents)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось заполнить список заданий: {str(e)}")


