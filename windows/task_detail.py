from PyQt5 import QtWidgets

class Ui_TaskDetail:
    def setupUi(self, Dialog):
        Dialog.setWindowTitle("Детали задания")
        Dialog.setGeometry(100, 100, 400, 300)

        # Создаем layout для окна
        self.layout = QtWidgets.QVBoxLayout(Dialog)

        # Добавляем информацию о задании
        self.label_invoice_number = QtWidgets.QLabel()
        self.label_customer_name = QtWidgets.QLabel()
        self.label_order_date = QtWidgets.QLabel()

        # Добавляем лейблы в layout
        self.layout.addWidget(self.label_invoice_number)
        self.layout.addWidget(self.label_customer_name)
        self.layout.addWidget(self.label_order_date)

        # Добавляем информацию о продуктах
        self.label_products = QtWidgets.QLabel("Изделия:")
        self.layout.addWidget(self.label_products)

        # Создаем список для изделий
        self.products_list = QtWidgets.QVBoxLayout()
        self.layout.addLayout(self.products_list)

        # Кнопка закрытия окна
        self.btn_close = QtWidgets.QPushButton("Закрыть")
        self.layout.addWidget(self.btn_close)

class TaskDetail(QtWidgets.QDialog):
    def __init__(self, task_data):
        super().__init__()

        # Создаем экземпляр Ui_TaskDetail и настраиваем интерфейс
        self.ui = Ui_TaskDetail()
        self.ui.setupUi(self)

        # Заполняем интерфейс данными
        self.ui.label_invoice_number.setText(f"Номер счета: {task_data['invoice_number']}")
        self.ui.label_customer_name.setText(f"Имя заказчика: {task_data.get('customer_name', 'Неизвестно')}")
        self.ui.label_order_date.setText(f"Дата заказа: {task_data['order_invoice_date']}")

        # Добавляем информацию о продуктах
        for product in task_data.get('products', []):
            product_label = QtWidgets.QLabel(f"{product['name']} - Количество: {product['quantity']}")
            self.ui.products_list.addWidget(product_label)

        # Подключаем кнопку закрытия
        self.ui.btn_close.clicked.connect(self.close)