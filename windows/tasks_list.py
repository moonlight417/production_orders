from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime
import sqlite3
import requests
import resources_rc

class Ui_TasksList(object):
    def setupUi(self, TasksList):
        TasksList.setObjectName("TasksList")
        TasksList.resize(1132, 698)
        self.centralwidget = QtWidgets.QWidget(TasksList)
        self.centralwidget.setObjectName("centralwidget")

        # Главный вертикальный layout для размещения всех виджетов
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # ======= Шапка с виджетами =======
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        # Горизонтальный layout для шапки
        header_layout = QtWidgets.QHBoxLayout(self.frame_3)
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(10)

        self.lineEditSearchCustomer = QtWidgets.QLineEdit(self.frame_3)
        self.lineEditSearchCustomer.setPlaceholderText("Введите название фирмы заказчика")
        header_layout.addWidget(self.lineEditSearchCustomer)

        self.checkBoxFilter = QtWidgets.QCheckBox("Фильтровать по заказчику")
        header_layout.addWidget(self.checkBoxFilter)

        # self.BtnSearchCustomer = QtWidgets.QPushButton(self.frame_3)
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap(":/utils/icons/search.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        # self.BtnSearchCustomer.setIcon(icon)
        # header_layout.addWidget(self.BtnSearchCustomer)

        # self.lineEditSearchProductName = QtWidgets.QLineEdit(self.frame_3)
        # self.lineEditSearchProductName.setPlaceholderText("Введите наименование изделия")
        # header_layout.addWidget(self.lineEditSearchProductName)
        #
        # self.BtnSearchProductName = QtWidgets.QPushButton(self.frame_3)
        # self.BtnSearchProductName.setIcon(icon)
        # header_layout.addWidget(self.BtnSearchProductName)

        self.checkBoxPeriodOn = QtWidgets.QCheckBox("В период от", self.frame_3)
        header_layout.addWidget(self.checkBoxPeriodOn)

        # self.dateEditStartPeriod = QtWidgets.QDateEdit(self.frame_3)
        # self.dateEditStartPeriod.setCalendarPopup(True)
        # self.dateEditStartPeriod.setFixedWidth(100)

        self.current_date = datetime.now()
        self.last_year_date = self.current_date.replace(year=self.current_date.year - 1)
        self.last_year_qdate = QDate(self.last_year_date.year, self.last_year_date.month, self.last_year_date.day)
        self.dateEditStartPeriod = QtWidgets.QDateEdit(self.frame_3)

        self.dateEditStartPeriod.setCalendarPopup(True)
        self.dateEditStartPeriod.setDate(QDate(self.last_year_qdate))
        self.dateEditStartPeriod.setFixedWidth(110)

        header_layout.addWidget(self.dateEditStartPeriod)

        self.label_7 = QtWidgets.QLabel("по", self.frame_3)
        header_layout.addWidget(self.label_7)



        self.dateEditEndPeriod = QtWidgets.QDateEdit(self.frame_3)
        self.dateEditEndPeriod.setCalendarPopup(True)
        self.dateEditEndPeriod.setFixedWidth(110)
        self.dateEditEndPeriod.setDate(QDate.currentDate())
        header_layout.addWidget(self.dateEditEndPeriod)

        # self.comboBoxSort = QtWidgets.QComboBox(self.frame_3)
        # self.comboBoxSort.addItem("Сортировка: По дате")
        # self.comboBoxSort.addItem("Сортировка: По номеру счёта")
        # header_layout.addWidget(self.comboBoxSort)

        # Добавляем шапку в главный layout
        main_layout.addWidget(self.frame_3)

        # ======= Прокручиваемая область =======
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet("""
            QScrollArea {
                background-color: #383838;
            }
            QScrollArea::widget {
                background-color: #383838;
            }
            QScrollBar {
                background-color: #d0d0d0;
                width: 12px;
            }
            QScrollBar::handle {
                background-color: #888888;
                border-radius: 6px;
            }
            QScrollBar::add-line, QScrollBar::sub-line {
                background-color: #a0a0a0;
            }
        """)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.layoutTask = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.layoutTask.setContentsMargins(5, 5, 5, 5)
        self.layoutTask.setSpacing(5)
        self.scrollAreaWidgetContents.setLayout(self.layoutTask)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # Добавляем scrollArea в главный layout
        main_layout.addWidget(self.scrollArea)

        TasksList.setCentralWidget(self.centralwidget)
        self.retranslateUi(TasksList)
        QtCore.QMetaObject.connectSlotsByName(TasksList)

    def retranslateUi(self, TasksList):
        _translate = QtCore.QCoreApplication.translate
        TasksList.setWindowTitle(_translate("TasksList", "Список заданий"))
        self.lineEditSearchCustomer.setPlaceholderText(_translate("TasksList", "Введите название фирмы заказчика"))
        # self.lineEditSearchProductName.setPlaceholderText(_translate("TasksList", "Введите наименование изделия"))
        # self.BtnSearchCustomer.setToolTip(_translate("TasksList", "Искать задания по названию фирмы заказчика"))
        # self.BtnSearchProductName.setToolTip(_translate("TasksList", "Искать задания по наименованию изделия"))
        self.checkBoxPeriodOn.setText(_translate("TasksList", "В период от"))
        self.label_7.setText(_translate("TasksList", "по"))


class TasksList(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TasksList()
        self.ui.setupUi(self)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.reload_tasks)
        self.timer.start(5000)  # 5000 мс = 5 секунд

        # Обработчики для кнопок
        # self.ui.BtnSearchCustomer.clicked.connect(self.search_tasks_by_customer)
        # self.ui.BtnBack.clicked.connect(self.back_main_manager_window)

        self.ui.checkBoxFilter.stateChanged.connect(self.handle_filter_change)
        self.ui.lineEditSearchCustomer.textChanged.connect(self.handle_text_changed)

        # Получаем данные из базы данных для названий организаций-заказчиков
        customer = self.get_words_from_database("orders_customer", "organization_name")

        # Настраиваем QCompleter для поля lineEditSearchCustomer
        completer = QtWidgets.QCompleter(customer, self)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)

        # Настройка шрифта для подсказок в QCompleter
        font = QtGui.QFont()
        font.setPointSize(11)  # Установка нужного размера шрифта
        completer.popup().setFont(font)  # Применяем шрифт к выпадающему списку

        self.ui.lineEditSearchCustomer.setCompleter(completer)

        # Получаем данные из базы данных для наименований изделий
        product_names = self.get_words_from_database("products_product", "name")

        # Настраиваем QCompleter для поля lineEditSearchProductName
        completer = QtWidgets.QCompleter(product_names, self)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)

        # Настройка шрифта для подсказок в QCompleter
        font = QtGui.QFont()
        font.setPointSize(11)  # Установка нужного размера шрифта
        completer.popup().setFont(font)  # Применяем шрифт к выпадающему списку

        # Устанавливаем completer для lineEditSearchProductName
        # self.ui.lineEditSearchProductName.setCompleter(completer)

        # self.ui.comboBoxSort.clear()
        # self.ui.comboBoxSort.addItem("Дата (новые сверху)")
        # self.ui.comboBoxSort.addItem("Номер счёта ↑")
        # self.ui.comboBoxSort.addItem("Номер счёта ↓")

        self.ui.checkBoxPeriodOn.stateChanged.connect(self.handle_period_filter_change)

        self.current_sorting = 'date_desc'

        # self.ui.comboBoxSort.currentIndexChanged.connect(self.handle_sort_change)

        self.show_products = True  # Всегда показывать продукты
        self.current_loading_tasks = []
        self.abort_loading = False
        self.original_tasks = []  # Исходные задачи (сортировка по дате)
        self.current_filtered_tasks = []

        # Загрузка данных
        self.load_initial_tasks()

    def handle_period_filter_change(self, state):
        """Обработчик изменения состояния чекбокса фильтрации по датам"""
        if state == QtCore.Qt.Checked:
            self.apply_date_filter()
        else:
            self.load_all_tasks()

    def apply_date_filter(self):
        """Применяет фильтр по датам"""
        start_date = self.ui.dateEditStartPeriod.date().toPyDate()
        end_date = self.ui.dateEditEndPeriod.date().toPyDate()

        filtered_tasks = []
        for task in self.original_tasks:
            task_date = datetime.strptime(task['order_invoice_date'], '%Y-%m-%d').date()
            if start_date <= task_date <= end_date:
                filtered_tasks.append(task)

        self.process_and_display_tasks(filtered_tasks)

    # def handle_sort_change(self, index):
    #     """Обработчик изменения сортировки"""
    #     sort_options = {
    #         0: 'invoice_asc',
    #         1: 'invoice_desc'
    #     }
    #     self.current_sorting = sort_options.get(index, 'date_desc')
    #     self.reload_tasks()

    def reload_tasks(self):
        """Перезагружает задачи с учетом текущих настроек"""
        if self.ui.checkBoxFilter.isChecked():
            self.apply_customer_filter()
        elif self.ui.checkBoxPeriodOn.isChecked():
            self.apply_date_filter()
        else:
            self.load_initial_tasks()

    def handle_filter_change(self, state):
        """Обработчик изменения состояния чекбокса"""
        if state == QtCore.Qt.Checked:
            customer_name = self.ui.lineEditSearchCustomer.text().strip()
            if customer_name:
                self.search_tasks_by_customer(customer_name)
        else:
            self.load_all_tasks()  # Возврат к полному списку

    def load_products_for_task(self, task_id):
        try:
            response = requests.get(
                "http://127.0.0.1:8000/products/add_product/",
                params={'task_id': task_id}
            )
            print(f"Ответ сервера для task_id={task_id}:", response.text)  # Логирование сырого ответа

            if not response.ok:
                return []

            products = response.json().get('products', [])
            print("Полученные продукты:", products)  # Логирование распарсенных данных
            return products

        except Exception as e:
            print(f"Ошибка загрузки продуктов: {e}")
            return []

    def handle_text_changed(self, text):
        """Обработчик изменения текста в поле поиска"""
        if self.ui.checkBoxFilter.isChecked():
            self.apply_customer_filter()

    def start_loading_tasks(self):
        """Инициализация новой загрузки"""
        self.abort_loading = False
        self.current_loading_tasks = []

        try:
            response = requests.get("http://127.0.0.1:8000/orders/add_customer_and_task/")
            if response.ok:
                self.current_loading_tasks = response.json().get('tasks', [])
                self.process_tasks_sequentially()
        except Exception as e:
            self.handle_error(str(e))

    def process_tasks_sequentially(self, index=0):
        """Рекурсивная обработка задач с задержкой"""
        if self.abort_loading or index >= len(self.current_loading_tasks):
            return

        task = self.current_loading_tasks[index]
        products = []

        if self.show_products:
            try:
                response = requests.get(
                    "http://127.0.0.1:8000/products/add_product/",
                    params={'task_id': task['task_id']},
                    timeout=3
                )
                if response.ok:
                    products = response.json().get('products', [])
            except Exception as e:
                print(f"Ошибка загрузки продуктов: {e}")

        # Создаем элемент интерфейса сразу
        self.add_single_task_to_ui({
            **task,
            'products': products
        })

        # Планируем обработку следующей задачи
        QtCore.QTimer.singleShot(50, lambda: self.process_tasks_sequentially(index + 1))

    def process_and_display_tasks(self, tasks):
        # Очистка текущего списка
        while self.ui.layoutTask.count() > 0:
            item = self.ui.layoutTask.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Добавление задач
        for task in tasks:
            task_frame = QtWidgets.QFrame()
            task_layout = QtWidgets.QVBoxLayout(task_frame)

            # Заголовок (счет, дата, заказчик)
            header = QtWidgets.QLabel(
                f"Счёт: {task['invoice_number']} | "
                f"Дата: {task['order_invoice_date']} | "
                f"Заказчик: {task['customer_name']}"
            )
            task_layout.addWidget(header)

            # Продукты (отображаются всегда)
            products = self.load_products_for_task(task['task_id'])
            for product in products:
                product_label = QtWidgets.QLabel(
                    f"→ {product['name']} ({product.get('quantity_in_task', 0)} шт.)"  # Используйте .get()
                )
                task_layout.addWidget(product_label)

            # Кнопка "Открыть"
            edit_button = QtWidgets.QPushButton("Открыть")
            edit_button.clicked.connect(lambda _, t_id=task['task_id']: self.open_task_editor(t_id))
            task_layout.addWidget(edit_button)

            self.ui.layoutTask.addWidget(task_frame)

    def add_single_task_to_ui(self, task):
        """Добавление одной задачи в UI"""
        try:
            task_frame = QtWidgets.QFrame()
            task_layout = QtWidgets.QVBoxLayout(task_frame)

            # Заголовок
            header = QtWidgets.QLabel(
                f"Счёт: {task.get('invoice_number', 'N/A')} | "
                f"Дата: {task.get('order_invoice_date', 'N/A')} | "
                f"Заказчик: {task.get('customer_name', 'N/A')}"
            )
            task_layout.addWidget(header)

            # Продукты (только если разрешено)
            if self.show_products:
                for product in task.get('products', []):
                    product_label = QtWidgets.QLabel(
                        f"→ {product.get('name', 'Неизвестно')} "
                        f"({product.get('quantity_in_task', 0)} шт.)"
                    )
                    task_layout.addWidget(product_label)

            # Кнопка редактирования
            edit_button = QtWidgets.QPushButton("Открыть")
            edit_button.clicked.connect(lambda _, t_id=task.get('task_id'): self.open_task_editor(t_id))
            task_layout.addWidget(edit_button)

            self.ui.layoutTask.insertWidget(self.ui.layoutTask.count() - 1, task_frame)
            QtWidgets.QApplication.processEvents()  # Принудительное обновление UI

        except Exception as e:
            print(f"Ошибка создания элемента: {e}")

    def apply_customer_filter(self):
        """Применяет фильтр по текущему значению в поле поиска"""
        customer_name = self.ui.lineEditSearchCustomer.text().strip()
        if customer_name:
            self.search_tasks_by_customer(customer_name)
        else:
            self.load_all_tasks()

    def search_tasks_by_customer(self, name):
        try:
            response = requests.get(
                "http://127.0.0.1:8000/orders/customer_data/",
                params={"name": name}
            )
            if response.status_code == 200:
                filtered_tasks = response.json().get("tasks", [])

                # Сортировка отфильтрованных задач по дате
                sorted_filtered_tasks = sorted(
                    filtered_tasks,
                    key=lambda x: datetime.strptime(x['order_invoice_date'], '%Y-%m-%d'),
                    reverse=True
                )
                self.process_and_display_tasks(sorted_filtered_tasks)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка фильтрации: {str(e)}")

    def load_all_tasks(self):
        """Загрузка исходного списка (с сортировкой по дате)"""
        self.process_and_display_tasks(self.original_tasks)

    def process_and_display_tasks(self, tasks):
        """Унифицированный метод отображения задач"""
        # Очистка списка
        while self.ui.layoutTask.count() > 0:
            item = self.ui.layoutTask.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Добавление задач
        for task in tasks:
            task_frame = QtWidgets.QFrame()
            task_frame.setStyleSheet("""
                border: 1.5px solid #666666;
                padding: 1px;
                margin: 1px;
                background-color: #FFFFFF;
            """)

            task_layout = QtWidgets.QVBoxLayout(task_frame)
            task_layout.setContentsMargins(5, 5, 5, 5)

            # Заголовок
            header = QtWidgets.QLabel(
                f"Счёт: {task['invoice_number']} | "
                f"Дата: {task['order_invoice_date']} | "
                f"Заказчик: {task['customer_name']}"
            )
            header.setStyleSheet("""
                font-size: 14px;
                font-weight: bold;
                padding: 5px;
                border-bottom: 1px solid #CCCCCC;
            """)
            task_layout.addWidget(header)

            # Продукты
            products_container = QtWidgets.QWidget()
            products_layout = QtWidgets.QVBoxLayout(products_container)

            if self.show_products:
                products = self.load_products_for_task(task['task_id'])
                if products:
                    for product in products:
                        product_label = QtWidgets.QLabel(
                            f"• {product['name']} - {product['quantity_in_task']} шт."
                        )
                        product_label.setStyleSheet("""
                            font-size: 13px;
                            color: #444444;
                            margin-left: 15px;
                        """)
                        products_layout.addWidget(product_label)
                else:
                    placeholder = QtWidgets.QLabel("Нет данных о продуктах")
                    placeholder.setStyleSheet("""
                        color: #888888;
                        font-style: italic;
                        margin-left: 15px;
                    """)
                    products_layout.addWidget(placeholder)
            else:
                placeholder = QtWidgets.QLabel("Для просмотра продуктов включите фильтр")
                placeholder.setStyleSheet("""
                    color: #888888;
                    font-style: italic;
                    margin-left: 15px;
                """)
                products_layout.addWidget(placeholder)

            task_layout.addWidget(products_container)

            # Кнопка редактирования
            edit_button = QtWidgets.QPushButton("Открыть")
            edit_button.setStyleSheet("""
                QPushButton {
                    background-color: #F0F0F0;
                    border: 1px solid #CCCCCC;
                    padding: 5px;
                    margin-top: 10px;
                }
                QPushButton:hover {
                    background-color: #E0E0E0;
                }
            """)
            edit_button.clicked.connect(lambda _, t_id=task['task_id']: self.open_task_editor(t_id))
            task_layout.addWidget(edit_button)

            self.ui.layoutTask.addWidget(task_frame)

        # Добавляем заполнитель
        self.ui.layoutTask.addWidget(QtWidgets.QWidget(), stretch=1)

    def load_initial_tasks(self):
        try:
            response = requests.get("http://127.0.0.1:8000/orders/add_customer_and_task/")
            if response.status_code == 200:
                tasks = response.json().get("tasks", [])

                # Сортировка по номеру счёта (от большего к меньшему)
                self.original_tasks = sorted(
                    tasks,
                    key=lambda x: int(x['invoice_number']),  # Преобразуем номер счёта в число для корректной сортировки
                    reverse=True  # Сортировка по убыванию
                )
                self.process_and_display_tasks(self.original_tasks)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка загрузки: {str(e)}")

    def search_tasks_by_customer(self, name):
        customer_name = self.ui.lineEditSearchCustomer.text().strip()
        if not customer_name:
            QMessageBox.warning(self, "Ошибка", "Введите название заказчика.")
            return

        try:
            response = requests.get("http://127.0.0.1:8000/orders/customer_data/", params={"name": customer_name})
            if response.status_code == 200:
                data = response.json()
                self.update_task_list(data)
            else:
                QMessageBox.warning(self, "Ошибка", f"Ошибка сервера: {response.text}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось подключиться к серверу: {e}")

    def update_task_list(self, tasks):
        # Очистка текущего списка
        for i in reversed(range(self.ui.layoutTask.count())):
            widget = self.ui.layoutTask.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Добавление заглушки при отсутствии задач
        if not tasks:
            no_data_label = QtWidgets.QLabel("Нет заданий для отображения")
            no_data_label.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.layoutTask.addWidget(no_data_label)
            return


        # Добавление новых заданий
        for task in reversed(tasks):
            # Создаем рамку для задания
            task_frame = QtWidgets.QFrame()
            task_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            task_frame.setStyleSheet("border: 1.5px solid #666666; padding: 1px; margin: 1px;")



            # Вертикальный layout для задания (информация о задании + список продуктов)
            task_layout = QtWidgets.QVBoxLayout(task_frame)

            # Верхняя часть задания: номер счета, дата, заказчик
            task_info = QtWidgets.QLabel(
                f"Счёт: {task['invoice_number']} / Дата: {task['order_date']} / Заказчик: {task['customer_name']}"
            )
            # task_info.setStyleSheet("font-weight: bold; font-size: 14px; background: white;")
            task_info.setStyleSheet("font-size: 14px; "
                                    "font-weight: bold; "
                                     "background: white; "
                                     "border: 1px solid #ff0f0f; "
                                     "margin: 3px;")
            task_info.setFixedHeight(34)
            task_layout.addWidget(task_info)


            product_number = 1

            # Список продуктов
            for product in task["products"]:
                product_label = QtWidgets.QLabel(f"{product_number}. {product['name']} — {product['quantity']} шт.")
                # Стиль для рамки продуктов с тонкой линией
                product_label.setStyleSheet("font-size: 14px; "
                                            "background: white; "
                                            "border: 1px solid #4049c2; "
                                            "margin: 3px;")
                product_label.setFixedHeight(34)
                task_layout.addWidget(product_label)
                product_number += 1

            # Кнопка для открытия окна редактирования задания

            edit_button = QtWidgets.QPushButton("Открыть")
            edit_button.clicked.connect(lambda checked, task_id=task['task_id']: self.open_task_editor(task_id))
            # edit_button.setStyleSheet("margin-top: 10px;font-size: 16px")
            task_layout.addWidget(edit_button, alignment=QtCore.Qt.AlignRight)
            edit_button.setFixedSize(80, 30)  # ширина: 120px, высота: 40px
            # edit_button.setStyleSheet("""
            #     QPushButton
            #     {
            #         background-color: #f0f0f0;
            #         border: 1px solid #808a9c;
            #         font-size: 13px;
            #     }
            #     QPushButton:hover {
            #         background-color: #dae5f7;
            #         border: 1px solid #0a66fa;
            #     }
            #     QPushButton:pressed {
            #         background-color: #d0d0d0;
            #     }
            #     QPushButton:focus {
            #         outline: none;
            #     }
            # """)

            # Добавляем рамку задания в общий layout
            self.ui.layoutTask.addWidget(task_frame)

        # Пустой заполнитель
        self.empty_placeholder = QtWidgets.QWidget()
        self.empty_placeholder.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.ui.layoutTask.addWidget(self.empty_placeholder)  # Добавляем заполнитель в конец layout

    def open_task_editor(self, task_id):
        """
        Открывает окно для просмотра и редактирования конкретного задания.
        :param task_id: ID задания, которое нужно отредактировать.
        """
        # Здесь будет код открытия нового окна и загрузки данных по task_id
        print(f"Открыть редактор для задания с ID: {task_id}")

    def get_words_from_database(self, table_name, column_name):

        """
        Получение данных из базы данных SQLite для указанной таблицы и столбца.
        :param table_name: Название таблицы.
        :param column_name: Название столбца.
        :return: Список строк из указанного столбца.
        """
        try:
            import os

            # Путь к базе данных
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            db_path = os.path.join(BASE_DIR, "db.sqlite3")
            conn = sqlite3.connect(db_path)

            cursor = conn.cursor()

            # Динамический SQL-запрос
            query = f"SELECT DISTINCT {column_name} FROM {table_name}"
            cursor.execute(query)
            result = cursor.fetchall()

            # Преобразуем результат в список строк
            words = [row[0] for row in result]

            conn.close()
            return words

        except sqlite3.Error as e:
            print(f"Ошибка доступа к базе данных: {e}")
            return []


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = TasksList()
    window.show()
    sys.exit(app.exec_())
