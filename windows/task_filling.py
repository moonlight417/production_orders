import requests
from PyQt5.QtCore import QDate
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QSpacerItem, QSizePolicy, QHBoxLayout, QPushButton
import sqlite3
import resources_rc
import json

class Ui_TaskFilling(object):
    def setupUi(self, TaskFilling):
        TaskFilling.setObjectName("TaskFilling")
        TaskFilling.resize(1132, 698)

        self.centralwidget = QtWidgets.QWidget(TaskFilling)
        self.centralwidget.setObjectName("centralwidget")

        # Главный вертикальный layout для размещения всех виджетов
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(0, 0, 0, 10)
        main_layout.setSpacing(10)

        # ======= Шапка с виджетами =======
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setMinimumHeight(80)  # Устанавливаем минимальную высоту для шапки
        self.frame_3.setObjectName("frame_3")

        # Горизонтальный layout для шапки, заменяем на QGridLayout
        header_layout = QtWidgets.QGridLayout(self.frame_3)
        header_layout.setContentsMargins(10, 10, 10, 10)
        header_layout.setSpacing(10)

        # Лейблы
        self.labelCheckNumber = QtWidgets.QLabel("№ счёта:")
        self.labelDate = QtWidgets.QLabel("Дата:")
        self.labelCustomer = QtWidgets.QLabel("Название организации заказчика:")
        self.labelProduct = QtWidgets.QLabel("Изделие:")
        # self.labelQuantity = QtWidgets.QLabel("Количество:")



        # Поля ввода
        self.lineEditCheckNumber = QtWidgets.QLineEdit()
        self.lineEditCheckNumber.setFixedWidth(50)
        self.dateEditDate = QtWidgets.QDateEdit()
        self.lineEditCustomer = QtWidgets.QLineEdit()
        self.lineEditProduct = QtWidgets.QLineEdit()
        self.lineEditQuantity = QtWidgets.QLineEdit()

        # Настройка QDateEdit
        self.dateEditDate.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.dateEditDate.setCalendarPopup(True)
        self.dateEditDate.setDate(QDate.currentDate())
        self.dateEditDate.setFixedWidth(100)

        # Добавляем виджеты в grid
        header_layout.addWidget(self.labelCheckNumber, 0, 0)  # 0 строка, 0 столбец
        header_layout.addWidget(self.lineEditCheckNumber, 0, 1)
        header_layout.addWidget(self.labelCustomer, 0, 2)
        header_layout.addWidget(self.lineEditCustomer, 0, 3)
        header_layout.addWidget(self.labelDate, 0, 5)
        header_layout.addWidget(self.dateEditDate, 0, 6, 1, 2)
        # header_layout.addWidget(self.labelProduct, 1, 3)
        # header_layout.addWidget(self.labelQuantity, 1, 5, 1, 2)


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
        self.layoutProducts = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.layoutProducts.setContentsMargins(5, 5, 5, 5)
        self.layoutProducts.setSpacing(5)
        self.scrollAreaWidgetContents.setLayout(self.layoutProducts)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # Добавляем scrollArea в главный layout
        main_layout.addWidget(self.scrollArea)

        # Нижняя панель с кнопками
        self.bottom_panel = QHBoxLayout()

        self.BtnAddNewProduct = QPushButton("Добавить изделие")
        self.bottom_panel.addWidget(self.BtnAddNewProduct)

        self.BtnSave = QPushButton("Сохранить")
        self.bottom_panel.addStretch()  # Добавляем отступ, чтобы кнопка была справа
        self.bottom_panel.addWidget(self.BtnSave)

        self.BtnForDeveloping = QPushButton("На разработку")
        self.BtnForDeveloping.setEnabled(True)
        self.bottom_panel.addStretch()  # Добавляем отступ, чтобы кнопка была справа
        self.bottom_panel.addWidget(self.BtnForDeveloping)

        main_layout.addLayout(self.bottom_panel)

        TaskFilling.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TaskFilling)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 21))
        self.menubar.setObjectName("menubar")
        TaskFilling.setMenuBar(self.menubar)

        self.retranslateUi(TaskFilling)
        QtCore.QMetaObject.connectSlotsByName(TaskFilling)

    def retranslateUi(self, TaskFilling):
        _translate = QtCore.QCoreApplication.translate

        TaskFilling.setWindowTitle(_translate("TaskFilling", "Оформление задания"))
        self.labelProduct.setText(_translate("TaskFilling", "Изделие"))
        # self.labelQuantity.setText(_translate("TaskFilling", "Количество"))
        self.labelCheckNumber.setText(_translate("TaskFilling", "№ счёта:"))
        self.labelDate.setText(_translate("TaskFilling", "Дата:"))
        self.labelCustomer.setText(_translate("TaskFilling", "     Название организации заказчика:"))
        self.BtnAddNewProduct.setText(_translate("TaskFilling", "Добавить изделие"))
        # self.BtnForDeveloping.setText(_translate("TaskFilling", "На разработку"))
        # self.BtnBack.setText(_translate("TaskFilling", "Назад"))
        self.BtnSave.setText(_translate("TaskFilling", "Сохранить"))


