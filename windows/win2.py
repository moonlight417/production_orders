import requests
from PyQt5 import QtWidgets
import sys


class DetailsWindow(QtWidgets.QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Детали заказчика")
        layout = QtWidgets.QVBoxLayout()
        if self.data:
            for item in self.data:
                label = QtWidgets.QLabel(
                    f"Наименование продукта: {item['name']}\n"
                    f"Количество: {item['quantity_in_task']}\n"
                    f"Дата заявки: {item['order_date']}\n"
                )
                layout.addWidget(label)
        else:
            layout.addWidget(QtWidgets.QLabel("Нет данных для отображения."))
        self.setLayout(layout)
