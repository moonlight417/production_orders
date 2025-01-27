import sys
import os
from functools import partial

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QPushButton,
    QLabel, QScrollArea, QFrame, QMessageBox, QInputDialog, QRadioButton, QCheckBox, QGridLayout
)
from PyQt5.QtCore import Qt

from django.db import IntegrityError
from django.core.exceptions import ValidationError
from products.models import MainDocument, Tag, Drawing, DrawingSheet
from windows.design_filling.tags_tab_content import TagsTabContent
from windows.design_filling.inner_tab_widget import InnerTabWidget
from .gui.ui_design_document_filling_form import Ui_DesignDocumentFillingForm


class MainTabWidget(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui  # Сохраняем ссылку на интерфейс
        self.initialize_ui()

        self.linked_tab = None  # Вкладка, связанная с главным именем

        # Данные по умолчанию
        # self.comment = "Комментарий к основному документу"
        self.doc_name = "Чертеж 1"
        self.mass = 100.5
        self.sheet_number = 1
        self.file = "path_to_drawing_sheet_file_1.pdf"
        self.is_actual = True

    def initialize_ui(self):
        """Инициализация пользовательского интерфейса."""
        layout = QVBoxLayout(self)

        # Основной виджет с вкладками
        self.main_tab_widget = QTabWidget()
        self.scroll_areas = {}  # Хранение областей прокрутки
        self.tab_types = {}  # Типы вкладок
        self.check_boxes = {}  # Чекбоксы для вкладок
        self.radio_buttons = {}  # Радиокнопки в областях прокрутки

        self.main_name = ""
        self.linked_tab = None  # Вкладка, от которой зависит main_name

        self.label_main_name = QLabel(self.main_name)
        self.label_main_name.setStyleSheet("font-size: 16pt; font-family: Arial;")

        # Кнопки управления вкладками
        button_layout = QHBoxLayout()
        add_assembly_button = QPushButton("+ СБ")
        add_assembly_button.clicked.connect(self.add_assembly_unit_tab)

        add_detail_button = QPushButton("+ Деталь")
        add_detail_button.clicked.connect(self.add_detail_tab)

        rename_tab_button = QPushButton("Назвать элемент")
        rename_tab_button.clicked.connect(self.rename_current_tab)

        close_tab_button = QPushButton("Закрыть текущую вкладку")
        close_tab_button.clicked.connect(self.close_current_tab)

        save_button = QPushButton("Сохранить в БД")
        save_button.clicked.connect(self.save_to_db)

        button_layout.addWidget(self.label_main_name)
        button_layout.addWidget(add_assembly_button)
        button_layout.addWidget(add_detail_button)
        button_layout.addWidget(rename_tab_button)
        button_layout.addWidget(close_tab_button)
        button_layout.addWidget(save_button)

        layout.addLayout(button_layout)
        layout.addWidget(self.main_tab_widget)

        # Добавление защищённых вкладок
        self.add_protected_tabs()

    def add_protected_tabs(self):
        """Добавление защищённых вкладок."""
        self.tags_tab_content = TagsTabContent()
        self.main_tab_widget.addTab(self.tags_tab_content, "Теги")
        self.protected_tabs = {self.tags_tab_content}

    def add_assembly_unit_tab(self):
        """Добавляет новую вкладку с названием 'Сборочная единица'."""
        self._add_tab("Сборочная единица", is_assembly_unit=True)
        self.linked_tab = self.main_tab_widget.currentWidget()
        self.main_name = "Сборочная единица"
        self.update_main_name()
        # Получаем текущую вкладку и выводим ее атрибут is_assembly_unit
        print(self.linked_tab.is_assembly_unit)  # Выведем атрибут для текущей вкладки

    def add_detail_tab(self):
        """Добавляет новую вкладку с названием 'Деталь'."""
        self._add_tab("Деталь", is_assembly_unit=False)
        self.linked_tab = self.main_tab_widget.currentWidget()
        self.main_name = "Деталь"
        self.update_main_name()
        # Получаем текущую вкладку и выводим ее атрибут is_assembly_unit
        print(self.linked_tab.is_assembly_unit)  # Выведем атрибут для текущей вкладки

    def _add_tab(self, tab_name, is_assembly_unit):
        """Создаёт вкладку с указанным названием."""
        tab = QWidget()

        # Внутренний виджет с табами
        tab_inner = InnerTabWidget()

        # Создание области прокрутки
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedWidth(200)
        scroll_frame = QFrame()
        scroll_layout = QVBoxLayout(scroll_frame)
        scroll_layout.setAlignment(Qt.AlignTop)
        scroll_area.setWidget(scroll_frame)

        # Чекбокс и кнопка
        check_box = QCheckBox("Добавить в СБ", self)
        check_box.stateChanged.connect(partial(self.on_check_box_state_changed, tab))
        # button_refresh = QPushButton("Обновить")
        # button_refresh.setFixedWidth(100)
        # button_refresh.clicked.connect(partial(self.check_and_disable, tab))

        # Создание Grid Layout
        tab_layout = QGridLayout(tab)

        # Добавление элементов в сетку
        tab_layout.addWidget(check_box, 0, 0)  # Чекбокс в (0, 0)
        # tab_layout.addWidget(button_refresh, 0, 1)  # Кнопка в (0, 1)
        tab_layout.addWidget(scroll_area, 1, 0, 1, 1)  # Область прокрутки в (1, 0)
        tab_layout.addWidget(tab_inner, 0, 1, 2, 1)  # InnerTabWidget в (1, 1)

        # Растяжимость колонок
        tab_layout.setColumnStretch(0, 0)  # Левая колонка растягивается
        tab_layout.setColumnStretch(1, 2)  # Правая колонка растягивается сильнее

        # Добавление новой вкладки в главный виджет
        self.main_tab_widget.addTab(tab, tab_name)
        new_index = self.main_tab_widget.count() - 1
        self.main_tab_widget.setCurrentIndex(new_index)

        # Сохранение ссылок на элементы
        self.scroll_areas[tab] = scroll_layout
        self.tab_types[tab] = tab_name
        self.check_boxes[tab] = check_box
        self.radio_buttons[tab] = []

        tab.is_assembly_unit = is_assembly_unit

        # Обновляем области прокрутки
        self.update_scroll_areas()
        self.update_main_name()



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

            # Проверка на связанной вкладке
            if self.main_tab_widget.widget(current_index) == self.linked_tab:
                self.main_name = new_name
                self.update_main_name()

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

        # Проверяем, является ли удаляемая вкладка связанной
        if tab == self.linked_tab:
            self.main_name = ""  # Сбрасываем основное имя
            self.update_main_name()
            self.linked_tab = None  # Сбрасываем ссылку на связанную вкладку

        self.main_tab_widget.removeTab(current_index)
        self.update_main_name()

        # Удаляем данные о вкладке из словарей
        if tab in self.scroll_areas:
            del self.scroll_areas[tab]
        if tab in self.tab_types:
            del self.tab_types[tab]
        if tab in self.check_boxes:
            del self.check_boxes[tab]
        if tab in self.radio_buttons:
            del self.radio_buttons[tab]

        # Обновляем области прокрутки
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

        # Обновляем содержимое self.label_main_name
        self.update_main_name()

    def update_main_name(self):
        """Обновляет содержимое self.label_main_name в зависимости от состояния чекбоксов."""
        print("Вызов update_main_name")  # Отладочный вывод

        main_assembly_unit = None

        # Проверяем вкладки, где чекбокс "Добавить в СБ" НЕ включен
        for tab, check_box in self.check_boxes.items():
            if not check_box.isChecked():
                main_assembly_unit = tab
                break

        if main_assembly_unit:
            # Имя главной сборочной единицы (вкладки с неотмеченным чекбоксом)
            self.main_name = self.main_tab_widget.tabText(self.main_tab_widget.indexOf(main_assembly_unit))
        else:
            # Если все чекбоксы включены, ищем первую вкладку "Деталь"
            for tab, tab_name in self.tab_types.items():
                if tab_name == "Деталь":
                    self.main_name = self.main_tab_widget.tabText(self.main_tab_widget.indexOf(tab))
                    break
            else:
                # Если вкладок нет или они все связаны, берем последнюю добавленную
                if self.main_tab_widget.count() > 0:
                    self.main_name = self.main_tab_widget.tabText(self.main_tab_widget.count() - 1)
                else:
                    self.main_name = ""

        print(f"Новое имя: {self.main_name}")  # Отладочный вывод
        # Обновляем текст в лейбле
        self.label_main_name.setText(self.main_name)

    def on_check_box_state_changed(self, tab, state):
        """Обрабатывает изменения состояния чекбокса и обновляет главную сборочную единицу."""
        is_checked = state == Qt.Checked
        for radio_button in self.radio_buttons[tab]:
            radio_button.setEnabled(is_checked)

        # Обновляем содержимое главной сборочной единицы
        self.update_main_name()

    def save_to_db(self):
        # Проверяем, существует ли связанная вкладка
        # if self.linked_tab is None:
        #     QMessageBox.warning(self, "Ошибка", "Связанная вкладка не выбрана. Проверьте корректность данных.")
        #     return
        #
        is_assembly_unit = self.linked_tab.is_assembly_unit
        main_name = self.label_main_name.text()
        comment = self.ui.textEditComments.toPlainText()


        # Получаем текстовые значения тегов из tag_list
        try:
            tag_names = self.tags_tab_content.get_tag_list()
            print("Теги:", tag_names)
        except Exception as e:
            print(f"Ошибка при создании списка тегов: {e}")

        try:
            # Создание основного документа
            main_doc = MainDocument.objects.create(
                main_name = main_name,
                comment = comment,
            )

            # Добавление тегов
            if not tag_names:
                print("Список тегов пустой. Пропускаем добавление тегов.")

            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                main_doc.tags.add(tag)

            # Создание чертежа, связанного с основным документом
            drawing = Drawing.objects.create(
                main_document=main_doc,
                doc_name=self.doc_name,
                mass=self.mass,
                assembly_unit=is_assembly_unit,
            )

            # Создание листа чертежа, связанного с чертежом
            drawing_sheet = DrawingSheet.objects.create(
                drawing=drawing,
                file=self.file,
                sheet_number=self.sheet_number,
                is_actual=self.is_actual,
            )

            QMessageBox.information(None, "Успех", "Документ успешно сохранён в базе данных.")
            print(f"Задача '{self.main_name}' и чертеж '{self.doc_name}' успешно сохранены.")

        except IntegrityError as e:
            QMessageBox.critical(None, "Ошибка", f"Ошибка сохранения данных: {e}")
            print(f"Ошибка сохранения данных: {e}")
        except ValidationError as e:
            QMessageBox.critical(None, "Ошибка", f"Ошибка валидации данных: {e}")
            print(f"Ошибка валидации данных: {e}")
        except Exception as e:
            QMessageBox.critical(None, "Ошибка", f"Произошла ошибка при сохранении: {e}")
            print(f"Ошибка при сохранении: {e}")

    