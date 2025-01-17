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
from PyQt5.QtCore import Qt


class MainTabWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Основной виджет с вкладками
        self.main_tab_widget = QTabWidget()
        layout.addWidget(self.main_tab_widget)

        # Кнопки для управления вкладками
        button_layout = QHBoxLayout()
        add_assembly_button = QPushButton("+СБ")
        add_assembly_button.clicked.connect(self.add_assembly_unit_tab)

        add_detail_button = QPushButton("+ Деталь")
        add_detail_button.clicked.connect(self.add_detail_tab)

        rename_tab_button = QPushButton("Переименовать вкладку")
        rename_tab_button.clicked.connect(self.rename_current_tab)

        close_tab_button = QPushButton("Закрыть текущую вкладку")
        close_tab_button.clicked.connect(self.close_current_tab)

        button_layout.addWidget(add_assembly_button)
        button_layout.addWidget(add_detail_button)
        button_layout.addWidget(rename_tab_button)
        button_layout.addWidget(close_tab_button)

        layout.addLayout(button_layout)

        # Словари для хранения областей прокрутки и типов вкладок
        self.scroll_areas = {}
        self.tab_types = {}

    def add_assembly_unit_tab(self):
        """Добавляет новую вкладку с названием 'Сборочная единица'."""
        tab = QWidget()
        tab_name = "Сборочная единица"

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_frame = QFrame()
        scroll_layout = QVBoxLayout(scroll_frame)
        scroll_area.setWidget(scroll_frame)

        tab_layout = QVBoxLayout(tab)
        check_box = QCheckBox("Принадлежность к СБ", self)
        tab_layout.addWidget(check_box)
        tab_layout.addWidget(scroll_area)

        self.main_tab_widget.addTab(tab, tab_name)
        new_index = self.main_tab_widget.count() - 1
        self.main_tab_widget.setCurrentIndex(new_index)

        self.scroll_areas[tab] = scroll_layout
        self.tab_types[tab] = "Сборочная единица"  # Храним тип вкладки как значение, а объект вкладки как ключ
        self.update_scroll_areas()

    def add_detail_tab(self):
        """Добавляет новую вкладку с названием 'Деталь'."""
        tab = QWidget()
        tab_name = "Деталь"

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_frame = QFrame()
        scroll_layout = QVBoxLayout(scroll_frame)
        scroll_area.setWidget(scroll_frame)

        tab_layout = QVBoxLayout(tab)
        check_box = QCheckBox("Принадлежность к СБ", self)
        tab_layout.addWidget(check_box)
        tab_layout.addWidget(scroll_area)

        self.main_tab_widget.addTab(tab, tab_name)
        new_index = self.main_tab_widget.count() - 1
        self.main_tab_widget.setCurrentIndex(new_index)

        self.scroll_areas[tab] = scroll_layout
        self.tab_types[tab] = "Деталь"  # Храним тип вкладки как значение, а объект вкладки как ключ
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
            self.update_scroll_areas()
        elif not new_name:
            QMessageBox.warning(self, "Предупреждение", "Название не может быть пустым.")

    def close_current_tab(self):
        """Закрывает текущую вкладку, если она не защищённая."""
        current_index = self.main_tab_widget.currentIndex()
        if current_index == -1:
            return

        # Проверяем, можно ли закрыть вкладку
        if not hasattr(self, 'protected_tabs') or current_index not in self.protected_tabs:
            self.main_tab_widget.removeTab(current_index)

            # Удаляем область прокрутки из словаря
            if current_index in self.scroll_areas:
                del self.scroll_areas[current_index]
            self.update_scroll_areas()
        else:
            QMessageBox.warning(self, "Предупреждение", "Нельзя удалить защищённую вкладку.")

    def update_scroll_areas(self):
        """Обновляет содержимое всех областей прокрутки."""
        tab_names = [
            self.main_tab_widget.tabText(i)
            for i in range(self.main_tab_widget.count())
            if self.tab_types.get(self.main_tab_widget.widget(i)) == "Сборочная единица"
        ]

        for scroll_layout in self.scroll_areas.values():
            for i in reversed(range(scroll_layout.count())):
                item = scroll_layout.itemAt(i)
                if item and item.widget():
                    item.widget().deleteLater()

            for name in tab_names:
                radio_button = QRadioButton(name, self)
                scroll_layout.addWidget(radio_button)

    def remove_from_scroll_area(self, index):
        """Удаляет область прокрутки при закрытии вкладки."""
        tab = self.main_tab_widget.widget(index)
        if tab in self.scroll_areas:
            del self.scroll_areas[tab]
        if tab in self.tab_types:
            del self.tab_types[tab]
        self.update_scroll_areas()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainTabWidget()
    window.show()
    sys.exit(app.exec_())






