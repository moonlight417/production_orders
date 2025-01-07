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

        self.BtnSearchCustomer = QtWidgets.QPushButton(self.frame_3)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/utils/icons/search.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.BtnSearchCustomer.setIcon(icon)
        header_layout.addWidget(self.BtnSearchCustomer)

        self.lineEditSearchProductName = QtWidgets.QLineEdit(self.frame_3)
        self.lineEditSearchProductName.setPlaceholderText("Введите наименование изделия")
        header_layout.addWidget(self.lineEditSearchProductName)

        self.BtnSearchProductName = QtWidgets.QPushButton(self.frame_3)
        self.BtnSearchProductName.setIcon(icon)
        header_layout.addWidget(self.BtnSearchProductName)

        self.checkBoxPeriodOn = QtWidgets.QCheckBox("В период от", self.frame_3)
        header_layout.addWidget(self.checkBoxPeriodOn)

        self.dateEditStartPeriod = QtWidgets.QDateEdit(self.frame_3)
        self.dateEditStartPeriod.setCalendarPopup(True)
        self.dateEditStartPeriod.setFixedWidth(100)

        header_layout.addWidget(self.dateEditStartPeriod)

        self.label_7 = QtWidgets.QLabel("по", self.frame_3)
        header_layout.addWidget(self.label_7)

        self.dateEditEndPeriod = QtWidgets.QDateEdit(self.frame_3)
        self.dateEditEndPeriod.setCalendarPopup(True)
        self.dateEditEndPeriod.setFixedWidth(100)
        self.dateEditEndPeriod.setDate(QDate.currentDate())
        header_layout.addWidget(self.dateEditEndPeriod)

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
        self.lineEditSearchProductName.setPlaceholderText(_translate("TasksList", "Введите наименование изделия"))
        self.BtnSearchCustomer.setToolTip(_translate("TasksList", "Искать задания по названию фирмы заказчика"))
        self.BtnSearchProductName.setToolTip(_translate("TasksList", "Искать задания по наименованию изделия"))
        self.checkBoxPeriodOn.setText(_translate("TasksList", "В период от"))
        self.label_7.setText(_translate("TasksList", "по"))


class TasksList(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TasksList()
        self.ui.setupUi(self)

        # Обработчики для кнопок
        self.ui.BtnSearchCustomer.clicked.connect(self.search_tasks_by_customer)
        # self.ui.BtnBack.clicked.connect(self.back_main_manager_window)

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
        self.ui.lineEditSearchProductName.setCompleter(completer)



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
        """
        Обновление списка заданий в прокручиваемой области.
        :param tasks: Список заданий, полученных с сервера.
        """
        # Очистка текущего списка
        for i in reversed(range(self.ui.layoutTask.count())):
            widget = self.ui.layoutTask.itemAt(i).widget()
            if widget:
                widget.deleteLater()


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
