from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

from order_dev.order_dev_main import OrderDev


class Ui_NewTasks(object):
    def setupUi(self, NewTasks):
        NewTasks.setObjectName("NewTasks")
        NewTasks.resize(1006, 650)

        self.centralwidget = QtWidgets.QWidget(NewTasks)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 986, 593))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Создаем кнопку и сохраняем ссылку на нее
        self.pushButton_new_task = QtWidgets.QPushButton("Новое задание")
        self.verticalLayout_2.addWidget(self.pushButton_new_task)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        NewTasks.setCentralWidget(self.centralwidget)


class NewTasks(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_NewTasks()
        self.ui.setupUi(self)
        self.parent = parent  # Сохраняем ссылку на родительское окно

        # Подключаем обработчик нажатия на кнопку
        self.ui.pushButton_new_task.clicked.connect(self.open_new_window)

    # def open_new_window(self):
    #     """Метод для открытия нового окна"""
    #     self.parent.switch_window(self.parent.order_dev_window)  # Переключаемся на OrderDev

    def open_new_window(self):
        """Метод для открытия нового окна"""
        # Пример данных о задании, которые можно получить из базы данных
        task_data = {
            'invoice_number': '143',
            'customer_name': 'ООО "Белагро Бел"',
            'order_invoice_date': '26.07.2024'
        }
        # self.new_window = OrderDev(task_data)  # Передаем данные о задании
        # self.new_window.show()  # Показываем новое окно
        self.parent.switch_window(self.parent.order_dev_window)  # Переключаемся на OrderDev

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    NewOrders = NewTasks()  # Создаем экземпляр NewTasks
    NewOrders.show()
    sys.exit(app.exec_())

