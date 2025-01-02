import requests
from PyQt5.QtCore import QDate
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import resources_rc
import json

class Ui_TaskFilling(object):
    def setupUi(self, TaskFilling):
        TaskFilling.setObjectName("TaskFilling")
        TaskFilling.resize(641, 785)

        self.centralwidget = QtWidgets.QWidget(TaskFilling)
        self.centralwidget.setObjectName("centralwidget")

        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 80, 621, 21))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.labelProduct = QtWidgets.QLabel(self.frame_3)
        self.labelProduct.setGeometry(QtCore.QRect(230, 0, 51, 16))
        self.labelProduct.setObjectName("labelProduct")

        self.labelQuantity = QtWidgets.QLabel(self.frame_3)
        self.labelQuantity.setGeometry(QtCore.QRect(475, 0, 61, 16))
        self.labelQuantity.setObjectName("labelQuantity")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 100, 621, 551))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 602, 549))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.layoutProducts = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.layoutProducts.setContentsMargins(5, 5, 5, 5)
        self.layoutProducts.setSpacing(5)
        self.scrollAreaWidgetContents.setLayout(self.layoutProducts)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.BtnForDeveloping = QtWidgets.QPushButton(self.centralwidget)
        self.BtnForDeveloping.setGeometry(QtCore.QRect(520, 720, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BtnForDeveloping.setFont(font)
        self.BtnForDeveloping.setObjectName("BtnForDeveloping")
        self.BtnForDeveloping.setEnabled(False)

        self.BtnBack = QtWidgets.QPushButton(self.centralwidget)
        self.BtnBack.setGeometry(QtCore.QRect(10, 720, 125, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BtnBack.setFont(font)
        self.BtnBack.setObjectName("BtnBack")

        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(10, 30, 621, 51))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")

        self.frameCustomer = QtWidgets.QFrame(self.frame_5)
        self.frameCustomer.setGeometry(QtCore.QRect(0, 0, 621, 41))
        self.frameCustomer.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border-color: rgb(0, 0, 0);")
        self.frameCustomer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCustomer.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameCustomer.setLineWidth(2)
        self.frameCustomer.setMidLineWidth(1)
        self.frameCustomer.setObjectName("frameCustomer")

        self.dateEditDate = QtWidgets.QDateEdit(self.frameCustomer)
        self.dateEditDate.setGeometry(QtCore.QRect(58, 10, 81, 22))
        self.dateEditDate.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.dateEditDate.setCalendarPopup(True)
        self.dateEditDate.setDate(QDate.currentDate())
        self.dateEditDate.setObjectName("dateEditDate")

        self.lineEditCustomer = QtWidgets.QLineEdit(self.frameCustomer)
        self.lineEditCustomer.setGeometry(QtCore.QRect(150, 10, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditCustomer.setFont(font)
        self.lineEditCustomer.setObjectName("lineEditCustomer")

        self.lineEditCheckNumber = QtWidgets.QLineEdit(self.frameCustomer)
        self.lineEditCheckNumber.setGeometry(QtCore.QRect(10, 10, 37, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditCheckNumber.setFont(font)
        self.lineEditCheckNumber.setObjectName("lineEditCheckNumber")

        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(10, 10, 561, 21))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")

        self.labelCheckNumber = QtWidgets.QLabel(self.frame_6)
        self.labelCheckNumber.setGeometry(QtCore.QRect(0, 0, 51, 16))
        self.labelCheckNumber.setObjectName("labelCheckNumber")

        self.labelDate = QtWidgets.QLabel(self.frame_6)
        self.labelDate.setGeometry(QtCore.QRect(80, 0, 31, 16))
        self.labelDate.setObjectName("labelDate")

        self.labelCustomer = QtWidgets.QLabel(self.frame_6)
        self.labelCustomer.setGeometry(QtCore.QRect(260, 0, 171, 16))
        self.labelCustomer.setObjectName("labelCustomer")

        self.BtnAddNewProduct = QtWidgets.QPushButton(self.centralwidget)
        self.BtnAddNewProduct.setGeometry(QtCore.QRect(12, 666, 123, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BtnAddNewProduct.setFont(font)
        icon1 = QtGui.QIcon()
        self.BtnAddNewProduct.setIcon(icon1)
        self.BtnAddNewProduct.setIconSize(QtCore.QSize(23, 23))
        self.BtnAddNewProduct.setObjectName("BtnAddNewProduct")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 700, 621, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.BtnSave = QtWidgets.QPushButton(self.centralwidget)
        self.BtnSave.setGeometry(QtCore.QRect(396, 720, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BtnSave.setFont(font)
        self.BtnSave.setObjectName("BtnForDeveloping_2")

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
        self.labelQuantity.setText(_translate("TaskFilling", "Количество"))
        self.labelCheckNumber.setText(_translate("TaskFilling", "№ счёта"))
        self.labelDate.setText(_translate("TaskFilling", "Дата"))
        self.labelCustomer.setText(_translate("TaskFilling", "Название организации заказчика"))
        self.BtnAddNewProduct.setText(_translate("TaskFilling", "Добавить изделие"))
        self.BtnForDeveloping.setText(_translate("TaskFilling", "На разработку"))
        self.BtnBack.setText(_translate("TaskFilling", "Назад"))
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
        self.ui.BtnBack.clicked.connect(self.back_main_manager_window)
        self.ui.BtnSave.clicked.connect(self.add_task)
        self.ui.BtnSave.clicked.connect(self.clearLineEdit)
        self.ui.BtnSave.clicked.connect(self.clear_products)

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
        # Сбор данных для заказчика и задания
        customer_and_task_data = {
            "invoice_number": self.ui.lineEditCheckNumber.text(),
            "order_date": self.ui.dateEditDate.date().toString("yyyy-MM-dd"),
            "organization_name": self.ui.lineEditCustomer.text(),
        }
        print("Отправляемые данные:", customer_and_task_data)

        # Проверка, что все поля заполнены
        if not all(customer_and_task_data.values()):
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Заполните все поля корректно.")
            return

        try:
            # Отправка первого запроса
            response = requests.post(
                "http://127.0.0.1:8000/orders/add_customer_and_task/",
                json=customer_and_task_data
            )
            if response.status_code == 201:
                task_id = response.json().get("task_id")
                if not task_id:
                    QtWidgets.QMessageBox.warning(self, "Ошибка", "Не удалось получить ID задания.")
                    return

                # Сбор данных о продуктах
                product_data_list = self.collect_product_data(task_id)

                # Проверка, что данные о продуктах корректны
                if not product_data_list:
                    QtWidgets.QMessageBox.warning(self, "Ошибка", "Добавьте хотя бы один продукт и заполните все поля.")
                    return

                # Отправка данных о продуктах
                for product_data in product_data_list:
                    response = requests.post("http://127.0.0.1:8000/products/add_product/", json=product_data)
                    if response.status_code != 201:
                        QtWidgets.QMessageBox.warning(
                            self,
                            "Ошибка",
                            f"Ошибка при добавлении продукта: {response.text}"
                        )
                        return

                self.enable_for_developing_button()  #Активация кнопки "На разработку"
                QtWidgets.QMessageBox.information(self, "Успех", "Данные успешно добавлены!")
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

    def clearLineEdit(self):
        self.ui.lineEditCustomer.clear()
        check_number = self.get_max_value_from_database("orders_task", "invoice_number")
        self.ui.lineEditCheckNumber.setText(str(check_number + 1))

    def clear_layout(self, layout):
        # Очищает все элементы в layout
        if layout is not None:
            for i in range(layout.count()):
                item = layout.itemAt(i)
                if item is not None:
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()  # Удаляем виджет
                    else:
                        # Если это подмакет, рекурсивно очищаем его
                        sub_layout = item.layout()
                        if sub_layout is not None:
                            self.clear_layout(sub_layout)

    def clear_products(self):
        # Очищает все строки продуктов в layout
        self.clear_layout(self.ui.layoutProducts)
        self.ui.layoutProducts.update()  # Обновляем layout после очистки

    def back_main_manager_window(self):
            # Возврат к главному окну менеджера
            from windows.main_manager_window import MainWindowManager
            self.main_manager_window = MainWindowManager()
            self.main_manager_window.show()
            self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = TaskFilling()
    main_window.show()
    sys.exit(app.exec_())

