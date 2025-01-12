from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout, QDialog, \
    QMessageBox, QLineEdit, QTabBar, QSizePolicy, QCheckBox
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QPixmap, QTransform, QPainter
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets
from gui.ui_design_document_filling_form import Ui_DesignDocumentFillingForm

class PrintDialog(QDialog):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.image_path = image_path
        self.init_ui()

    def init_ui(self):
        printer = QPrinter()
        print_dialog = QPrintDialog(printer, self)

        if print_dialog.exec_() == QPrintDialog.Accepted:
            self.print_image(printer)

    def print_image(self, printer):
        pixmap = QPixmap(self.image_path)

        if pixmap.isNull():
            QMessageBox.critical(self, "Ошибка", "Невозможно загрузить изображение для печати.")
            return

        painter = QPainter(printer)
        try:
            rect = printer.pageRect()
            scaled_pixmap = pixmap.scaled(rect.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            painter.drawPixmap(rect, scaled_pixmap)
        finally:
            painter.end()
            self.close()


from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QFileDialog, QMessageBox
)
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt, QSize

class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap()
        self.current_angle = 0

        # Основной layout - горизонтальный
        self.main_layout = QHBoxLayout(self)

        # Левая панель с кнопками
        self.button_panel = QVBoxLayout()
        self.load_button = QPushButton("Загрузить изображение")
        self.load_button.clicked.connect(self.open_file)
        self.print_button = QPushButton("Печать изображения")
        self.print_button.clicked.connect(self.open_printer_window)
        self.rotate_left_button = QPushButton("Повернуть влево")
        self.rotate_left_button.clicked.connect(self.rotate_left)
        self.rotate_right_button = QPushButton("Повернуть вправо")
        self.rotate_right_button.clicked.connect(self.rotate_right)

        # Добавляем кнопки в левую панель
        self.button_panel.addWidget(self.load_button)
        self.button_panel.addWidget(self.print_button)
        self.button_panel.addWidget(self.rotate_left_button)
        self.button_panel.addWidget(self.rotate_right_button)

        # Spacer для заполнения пространства внизу
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button_panel.addSpacerItem(spacer)

        # Добавляем панели в основной layout
        self.main_layout.addLayout(self.button_panel)  # Левая панель с кнопками
        self.main_layout.addWidget(self.image_label, stretch=1)  # Область для изображения с растяжением

        self.setLayout(self.main_layout)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "../utils/drawings/",
                                                   "Изображения (*.png *.jpg *.bmp *.gif)")
        if file_path:
            self.pixmap = QPixmap(file_path)
            self.current_angle = 0
            self.update_image()  # После загрузки обновляем изображение
            self.current_image_path = file_path

    def rotate_right(self):
        if not self.pixmap.isNull():
            self.current_angle = (self.current_angle + 90) % 360
            self.update_image()

    def rotate_left(self):
        if not self.pixmap.isNull():
            self.current_angle = (self.current_angle - 90) % 360
            self.update_image()

    def update_image(self):
        """Обновляем изображение с фиксированным размером"""
        if not self.pixmap.isNull():
            transform = QTransform().rotate(self.current_angle)
            rotated_pixmap = self.pixmap.transformed(transform, Qt.SmoothTransformation)

            # Фиксируем размер изображения (например, 500x500)
            fixed_size = QSize(500, 500)
            scaled_pixmap = rotated_pixmap.scaled(fixed_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            self.image_label.setPixmap(scaled_pixmap)

    def open_printer_window(self):
        if not hasattr(self, 'current_image_path') or not self.current_image_path:
            QMessageBox.warning(self, "Предупреждение", "Нет изображения для печати.")
            return

        # Открытие окна для печати
        self.printer_window = PrintDialog(self.current_image_path)
        self.printer_window.show()

class CustomTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def close_current_tab(self):
        index = self.currentIndex()
        # Проверяем, существует ли защищённый список вкладок, и удаляем, только если вкладка не защищена
        if index != -1 and (not hasattr(self, 'protected_tabs') or index not in self.protected_tabs):
            self.removeTab(index)
        else:
            QMessageBox.warning(self, "Предупреждение", "Нельзя удалить защищённую вкладку.")
            return


class RenameTabDialog(QDialog):
    def __init__(self, current_name, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Изменение названия вкладки")
        self.current_name = current_name
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout(self)

        self.label = QLabel(f"Текущее название: {self.current_name}", self)
        self.layout.addWidget(self.label)

        self.new_name_input = QLineEdit(self)
        self.new_name_input.setText(self.current_name)
        self.layout.addWidget(self.new_name_input)

        self.button_ok = QPushButton("Изменить", self)
        self.button_ok.clicked.connect(self.accept)
        self.layout.addWidget(self.button_ok)

    def get_new_name(self):
        return self.new_name_input.text()

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QFrame


class StructureTabContent(QWidget):
    def __init__(self):
        super().__init__()

        # Основной layout вкладки
        layout = QVBoxLayout(self)

        # Создаём область прокрутки
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Создаём содержимое для скролла
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        # Добавляем примерные элементы в содержимое
        for i in range(50):  # Больше элементов для прокрутки
            label = QLabel(f"Элемент структуры {i + 1}")
            scroll_layout.addWidget(label)

        scroll_content.setLayout(scroll_layout)

        # Добавляем содержимое в область прокрутки
        scroll_area.setWidget(scroll_content)

        layout.addWidget(scroll_area)
        self.setLayout(layout)


from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea, QFrame, QLineEdit, QPushButton, QHBoxLayout
)
from PyQt5.QtCore import Qt


class TagsTabContent(QWidget):
    def __init__(self):
        super().__init__()

        # Основной layout вкладки
        main_layout = QVBoxLayout(self)

        # Создаём область прокрутки
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Содержимое для скролла
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignTop)  # Прижимаем содержимое к верху

        scroll_area.setWidget(self.scroll_content)

        # Кнопка для добавления нового поля для тега
        add_tag_button = QPushButton("Добавить новый тег")
        add_tag_button.clicked.connect(self.add_tag_input)

        # Добавляем область прокрутки и кнопку в основной layout
        main_layout.addWidget(scroll_area)
        main_layout.addWidget(add_tag_button)

        self.setLayout(main_layout)

    def add_tag_input(self):
        """Добавляет новое поле ввода для тега с кнопкой удаления."""
        # Создаём горизонтальный layout для поля ввода и кнопки
        tag_layout = QHBoxLayout()

        # Поле ввода тега
        tag_input = QLineEdit()
        tag_input.setPlaceholderText("Введите содержание тега")
        tag_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Кнопка удаления
        delete_button = QPushButton("Удалить")
        delete_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        delete_button.clicked.connect(lambda: self.remove_tag_input(tag_layout))

        # Добавляем поле ввода и кнопку в горизонтальный layout
        tag_layout.addWidget(tag_input)
        tag_layout.addWidget(delete_button)

        # Добавляем горизонтальный layout в основной вертикальный layout
        self.scroll_layout.addLayout(tag_layout)

    def remove_tag_input(self, tag_layout):
        """Удаляет указанный layout с полем ввода и кнопкой."""
        # Удаляем все виджеты из переданного layout
        while tag_layout.count():
            child = tag_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Удаляем сам layout из scroll_layout
        self.scroll_layout.removeItem(tag_layout)



