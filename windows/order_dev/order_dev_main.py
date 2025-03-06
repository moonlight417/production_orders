import sys
from PyQt5 import QtWidgets
from .ui_order_dev import Ui_OrderDev

class OrderDev(QtWidgets.QMainWindow):
    def __init__(self, task_data=None):
        super().__init__()
        self.ui = Ui_OrderDev()
        self.ui.setupUi(self)

        if task_data:
            self.populate_task_data(task_data)

    def populate_task_data(self, task_data):
        """Заполняет лейблы данными о задании."""
        self.ui.label_check_number.setText(str(task_data['invoice_number']))  # Номер счета
        self.ui.label_customer.setText(task_data['customer_name'])  # Имя заказчика
        self.ui.label_date_of_task.setText(task_data['order_invoice_date'])  # Дата заказа
        # Добавьте другие поля по мере необходимости


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_OrderDev()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())