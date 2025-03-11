from PyQt5 import QtWidgets

class TaskDetail(QtWidgets.QDialog):
    def __init__(self, task_data):
        super().__init__()
        self.setWindowTitle("Детали задания")
        self.setGeometry(100, 100, 400, 300)

        # Создаем layout для окна
        self.layout = QtWidgets.QVBoxLayout(self)

        # Добавляем информацию о задании
        self.label_invoice_number = QtWidgets.QLabel(f"Номер счета: {task_data['invoice_number']}")
        self.label_customer_name = QtWidgets.QLabel(f"Имя заказчика: {task_data.get('customer_name', 'Неизвестно')}")
        self.label_order_date = QtWidgets.QLabel(f"Дата заказа: {task_data['order_invoice_date']}")

        # Добавляем лейблы в layout
        self.layout.addWidget(self.label_invoice_number)
        self.layout.addWidget(self.label_customer_name)
        self.layout.addWidget(self.label_order_date)

        # Добавляем информацию о продуктах
        self.label_products = QtWidgets.QLabel("Изделия:")
        self.layout.addWidget(self.label_products)

        # Создаем список для изделий
        self.products_list = QtWidgets.QVBoxLayout()
        for product in task_data.get('products', []):
            product_label = QtWidgets.QLabel(f"{product['name']} - Количество: {product['quantity']}")
            self.products_list.addWidget(product_label)

        self.layout.addLayout(self.products_list)

        # Кнопка закрытия окна
        self.btn_close = QtWidgets.QPushButton("Закрыть")
        self.btn_close.clicked.connect(self.close)
        self.layout.addWidget(self.btn_close)