from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QMessageBox, QDialog, QTabBar, QScrollArea, QVBoxLayout, QFrame
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QMessageBox, QDialog, QTabBar, QScrollArea, QVBoxLayout, QFrame
from PyQt5.QtCore import Qt

class MainTabWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.main_tab_widget = CustomTabWidget()
        layout.addWidget(self.main_tab_widget)

        # Словарь для хранения QScrollArea вкладок
        self.scroll_areas = {}

        # Добавляем защищённые вкладки
        self.add_protected_tabs()

    def add_protected_tabs(self):
        self.main_tab_widget.protected_tabs = set()

        # Вкладка "Структура"
        structure_tab = StructureTabContent()
        self.main_tab_widget.addTab(structure_tab, "")
        self.add_scroll_area_to_tab(structure_tab, "Структура")

        # Вкладка "Теги"
        tags_tab = TagsTabContent()
        self.main_tab_widget.addTab(tags_tab, "")
        self.add_scroll_area_to_tab(tags_tab, "Теги")

        # Кастомные заголовки вкладок
        self.main_tab_widget.tabBar().setTabButton(0, QTabBar.LeftSide,
                                                   self.create_custom_label("Структура", "blue", 12))
        self.main_tab_widget.tabBar().setTabButton(1, QTabBar.LeftSide,
                                                   self.create_custom_label("Теги", "blue", 12))

        # Добавляем индексы защищённых вкладок
        self.main_tab_widget.protected_tabs.add(0)  # Структура
        self.main_tab_widget.protected_tabs.add(1)  # Теги

    def create_custom_label(self, text, color, font_size):
        label = QLabel(text)
        label.setStyleSheet(f"color: {color}; font-size: {font_size}px; font-weight: bold;")
        return label

    def add_scroll_area_to_tab(self, tab, tab_name):
        """Добавляет QScrollArea во вкладку и сохраняет её для обновления."""
        scroll_area = QScrollArea()
        scroll_content = QFrame()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_content.setLayout(scroll_layout)

        scroll_area.setWidget(scroll_content)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedHeight(200)

        layout = QVBoxLayout(tab)
        layout.addWidget(QLabel(f"Вкладка: {tab_name}"))
        layout.addWidget(scroll_area)

        # Сохраняем ссылку на QScrollArea
        self.scroll_areas[tab] = scroll_layout

    def add_detail_tab(self):
        tab = InnerTabWidget()
        self.main_tab_widget.addTab(tab, "Деталь")
        new_index = self.main_tab_widget.count() - 1
        self.main_tab_widget.setCurrentIndex(new_index)

    def add_assembly_unit_tab(self):
        tab = InnerTabWidget()
        self.main_tab_widget.addTab(tab, "Сборочная единица")
        new_index = self.main_tab_widget.count() - 1
        self.main_tab_widget.setCurrentIndex(new_index)

        print("Добавляем вкладку 'Сборочная единица' и обновляем список.")
        self.update_scroll_areas("Сборочная единица")

    def update_scroll_areas(self, tab_name):
        """Добавляет название новой вкладки в QScrollArea всех вкладок с деталями."""
        if not self.scroll_areas:
            print("Нет доступных QScrollArea для обновления.")
            return

        for tab, scroll_layout in self.scroll_areas.items():
            label = QLabel(tab_name)
            scroll_layout.addWidget(label)
            print(f"Добавлено '{tab_name}' в вкладку {tab}")

    def rename_tab(self):
        current_index = self.main_tab_widget.currentIndex()
        if current_index == -1:
            QMessageBox.warning(self, "Предупреждение", "Выберите вкладку для изменения названия.")
            return

        # Проверяем, является ли вкладка защищённой
        if current_index in self.main_tab_widget.protected_tabs:
            QMessageBox.warning(self, "Предупреждение", "Нельзя изменить название защищённой вкладки.")
            return

        current_name = self.main_tab_widget.tabText(current_index)
        dialog = RenameTabDialog(current_name, self)

        if dialog.exec_() == QDialog.Accepted:
            new_name = dialog.get_new_name()
            if new_name:
                self.main_tab_widget.setTabText(current_index, new_name)
            else:
                QMessageBox.warning(self, "Предупреждение", "Название не может быть пустым.")

class InnerTabWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QGridLayout(self)
        self.inner_tab_widget = CustomTabWidget()

        self.checkbox = QCheckBox("Принадлежность к СБ")

        # Создаём область прокрутки
        self.scroll_content = QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout(self.scroll_content)

        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_content)
        self.scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.scroll_area.setFixedWidth(200)

        # Кнопки управления вкладками
        self.rename_inner_tab_button = QPushButton("Название листа")
        self.rename_inner_tab_button.clicked.connect(self.rename_inner_tab)

        self.add_inner_tab_button = QPushButton("Добавить лист")
        self.add_inner_tab_button.clicked.connect(self.add_inner_tab)

        self.close_inner_tab_button = QPushButton("Закрыть текущий лист")
        self.close_inner_tab_button.clicked.connect(self.inner_tab_widget.close_current_tab)

        # Добавляем виджет с прокруткой и кнопки в компоновку
        layout.addWidget(self.inner_tab_widget, 0, 0, 5, 1)  # Вкладки
        layout.addWidget(self.checkbox, 0, 1, 1, 1)  # Область прокрутки
        layout.addWidget(self.scroll_area, 1, 1, 1, 1)  # Область прокрутки
        layout.addWidget(self.rename_inner_tab_button, 2, 1, 1, 1)  # Кнопка "Название листа"
        layout.addWidget(self.add_inner_tab_button, 3, 1, 1, 1)  # Кнопка "Добавить лист"
        layout.addWidget(self.close_inner_tab_button, 4, 1, 1, 1)  # Кнопка "Закрыть текущий лист"

        self.add_inner_tab()

    def add_inner_tab(self):
        tab = QWidget()
        tab_layout = QtWidgets.QGridLayout(tab)
        drawing_widget = DrawingWidget()

        # Добавляем DrawingWidget в таб
        tab_layout.addWidget(drawing_widget, 0, 0, 1, 2)

        # Определяем имя новой вкладки
        tab_name = f"Лист {self.inner_tab_widget.count() + 1}"
        self.inner_tab_widget.addTab(tab, tab_name)

        # Добавляем элемент в scroll_area
        label = QLabel(tab_name)
        label.setObjectName(f"tab_label_{self.inner_tab_widget.count() - 1}")
        self.scroll_layout.addWidget(label)

        # Делаем новую вкладку текущей
        new_index = self.inner_tab_widget.count() - 1
        self.inner_tab_widget.setCurrentIndex(new_index)

    def rename_inner_tab(self):
        current_index = self.inner_tab_widget.currentIndex()
        if current_index == -1:
            QMessageBox.warning(self, "Предупреждение", "Выберите вкладку для изменения названия.")
            return

        current_name = self.inner_tab_widget.tabText(current_index)
        dialog = RenameTabDialog(current_name, self)

        if dialog.exec_() == QDialog.Accepted:
            new_name = dialog.get_new_name()
            if new_name:
                self.inner_tab_widget.setTabText(current_index, new_name)

                # Обновляем текст в scroll_area
                item = self.scroll_layout.itemAt(current_index)
                if item and item.widget():
                    item.widget().setText(new_name)
            else:
                QMessageBox.warning(self, "Предупреждение", "Название не может быть пустым.")

    def close_current_tab(self):
        current_index = self.inner_tab_widget.currentIndex()
        if current_index == -1:
            return

        self.inner_tab_widget.removeTab(current_index)

        # Удаляем элемент из scroll_area
        item = self.scroll_layout.takeAt(current_index)  # Забираем элемент из layout
        if item:
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # Обновляем область прокрутки
        self.scroll_content.update()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = MainTabWidget()
    main_window.show()
    sys.exit(app.exec_())
