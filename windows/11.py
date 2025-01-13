from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui_design_document_filling_form import Ui_DesignDocumentFillingForm
from image_handler import ImageHandler
from tab_manager import TabManager
from printer import PrintDialog
import sys

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QPushButton,
    QLabel, QScrollArea, QFrame, QMessageBox, QVBoxLayout, QRadioButton
)
from PyQt5.QtCore import pyqtSignal

class CustomTabWidget(QTabWidget):
    tab_closed = pyqtSignal(int)  # Сигнал для передачи индекса закрытой вкладки

    def __init__(self):
        super().__init__()

    def close_current_tab(self):
        index = self.currentIndex()
        if index != -1 and (not hasattr(self, 'protected_tabs') or index not in self.protected_tabs):
            self.removeTab(index)
            self.tab_closed.emit(index)  # Испускаем сигнал о закрытии вкладки
        else:
            QMessageBox.warning(self, "Предупреждение", "Нельзя удалить защищённую вкладку.")

class MainTabWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Основной виджет с вкладками
        self.main_tab_widget = CustomTabWidget()
        self.main_tab_widget.tab_closed.connect(self.remove_from_scroll_area)  # Подключаем сигнал

        # Кнопки для управления вкладками
        button_layout = QHBoxLayout()
        add_tab_button = QPushButton("Добавить сборочную единицу")
        add_tab_button.clicked.connect(self.add_assembly_unit_tab)
        close_tab_button = QPushButton("Закрыть текущую вкладку")
        close_tab_button.clicked.connect(self.main_tab_widget.close_current_tab)

        button_layout.addWidget(add_tab_button)
        button_layout.addWidget(close_tab_button)

        # Область прокрутки для отображения названий вкладок
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_frame = QFrame()
        self.scroll_layout = QVBoxLayout(scroll_frame)
        scroll_area.setWidget(scroll_frame)

        layout.addLayout(button_layout)
        layout.addWidget(self.main_tab_widget)
        layout.addWidget(scroll_area)

    def add_assembly_unit_tab(self):
        """Добавляет новую вкладку с названием 'Сборочная единица'."""
        tab = QWidget()  # Заглушка для содержимого вкладки
        tab_name = "Сборочная единица"
        self.main_tab_widget.addTab(tab, tab_name)

        # Делаем новую вкладку текущей
        new_index = self.main_tab_widget.count() - 1
        self.main_tab_widget.setCurrentIndex(new_index)

        # Добавляем название вкладки в scroll_area
        self.add_to_scroll_area(tab_name)

    def add_to_scroll_area(self, tab_name):
        """Добавляет название вкладки в scroll_area."""
        # Создание радиокнопок
        self.radio_button1 = QRadioButton(tab_name)

        # label = QLabel(tab_name)
        self.radio_button1.setObjectName(f"tab_label_{self.main_tab_widget.count() - 1}")
        self.scroll_layout.addWidget(self.radio_button1)

    def remove_from_scroll_area(self, index):
        """Удаляет элемент из scroll_area по индексу вкладки."""
        item = self.scroll_layout.itemAt(index)
        if item:
            widget = item.widget()
            if widget:
                widget.deleteLater()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainTabWidget()
    window.show()
    sys.exit(app.exec_())
