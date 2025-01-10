from PyQt5 import QtWidgets


class ExampleApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример с добавлением вкладок")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QtWidgets.QVBoxLayout(self)

        # Основное окно с вкладками
        self.tab_widget = QtWidgets.QTabWidget()
        self.layout.addWidget(self.tab_widget)

        # Кнопки для добавления новых вкладок
        self.add_detail_button = QtWidgets.QPushButton("Добавить вкладку 'Деталь'")
        self.add_detail_button.clicked.connect(self.add_detail_tab)
        self.layout.addWidget(self.add_detail_button)

        self.add_assembly_button = QtWidgets.QPushButton("Добавить вкладку 'Сборочная единица'")
        self.add_assembly_button.clicked.connect(self.add_assembly_unit_tab)
        self.layout.addWidget(self.add_assembly_button)

        # Создаем постоянную вкладку "Деталь"
        self.tab_detail = self.create_permanent_detail_tab()
        self.tab_widget.addTab(self.tab_detail, "Деталь")

    def create_permanent_detail_tab(self):
        # Постоянная вкладка "Деталь", которая будет копироваться
        tab_widget = QtWidgets.QWidget()
        tab_layout = QtWidgets.QVBoxLayout(tab_widget)

        # Добавим элементы в постоянную вкладку
        self.label = QtWidgets.QLabel("Постоянная вкладка: Деталь")
        self.input_field = QtWidgets.QLineEdit()
        self.input_field.setPlaceholderText("Введите данные детали")

        tab_layout.addWidget(self.label)
        tab_layout.addWidget(self.input_field)

        return tab_widget

    def add_detail_tab(self):
        # Копируем содержимое вкладки "Деталь" в новую вкладку
        new_tab = QtWidgets.QWidget()
        new_tab_layout = QtWidgets.QVBoxLayout(new_tab)

        # Копируем все виджеты с вкладки self.tab_detail в новый layout
        for widget in self.tab_detail.findChildren(QtWidgets.QWidget):
            new_widget = widget.__class__()
            new_widget.setText(widget.text()) if isinstance(widget, QtWidgets.QLabel) else None
            new_input_field = QtWidgets.QLineEdit()
            new_input_field.setPlaceholderText(self.input_field.placeholderText()) if isinstance(widget,
                                                                                                 QtWidgets.QLineEdit) else None
            new_tab_layout.addWidget(new_widget)

        # Добавляем новый таб в основной tab_widget
        tab_index = self.tab_widget.addTab(new_tab, "Деталь")
        self.tab_widget.setCurrentIndex(tab_index)

    def add_assembly_unit_tab(self):
        # Копируем содержимое вкладки "Деталь" в новую вкладку для сборочной единицы
        new_tab = QtWidgets.QWidget()
        new_tab_layout = QtWidgets.QVBoxLayout(new_tab)

        # Копируем все виджеты с вкладки self.tab_detail в новый layout
        for widget in self.tab_detail.findChildren(QtWidgets.QWidget):
            new_widget = widget.__class__()
            new_widget.setText(widget.text()) if isinstance(widget, QtWidgets.QLabel) else None
            new_input_field = QtWidgets.QLineEdit()
            new_input_field.setPlaceholderText(self.input_field.placeholderText()) if isinstance(widget,
                                                                                                 QtWidgets.QLineEdit) else None
            new_tab_layout.addWidget(new_widget)

        # Добавляем новый таб в основной tab_widget
        tab_index = self.tab_widget.addTab(new_tab, "Сборочная единица")
        self.tab_widget.setCurrentIndex(tab_index)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = ExampleApp()
    window.show()
    app.exec_()
