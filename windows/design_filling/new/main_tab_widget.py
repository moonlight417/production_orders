import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QPushButton,
    QLabel, QScrollArea, QFrame, QMessageBox, QInputDialog, QRadioButton, QCheckBox
)
from PyQt5.QtCore import Qt
from functools import partial
from tags_tab_content import TagsTabContent
from inner_tab_widget import InnerTabWidget
from rename_tab_dialog import RenameTabDialog


class MainTabWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Основной виджет с вкладками
        self.main_tab_widget = QTabWidget()

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
        layout.addWidget(self.main_tab_widget)

        # Словари для хранения областей прокрутки и типов вкладок
        self.scroll_areas = {}
        self.tab_types = {}
        self.check_boxes = {}  # Связывает вкладки с чекбоксами
        self.radio_buttons = {}  # Связывает вкладки с радиокнопками

        # Добавляем защищенные вкладки
        self.add_protected_tabs()

    def add_protected_tabs(self):
        """Добавляет защищённые вкладки."""
        tags_tab = TagsTabContent()
        self.main_tab_widget.addTab(tags_tab, "Теги")

        # Инициализируем множество защищённых вкладок и добавляем вкладку "Теги"
        self.protected_tabs = {tags_tab}

    def add_assembly_unit_tab(self):
        """Добавляет новую вкладку с названием 'Сборочная единица'."""
        self._add_tab("Сборочная единица")

    def add_detail_tab(self):
        """Добавляет новую вкладку с названием 'Деталь'."""

        self._add_tab("Деталь")

    # def add_assembly_unit_tab(self):
    #     tab = InnerTabWidget()
    #     tab_name = f"Сборочная единица {self.main_tab_widget.count() + 1}"
    #     self.main_tab_widget.addTab(tab, tab_name)
    #     new_index = self.main_tab_widget.count() - 1
    #     self.main_tab_widget.setCurrentIndex(new_index)
    #
    # def add_detail_tab(self):
    #     tab = InnerTabWidget()
    #     self.main_tab_widget.addTab(tab, "Деталь")
    #     new_index = self.main_tab_widget.count() - 1
    #     self.main_tab_widget.setCurrentIndex(new_index)

    def _add_tab(self, tab_name):
        """Создаёт вкладку с указанным названием."""
        tab = QWidget()

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedWidth(200)
        scroll_frame = QFrame()
        scroll_layout = QVBoxLayout(scroll_frame)
        scroll_layout.setAlignment(Qt.AlignTop)
        scroll_area.setWidget(scroll_frame)

        tab_layout = QVBoxLayout(tab)
        check_box = QCheckBox("Принадлежность к СБ", self)
        button_refresh = QPushButton("Обновить")
        button_refresh.clicked.connect(partial(self.check_and_disable, tab))

        tab_layout.addWidget(check_box)
        tab_layout.addWidget(button_refresh)
        tab_layout.addWidget(scroll_area)

        self.main_tab_widget.addTab(tab, tab_name)
        new_index = self.main_tab_widget.count() - 1
        self.main_tab_widget.setCurrentIndex(new_index)

        self.scroll_areas[tab] = scroll_layout
        self.tab_types[tab] = tab_name
        self.check_boxes[tab] = check_box
        self.radio_buttons[tab] = []

        # Обновляем области прокрутки
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

        tab = self.main_tab_widget.widget(current_index)
        if tab in self.protected_tabs:
            QMessageBox.warning(self, "Предупреждение", "Нельзя удалить защищённую вкладку.")
            return

        self.main_tab_widget.removeTab(current_index)

        if tab in self.scroll_areas:
            del self.scroll_areas[tab]
        if tab in self.tab_types:
            del self.tab_types[tab]
        if tab in self.check_boxes:
            del self.check_boxes[tab]
        if tab in self.radio_buttons:
            del self.radio_buttons[tab]

        self.update_scroll_areas()

    def update_scroll_areas(self):
        """Обновляет содержимое всех областей прокрутки."""
        tab_names = [
            self.main_tab_widget.tabText(i)
            for i in range(self.main_tab_widget.count())
            if self.tab_types.get(self.main_tab_widget.widget(i)) == "Сборочная единица"
        ]

        for tab, scroll_layout in self.scroll_areas.items():
            # Удаляем старые радиокнопки
            for i in reversed(range(scroll_layout.count())):
                item = scroll_layout.itemAt(i)
                if item and item.widget():
                    item.widget().deleteLater()

            # Добавляем новые радиокнопки
            self.radio_buttons[tab] = []
            for name in tab_names:
                radio_button = QRadioButton(name, self)
                radio_button.setEnabled(self.check_boxes[tab].isChecked())
                scroll_layout.addWidget(radio_button)
                self.radio_buttons[tab].append(radio_button)

    def check_and_disable(self, tab):
        """Обновляет состояние радиокнопок в зависимости от состояния чекбокса."""
        is_checked = self.check_boxes[tab].isChecked()
        for radio_button in self.radio_buttons[tab]:
            radio_button.setEnabled(is_checked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainTabWidget()
    window.show()
    sys.exit(app.exec_())

