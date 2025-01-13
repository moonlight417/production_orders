from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui_design_document_filling_form import Ui_DesignDocumentFillingForm
from image_handler import ImageHandler
from tab_manager import TabManager
from printer import PrintDialog
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QPushButton,
    QLabel, QScrollArea, QFrame, QMessageBox, QInputDialog, QRadioButton, QCheckBox
)
from PyQt5.QtCore import pyqtSignal, Qt


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
        self.main_tab_widget.tab_closed.connect(self.remove_from_scroll_area)

        # Кнопки для управления вкладками
        button_layout = QHBoxLayout()
        add_assembly_button = QPushButton("+СБ")
        add_assembly_button.clicked.connect(self.add_assembly_unit_tab)

        add_detail_button = QPushButton("+ Деталь")
        add_detail_button.clicked.connect(self.add_detail_tab)

        rename_tab_button = QPushButton("Переименовать вкладку")
        rename_tab_button.clicked.connect(self.rename_current_tab)

        close_tab_button = QPushButton("Закрыть текущую вкладку")
        close_tab_button.clicked.connect(self.main_tab_widget.close_current_tab)

        button_layout.addWidget(add_assembly_button)
        button_layout.addWidget(add_detail_button)
        button_layout.addWidget(rename_tab_button)
        button_layout.addWidget(close_tab_button)

        layout.addLayout(button_layout)
        layout.addWidget(self.main_tab_widget)

        # Список для хранения областей прокрутки каждой вкладки
        self.scroll_areas = {}
        # Список для хранения типов вкладок
        self.tab_types = {}

    def add_assembly_unit_tab(self):
        """Добавляет новую вкладку с названием 'Сборочная единица'."""
        tab = QWidget()
        tab_name = "Сборочная единица"

        # Создаём область прокрутки для вкладки
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_frame = QFrame()
        scroll_layout = QVBoxLayout(scroll_frame)
        scroll_area.setWidget(scroll_frame)

        tab_layout = QVBoxLayout(tab)
        self.check_box = QCheckBox("Принадлежность к СБ", self)
        tab_layout.addWidget(self.check_box)
        tab_layout.addWidget(scroll_area)

        self.main_tab_widget.addTab(tab, tab_name)

        # Делаем новую вкладку текущей
        new_index = self.main_tab_widget.count() - 1
        self.main_tab_widget.setCurrentIndex(new_index)

        # Сохраняем область прокрутки для обновления
        self.scroll_areas[new_index] = scroll_layout
        self.tab_types[new_index] = "Сборочная единица"  # Запоминаем тип вкладки

        # Обновляем все области прокрутки
        self.update_scroll_areas()

    def add_detail_tab(self):
        """Добавляет новую вкладку с названием 'Деталь'."""
        tab = QWidget()
        tab_name = "Деталь"

        # Создаём область прокрутки для вкладки
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_frame = QFrame()
        scroll_layout = QVBoxLayout(scroll_frame)
        scroll_area.setWidget(scroll_frame)

        tab_layout = QVBoxLayout(tab)
        self.check_box = QCheckBox("Принадлежность к СБ", self)
        tab_layout.addWidget(self.check_box)
        tab_layout.addWidget(scroll_area)

        self.main_tab_widget.addTab(tab, tab_name)

        # Делаем новую вкладку текущей
        new_index = self.main_tab_widget.count() - 1
        self.main_tab_widget.setCurrentIndex(new_index)

        # Сохраняем область прокрутки для обновления
        self.scroll_areas[new_index] = scroll_layout
        self.tab_types[new_index] = "Деталь"  # Запоминаем тип вкладки

        # Обновляем все области прокрутки
        self.update_scroll_areas()

    def rename_current_tab(self):
        """Переименовывает текущую вкладку и обновляет области прокрутки."""
        current_index = self.main_tab_widget.currentIndex()
        if current_index == -1:
            QMessageBox.warning(self, "Предупреждение", "Выберите вкладку для переименования.")
            return

        current_name = self.main_tab_widget.tabText(current_index)
        new_name, ok = QInputDialog.getText(self, "Переименовать вкладку", "Введите новое название:", text=current_name)

        if ok and new_name:
            self.main_tab_widget.setTabText(current_index, new_name)

            # Обновляем область прокрутки для переименованной вкладки
            self.update_scroll_areas()

        elif not new_name:
            QMessageBox.warning(self, "Предупреждение", "Название не может быть пустым.")

    def update_scroll_areas(self):
        """Обновляет содержимое всех областей прокрутки."""
        # Получаем актуальный список всех вкладок, исключая те, которые называются "Деталь"
        tab_names = [
            self.main_tab_widget.tabText(i)
            for i in range(self.main_tab_widget.count())
            if self.main_tab_widget.tabText(i) != "Деталь"  # Исключаем "Деталь"
        ]

        # Обновляем области прокрутки для вкладок с типом "Сборочная единица"
        for index, scroll_layout in self.scroll_areas.items():
            # Очищаем текущий layout
            for i in reversed(range(scroll_layout.count())):
                item = scroll_layout.itemAt(i)
                if item and item.widget():
                    item.widget().deleteLater()

            # Добавляем актуальный список названий вкладок
            for name in tab_names:
                self.radio_button1 = QRadioButton(name, self)
                label = QLabel(name)
                scroll_layout.addWidget(self.radio_button1)


    def remove_from_scroll_area(self, index):
        """Удаляет область прокрутки при закрытии вкладки."""
        if index in self.scroll_areas:
            del self.scroll_areas[index]
        self.update_scroll_areas()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainTabWidget()
    window.show()
    sys.exit(app.exec_())



