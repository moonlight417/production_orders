
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import requests


class Ui_NewTasks(object):
    def setupUi(self, NewTasks):
        NewTasks.setObjectName("NewTasks")
        NewTasks.resize(1006, 650)

        self.centralwidget = QtWidgets.QWidget(NewTasks)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)

        self.verticalLayout.addWidget(self.widget)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 986, 593))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.empty_task = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.empty_task.setMinimumSize(QtCore.QSize(0, 60))
        self.empty_task.setAutoFillBackground(False)
        self.empty_task.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.empty_task.setObjectName("empty_task")
        self.verticalLayout_2.addWidget(self.empty_task)

        spacerItem = QtWidgets.QSpacerItem(20, 506, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        NewTasks.setCentralWidget(self.centralwidget)

        self.retranslateUi(NewTasks)
        QtCore.QMetaObject.connectSlotsByName(NewTasks)

    def retranslateUi(self, NewOrders):
        _translate = QtCore.QCoreApplication.translate
        NewOrders.setWindowTitle(_translate("NewTasks", "Новые заказы"))
        self.label_3.setText(_translate("NewTasks", "Новые задания на разработку заказа"))

class NewTasks(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_NewTasks()
        self.ui.setupUi(self)
        self.parent = parent  # Сохраняем ссылку на родительское окно

        # self.update_task_list()

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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewOrders = QtWidgets.QMainWindow()
    ui = Ui_NewTasks()
    ui.setupUi(NewOrders)
    NewOrders.show()
    sys.exit(app.exec_())
