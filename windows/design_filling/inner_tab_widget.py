from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMessageBox
from .custom_tab_widget import CustomTabWidget
from .drawing_widget import DrawingWidget

class InnerTabWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        self.inner_tab_widget = CustomTabWidget()

        add_button = QPushButton("Добавить лист")
        add_button.clicked.connect(self.add_inner_tab)

        layout.addWidget(add_button)
        layout.addWidget(self.inner_tab_widget)
        self.setLayout(layout)

    def add_inner_tab(self):
        tab = QWidget()
        tab_layout = QVBoxLayout(tab)
        drawing_widget = DrawingWidget()

        # Подключаем сигнал к методу удаления вкладки
        drawing_widget.tabCloseRequested.connect(self.delete_current_inner_tab)

        tab_layout.addWidget(drawing_widget)

        self.sheet_number = self.inner_tab_widget.count() + 1

        tab_name = f"Лист {self.sheet_number}"
        self.inner_tab_widget.addTab(tab, tab_name)

    def delete_current_inner_tab(self):
        """
        Удаляет текущую вкладку (лист).
        """
        current_index = self.inner_tab_widget.currentIndex()

        if current_index != -1:
            print(f"Удаляем вкладку с индексом: {current_index}")
            self.inner_tab_widget.removeTab(current_index)
            QMessageBox.information(self, "Удаление", "Текущий лист был удалён.")
        else:
            QMessageBox.warning(self, "Ошибка", "Нет вкладки для удаления.")