class TaskFilling(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TaskFilling()
        self.ui.setupUi(self)

        check_number = self.get_max_value_from_database("orders_task", "invoice_number")
        self.ui.lineEditCheckNumber.setText(str(check_number + 1))  # Преобразуем int в str

        # Получаем данные из базы данных для изделий
        customer = self.get_words_from_database("orders_customer", "organization_name")

        # Настраиваем QCompleter для поля lineEditCustomer
        completer = QtWidgets.QCompleter(customer, self)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.lineEditCustomer.setCompleter(completer)

        # Обработчики для кнопок
        self.ui.BtnAddNewProduct.clicked.connect(self.add_product_line)
        # self.ui.BtnBack.clicked.connect(self.back_main_manager_window)
        self.ui.BtnSave.clicked.connect(self.add_task)
        # self.ui.BtnSave.clicked.connect(self.clearLineEdit)
        # self.ui.BtnSave.clicked.connect(self.clear_scroll_area)

        # Пустой заполнитель
        self.empty_placeholder = QtWidgets.QWidget()
        self.empty_placeholder.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.ui.layoutProducts.addWidget(self.empty_placeholder)  # Добавляем заполнитель в конец layout


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

    def get_max_value_from_database(self, table_name, column_name):
        """
        Получение максимального числового значения из указанной колонки таблицы SQLite.

        :param table_name: Название таблицы.
        :param column_name: Название столбца.
        :return: Максимальное значение из указанного столбца или None в случае ошибки.
        """
        try:
            import os
            import sqlite3

            # Путь к базе данных
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            db_path = os.path.join(BASE_DIR, "db.sqlite3")
            conn = sqlite3.connect(db_path)

            cursor = conn.cursor()

            # Динамический SQL-запрос с приведением к числовому типу
            query = f"SELECT MAX(CAST({column_name} AS INTEGER)) FROM {table_name}"
            cursor.execute(query)
            result = cursor.fetchone()

            conn.close()

            # Если результат не None, вернуть максимальное значение
            return result[0] if result else None

        except sqlite3.Error as e:
            print(f"Ошибка доступа к базе данных: {e}")
            return None

    def add_product_line(self):
        try:
            # Создаем новый фрейм для строки изделия
            frame_product_line = QtWidgets.QFrame()
            frame_product_line.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame_product_line.setFrameShadow(QtWidgets.QFrame.Raised)
            frame_product_line.setStyleSheet("""
                QFrame {
                    border: 1px solid black;
                }
            """)
            frame_product_line.setFixedHeight(40)
            frame_product_line.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

            # Создаем layout для элементов внутри строки
            frame_layout = QtWidgets.QHBoxLayout(frame_product_line)
            frame_layout.setContentsMargins(5, 5, 5, 5)
            frame_layout.setSpacing(5)

            # Лейбл с порядковым номером изделия
            product_num = self.ui.layoutProducts.count()  # Учитываем добавление заполнителя
            label_product_num = QtWidgets.QLabel(str(product_num))
            font = QtGui.QFont()
            font.setPointSize(12)
            label_product_num.setFont(font)
            label_product_num.setStyleSheet("QLabel { border: none; }")
            frame_layout.addWidget(label_product_num)

            # Поле ввода названия изделия
            lineEditProductName = QtWidgets.QLineEdit()
            lineEditProductName.setFont(QtGui.QFont("Arial", 12))
            lineEditProductName.setPlaceholderText("Введите название изделия")

            # Настраиваем QCompleter для нового поля
            product_names = self.get_words_from_database("products_product", "name")
            completer = QtWidgets.QCompleter(product_names, self)
            completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
            lineEditProductName.setCompleter(completer)

            frame_layout.addWidget(lineEditProductName)

            # Поле ввода количества
            spin_box_quantity = QtWidgets.QSpinBox()
            spin_box_quantity.setFixedSize(80, 24)
            spin_box_quantity.setStyleSheet("QSpinBox { font-size: 14px; }")
            spin_box_quantity.setMaximum(999999)
            spin_box_quantity.setSingleStep(10)
            frame_layout.addWidget(spin_box_quantity)

            label_piece = QtWidgets.QLabel("шт.")
            label_piece.setStyleSheet("""
                QLabel {
                        border: none;
                     }
                        """)

            frame_layout.addWidget(label_piece)

            # Кнопка удаления строки
            btn_delete = QtWidgets.QPushButton()
            btn_delete.setFixedSize(26, 26)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/utils/icons/x-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            btn_delete.setIcon(icon)
            btn_delete.setIconSize(QtCore.QSize(16, 16))
            frame_layout.addWidget(btn_delete)

            # Привязка кнопки удаления к функции
            btn_delete.clicked.connect(lambda: self.delete_product_line(frame_product_line))

            # Добавляем созданный фрейм перед заполнителем
            self.ui.layoutProducts.insertWidget(self.ui.layoutProducts.count() - 1, frame_product_line)

        except Exception as e:
            print(f"Ошибка в add_product_line: {e}")

    def delete_product_line(self, frame_product_line):
        """Удаление строки и обновление нумерации"""
        try:
            # Удаление фрейма из layout
            self.ui.layoutProducts.removeWidget(frame_product_line)
            frame_product_line.deleteLater()

            # Обновляем номера всех строк
            self.update_product_numbers()

        except Exception as e:
            print(f"Ошибка в delete_product_line: {e}")

    def update_product_numbers(self):
        """Пересчитывает номера всех строк"""
        try:
            # Находим все фреймы в layoutProducts, исключая заполнитель
            for i in range(self.ui.layoutProducts.count() - 1):
                item = self.ui.layoutProducts.itemAt(i).widget()
                if isinstance(item, QtWidgets.QFrame):
                    label = item.findChild(QtWidgets.QLabel)  # Находим QLabel в фрейме
                    if label:
                        label.setText(str(i + 1))  # Обновляем номер
        except Exception as e:
            print(f"Ошибка в update_product_numbers: {e}")

    def enable_for_developing_button(self):
        """Активирует вторую кнопку."""
        self.ui.BtnForDeveloping.setEnabled(True)

    def add_task(self):
        # Собирает данные о заказе и продуктах, отправляет их на сервер.
        customer_and_task_data = {
            "invoice_number": self.ui.lineEditCheckNumber.text(),
            "order_date": self.ui.dateEditDate.date().toString("yyyy-MM-dd"),
            "organization_name": self.ui.lineEditCustomer.text(),
        }

        # Проверка, что все поля задания заполнены
        if not all(customer_and_task_data.values()):
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Заполните все поля корректно.")
            return

        # Проверка, что добавлен хотя бы один продукт
        product_data_list = self.collect_product_data(None)  # Передаем None, так как task_id пока неизвестен
        if not product_data_list:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Добавьте хотя бы один продукт и заполните все поля.")
            return

        try:
            # Сначала отправляем задание и получаем task_id
            response = requests.post(
                "http://127.0.0.1:8000/orders/add_customer_and_task/",
                json=customer_and_task_data
            )
            if response.status_code == 201:
                task_id = response.json().get("task_id")
                if not task_id:
                    QtWidgets.QMessageBox.warning(self, "Ошибка", "Не удалось получить ID задания.")
                    return

                # Теперь добавляем task_id к каждому продукту
                for product_data in product_data_list:
                    product_data["task_id"] = task_id

                # Отправляем данные о продуктах
                for product_data in product_data_list:
                    response = requests.post("http://127.0.0.1:8000/products/add_product/", json=product_data)
                    if response.status_code != 201:
                        QtWidgets.QMessageBox.warning(
                            self,
                            "Ошибка",
                            f"Ошибка при добавлении продукта: {response.text}"
                        )
                        return

                QtWidgets.QMessageBox.information(self, "Успех", "Данные успешно добавлены!")
                self.clear_products()
                self.ui.lineEditCustomer.clear()
                check_number = self.get_max_value_from_database("orders_task", "invoice_number")
                self.ui.lineEditCheckNumber.setText(str(check_number + 1))
            else:
                QtWidgets.QMessageBox.warning(self, "Ошибка", f"Ошибка сервера: {response.text}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка", f"Не удалось отправить данные: {e}")

    def collect_product_data(self, task_id):
        """
        Сбор данных о продуктах из динамически созданных строк.

        :param task_id: ID задания, с которым связаны продукты.
        :return: Список словарей с данными о продуктах.
        """
        product_data_list = []

        for i in range(self.ui.layoutProducts.count() - 1):  # Исключаем последний виджет-заполнитель
            item = self.ui.layoutProducts.itemAt(i).widget()
            if isinstance(item, QtWidgets.QFrame):  # Проверяем, что это строка продукта
                # Извлекаем данные из виджетов внутри строки
                lineEditProductName = item.findChild(QtWidgets.QLineEdit)
                spin_box_quantity = item.findChild(QtWidgets.QSpinBox)

                if lineEditProductName and spin_box_quantity:
                    product_name = lineEditProductName.text().strip()
                    quantity = spin_box_quantity.value()

                    # Проверка, что данные заполнены
                    if product_name and quantity > 0:
                        product_data_list.append({
                            "task_id": task_id,
                            "name": product_name,
                            "quantity": quantity,
                        })

        return product_data_list

    def clear_layout(self, layout):
        """Очищает layout и обновляет его."""
        if layout:
            for i in reversed(range(layout.count())):
                item = layout.itemAt(i)
                if item is not None:
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()
            layout.update()  # Обновляем layout после удаления виджетов

    def clear_products(self):
        # Очищает все строки продуктов в layout
        self.clear_layout(self.ui.layoutProducts)
        self.ui.layoutProducts.update()  # Обновляем layout после очистки
        # Пустой заполнитель
        self.empty_placeholder = QtWidgets.QWidget()
        self.empty_placeholder.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.ui.layoutProducts.addWidget(self.empty_placeholder)  # Добавляем заполнитель в конец layout


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = TaskFilling()
    main_window.show()
    sys.exit(app.exec_())

