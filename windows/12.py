from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QPushButton,
    QLabel, QScrollArea, QFrame, QMessageBox, QInputDialog, QRadioButton
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
        # Список для хранения кнопок каждой вкладки
        self.activate_buttons = {}
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
        activate_button = QPushButton("Активировать принадлежность к СБ", self)
        tab_layout.addWidget(activate_button)
        tab_layout.addWidget(scroll_area)

        self.main_tab_widget.addTab(tab, tab_name)

        # Делаем новую вкладку текущей
        new_index = self.main_tab_widget.count() - 1
        self.main_tab_widget.setCurrentIndex(new_index)

        # Сохраняем область прокрутки для обновления
        self.scroll_areas[new_index] = scroll_layout
        self.tab_types[new_index] = "Сборочная единица"  # Запоминаем тип вкладки
        self.activate_buttons[new_index] = activate_button  # Сохраняем кнопку для этой вкладки

        # Подключаем сигнал для активации кнопки
        activate_button.clicked.connect(lambda: self.update_scroll_areas(new_index, True))

        # Обновляем все области прокрутки
        self.update_scroll_areas(new_index, False)

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
        activate_button = QPushButton("Активировать принадлежность к СБ", self)
        tab_layout.addWidget(activate_button)
        tab_layout.addWidget(scroll_area)

        self.main_tab_widget.addTab(tab, tab_name)

        # Делаем новую вкладку текущей
        new_index = self.main_tab_widget.count() - 1
        self.main_tab_widget.setCurrentIndex(new_index)

        # Сохраняем область прокрутки для обновления
        self.scroll_areas[new_index] = scroll_layout
        self.tab_types[new_index] = "Деталь"  # Запоминаем тип вкладки
        self.activate_buttons[new_index] = activate_button  # Сохраняем кнопку для этой вкладки

        # Подключаем сигнал для активации кнопки
        activate_button.clicked.connect(lambda: self.update_scroll_areas(new_index, True))

        # Обновляем все области прокрутки
        self.update_scroll_areas(new_index, False)

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
            self.update_scroll_areas(current_index, False)

        elif not new_name:
            QMessageBox.warning(self, "Предупреждение", "Название не может быть пустым.")

    def update_scroll_areas(self, index, is_active):
        """Обновляет содержимое области прокрутки в зависимости от активации кнопки в своей вкладке."""
        scroll_layout = self.scroll_areas.get(index)
        if not scroll_layout:
            return

        # Очищаем текущий layout
        for i in reversed(range(scroll_layout.count())):
            item = scroll_layout.itemAt(i)
            if item and item.widget():
                item.widget().deleteLater()

        if is_active:
            # Добавляем радиокнопки только для текущей вкладки
            tab_names = [
                self.main_tab_widget.tabText(i)
                for i in range(self.main_tab_widget.count())
                if i != index and self.tab_types[i] == "Сборочная единица"  # Исключаем текущую вкладку и "Деталь"
            ]

            for name in tab_names:
                radio_button = QRadioButton(name, self)
                scroll_layout.addWidget(radio_button)

    def remove_from_scroll_area(self, index):
        """Удаляет область прокрутки и связанные данные при закрытии вкладки."""
        if index in self.scroll_areas:
            del self.scroll_areas[index]
        if index in self.tab_types:
            del self.tab_types[index]
        if index in self.activate_buttons:
            del self.activate_buttons[index]

        # Обновляем оставшиеся вкладки
        self.update_scroll_areas(index, False)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainTabWidget()
    window.show()
    sys.exit(app.exec_())


