import sys
import os
from django.db import transaction
from functools import partial

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QPushButton,
    QLabel, QScrollArea, QFrame, QMessageBox, QInputDialog, QRadioButton, QCheckBox, QGridLayout, QLineEdit
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

        self.current_image_path = None  # ✅ Добавляем переменную для хранения пути к файлу
        # self.check_box_is_actual = QCheckBox("Актуальность документа", self)  # ✅ Чекбокс актуальности

        self.linked_tab = None  # Вкладка, связанная с главным именем
        self.selected_radio_button = None

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

        rename_tab_button = QPushButton("Переименовать вкладку")
        rename_tab_button.clicked.connect(self.rename_current_tab)

        close_tab_button = QPushButton("Удалить текущую вкладку")
        close_tab_button.clicked.connect(self.close_current_tab)

        save_button = QPushButton("Сохранить в БД")
        save_button.clicked.connect(self.on_save_button_clicked)
        # save_button.clicked.connect(self.save_tabs_data_to_db)
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

    def on_save_button_clicked(self):
        tabs_data = self.get_tabs_data()
        print(tabs_data)  # Для тестирования, заменить на сохранение в файл или обработку

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

        self.current_name = self.main_tab_widget.tabText(current_index)
        new_name, ok = QInputDialog.getText(self, "Переименовать вкладку", "Введите новое название:", text=self.current_name)

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
        """Закрывает текущую вкладку с подтверждением, если она не защищённая."""
        current_index = self.main_tab_widget.currentIndex()
        if current_index == -1:
            return

        tab = self.main_tab_widget.widget(current_index)

        # Проверка на защищённую вкладку
        if tab in self.protected_tabs:
            QMessageBox.warning(self, "Предупреждение", "Нельзя удалить защищённую вкладку.")
            return

        # Показываем подтверждение удаления
        reply = QMessageBox.question(
            self, "Подтверждение удаления",
            "Вы уверены, что хотите удалить текущую вкладку?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.No:
            return

        # Если вкладка связана, сбрасываем её данные
        if tab == self.linked_tab:
            self.main_name = ""  # Сбрасываем основное имя
            self.update_main_name()
            self.linked_tab = None  # Сбрасываем ссылку на связанную вкладку

        # Удаляем вкладку
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
                radio_button.toggled.connect(
                    partial(self.on_radio_button_toggled, radio_button, tab))  # Подключаем обработчик
                scroll_layout.addWidget(radio_button)
                self.radio_buttons[tab].append(radio_button)

    def on_radio_button_toggled(self, radio_button, tab):
        """Обрабатывает изменение состояния радиокнопки."""
        if radio_button.isChecked():
            # Сохраняем имя выбранной радиокнопки
            self.selected_radio_button = radio_button.text()
            print(f"Выбрана радиокнопка: {self.selected_radio_button}")

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

    def get_tabs_data(self):
        """Собирает данные вкладок и находит главную сборку"""
        from django.db import transaction
        tabs_data = []
        parent_id = None
        main_parent_name = None  # Здесь будет имя главного документа

        try:
            with transaction.atomic():
                first_tab_name = None  # Запоминаем первую вкладку

                for i in range(self.main_tab_widget.count()):
                    tab = self.main_tab_widget.widget(i)

                    if self.main_tab_widget.tabText(i) == "Теги":
                        continue  # Пропускаем вкладку "Теги"

                    tab_name = self.main_tab_widget.tabText(i)
                    mass_input = self._find_mass_input(tab)
                    mass = float(mass_input.text()) if mass_input and mass_input.text() else None

                    # ✅ Определяем, является ли вкладка дочерней (если у нее есть родитель)
                    is_child = tab in self.radio_buttons and tab in self.check_boxes and self.check_boxes[
                        tab].isChecked()
                    parent = self.main_tab_widget.tabText(i - 1) if is_child else None

                    # ✅ Определяем главную сборку (первая вкладка без родителя)
                    if main_parent_name is None and not is_child:
                        main_parent_name = tab_name  # Берем первую сборочную единицу

                    # Сохраняем данные вкладки
                    tab_data = {
                        'doc_name': tab_name,
                        'mass': mass,
                        'parent': parent  # ✅ Сохраняем только родительскую связь
                    }
                    tabs_data.append(tab_data)

                # Если главная сборка не найдена, используем имя первой вкладки (даже если это деталь)
                if main_parent_name is None:
                    main_parent_name = first_tab_name

                print(f"Собранные данные вкладок: {tabs_data}")
                print(f"Главный документ: {main_parent_name}")

        except Exception as e:
            print(f"Ошибка при обработке данных вкладок: {e}")

        return tabs_data, main_parent_name

    # код корректно сохраняет в базу данных значения assembly_unit и ссылка на parent_id
    # def get_tabs_data(self):
    #     from django.db import transaction
    #     tabs_data = []
    #
    #     try:
    #         with transaction.atomic():  # Используем транзакцию для безопасности операций с базой данных
    #             parent_drawing = None  # Здесь будет храниться объект родителя
    #             parent_id = None  # Здесь будет храниться id родителя
    #
    #             # Шаг 1: Сохранение родительского документа
    #             if self.selected_radio_button:  # Проверяем, выбрана ли радиокнопка
    #                 parent_name = self.selected_radio_button  # Имя родительского документа
    #
    #                 # Попробуем найти первый объект с таким именем
    #                 parent_drawing = Drawing.objects.filter(doc_name=parent_name).first()
    #
    #                 if not parent_drawing:
    #                     # Если объекта нет, создаем его
    #                     parent_drawing = Drawing.objects.create(
    #                         doc_name=parent_name,
    #                         mass=None,
    #                         assembly_unit=True  # Используем assembly_unit вместо is_assembly_unit
    #                     )
    #
    #                 parent_id = parent_drawing.id  # Получаем ID родителя
    #                 print(f"Родительский документ '{parent_name}' сохранен с ID: {parent_id}")
    #
    #             # Шаг 2: Проходим по всем вкладкам верхнего уровня
    #             for i in range(self.main_tab_widget.count()):
    #                 # Получаем виджет текущей вкладки
    #                 tab = self.main_tab_widget.widget(i)
    #
    #                 # Пропускаем вкладку "Теги"
    #                 if self.main_tab_widget.tabText(i) == "Теги":
    #                     continue
    #
    #                 # Ищем поле ввода массы в дочерних вкладках
    #                 mass_input = self._find_mass_input(tab)
    #
    #                 # Шаг 3: Запись данных вкладки
    #                 tab_data = {
    #                     'doc_name': self.main_tab_widget.tabText(i),  # Имя вкладки
    #                     'mass': mass_input.text() if mass_input else None,  # Масса
    #                     'assembly_unit': tab.assembly_unit if hasattr(tab, 'assembly_unit') else False,
    #                     # ID родителя
    #                     'parent': parent_id if tab in self.radio_buttons and tab in self.check_boxes and
    #                                            self.check_boxes[tab].isChecked() else None
    #                 }
    #
    #                 # Добавляем данные вкладки в общий список
    #                 tabs_data.append(tab_data)
    #
    #             print("Собранные данные вкладок:", tabs_data)
    #
    #     except Exception as e:
    #         print(f"Ошибка при обработке данных вкладок: {e}")
    #
    #     return tabs_data

    # Сохраняет всё, кроме значения assembly_unit и ссылка на parent_id
    # def get_tabs_data(self):
    #     """Собирает данные вкладок и находит главную сборку"""
    #     from django.db import transaction
    #     tabs_data = []
    #     parent_id = None
    #     main_parent_name = None  # Здесь будет имя главного документа
    #
    #     try:
    #         with transaction.atomic():
    #             first_tab_name = None  # Запоминаем первую вкладку
    #
    #             for i in range(self.main_tab_widget.count()):
    #                 tab = self.main_tab_widget.widget(i)
    #
    #                 if self.main_tab_widget.tabText(i) == "Теги":
    #                     continue  # Пропускаем вкладку "Теги"
    #
    #                 tab_name = self.main_tab_widget.tabText(i)
    #                 mass_input = self._find_mass_input(tab)
    #                 mass = float(mass_input.text()) if mass_input and mass_input.text() else None
    #                 is_assembly_unit = hasattr(tab, 'assembly_unit') and tab.assembly_unit
    #                 is_child = tab in self.radio_buttons and tab in self.check_boxes and self.check_boxes[
    #                     tab].isChecked()
    #                 parent = parent_id if is_child else None
    #
    #                 # Запоминаем имя первой вкладки (любого типа)
    #                 if first_tab_name is None:
    #                     first_tab_name = tab_name
    #
    #                 # Определяем главную сборку (первая сборочная вкладка без родителя)
    #                 if is_assembly_unit and not is_child:
    #                     if main_parent_name is None:  # Берем первую подходящую
    #                         main_parent_name = tab_name
    #
    #                 # Сохраняем данные вкладки
    #                 tab_data = {
    #                     'doc_name': tab_name,
    #                     'mass': mass,
    #                     'assembly_unit': is_assembly_unit,
    #                     'parent': parent
    #                 }
    #                 tabs_data.append(tab_data)
    #
    #             # Если главная сборка не найдена, используем имя первой вкладки (даже если это деталь)
    #             if main_parent_name is None:
    #                 main_parent_name = first_tab_name
    #
    #             print(f"Собранные данные вкладок: {tabs_data}")
    #             print(f"Главный документ: {main_parent_name}")
    #
    #     except Exception as e:
    #         print(f"Ошибка при обработке данных вкладок: {e}")
    #
    #     return tabs_data, main_parent_name

    # def get_main_document(self):
    #     """Получение основного документа для привязки чертежей."""
    #     # Здесь можно использовать существующий документ или создать новый
    #     main_doc, created = MainDocument.objects.get_or_create(
    #         main_name=self.label_main_name.text(),
    #         defaults={'comment': self.ui.textEditComments.toPlainText()}
    #     )
    #     return main_doc

    def _find_mass_input(self, parent_widget):
        """
        Рекурсивно ищет self.lineEditMass в дочерних виджетах.
        :param parent_widget: Родительский виджет, в котором искать.
        :return: Найденный QLineEdit или None.
        """
        # Если текущий виджет имеет атрибут lineEditMass, возвращаем его
        if hasattr(parent_widget, 'lineEditMass'):
            return parent_widget.lineEditMass

        # Если у виджета есть дочерние элементы, ищем среди них
        for child in parent_widget.children():
            result = self._find_mass_input(child)
            if result:
                return result

        return None

    def save_to_db(self):
        """Сохраняет данные вкладок в базу данных и файлы чертежей"""
        if self.linked_tab is None:
            QMessageBox.warning(self, "Ошибка", "Связанная вкладка не выбрана. Проверьте корректность данных.")
            return

        tag_names = self.tags_tab_content.get_tag_list()
        if not tag_names:
            QMessageBox.warning(self, "Ошибка", "Необходимо добавить хотя бы один тег.")
            return

        # Получаем данные вкладок и имя главной сборки
        tabs_data, main_parent_name = self.get_tabs_data()

        if not main_parent_name:
            QMessageBox.warning(self, "Ошибка", "Главная сборка не найдена.")
            return

        try:
            with transaction.atomic():
                # **ШАГ 1: Создаем `MainDocument`**
                main_doc, created = MainDocument.objects.get_or_create(
                    main_name=main_parent_name,
                    defaults={'comment': self.ui.textEditComments.toPlainText()}
                )

                # **ШАГ 2: Добавляем теги**
                for tag_name in tag_names:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    main_doc.tags.add(tag)

                # **ШАГ 3: Разделяем родительские и дочерние элементы**
                parent_tabs = [tab for tab in tabs_data if tab['parent'] is None]
                child_tabs = [tab for tab in tabs_data if tab['parent'] is not None]

                parent_drawings = {}

                # **ШАГ 4: Сохраняем родительские элементы**
                for parent_tab in parent_tabs:
                    drawing, created = Drawing.objects.get_or_create(
                        doc_name=parent_tab['doc_name'],
                        defaults={
                            'main_document': main_doc,
                            'mass': parent_tab['mass'],
                            'parent': None
                        }
                    )

                    parent_drawings[drawing.doc_name] = drawing  # Используем `doc_name` как ключ

                    # **Сохранение чертежных листов**
                    self.save_drawing_sheets(drawing)

                # **ШАГ 5: Сохраняем дочерние элементы**
                for child_tab in child_tabs:
                    parent_name = child_tab['parent']
                    parent_drawing = parent_drawings.get(parent_name)

                    if not parent_drawing:
                        raise ValueError(f"❌ Ошибка: Не найден родительский документ для {child_tab['doc_name']}")

                    drawing, created = Drawing.objects.get_or_create(
                        doc_name=child_tab['doc_name'],
                        defaults={
                            'main_document': main_doc,
                            'mass': child_tab['mass'],
                            'parent': parent_drawing
                        }
                    )

                    # **Сохранение чертежных листов**
                    self.save_drawing_sheets(drawing)

                QMessageBox.information(None, "Успех",
                                        "Документ, файлы чертежей и данные вкладок успешно сохранены в базе данных.")
                print(f"✅ Основной документ '{main_parent_name}' и связанные данные вкладок успешно сохранены.")

        except IntegrityError as e:
            QMessageBox.critical(None, "Ошибка", f"Ошибка сохранения данных: {e}")
            print(f"Ошибка сохранения данных: {e}")
        except ValidationError as e:
            QMessageBox.critical(None, "Ошибка", f"Ошибка валидации данных: {e}")
            print(f"Ошибка валидации данных: {e}")
        except Exception as e:
            QMessageBox.critical(None, "Ошибка", f"Произошла ошибка при сохранении: {e}")
            print(f"Ошибка при сохранении: {e}")

    def save_drawing_sheets(self, drawing):
        """Сохраняет файлы чертежей и их актуальность для данного чертежа."""

        # ✅ Проверяем, есть ли self.current_image_path
        if not hasattr(self, 'current_image_path') or not self.current_image_path:
            print(f"⚠️ Ошибка: `current_image_path` отсутствует! Чертеж '{drawing.doc_name}' будет без файла.")
            file_path = None  # ❌ Нет файла
        else:
            file_path = self.current_image_path  # ✅ Берем путь из `open_file()`

        # ✅ Проверяем чекбокс актуальности
        is_actual = False  # По умолчанию
        if hasattr(self, 'linked_tab') and hasattr(self.linked_tab, 'drawing_widget'):
            if hasattr(self.linked_tab.drawing_widget, 'check_box_is_actual'):
                is_actual = self.linked_tab.drawing_widget.check_box_is_actual.isChecked()
            else:
                print("⚠️ `drawing_widget` не содержит чекбокс актуальности!")
        else:
            print("⚠️ `linked_tab` не содержит `drawing_widget`!")

        # ✅ Сохраняем путь относительно `archived_images`
        archive_folder = os.path.join(os.path.dirname(__file__), 'archived_images')
        relative_path = os.path.relpath(file_path, archive_folder) if file_path else None

        print(
            f"📄 Сохраняем чертеж: {relative_path if relative_path else '❌ ФАЙЛ ОТСУТСТВУЕТ'} (Актуальность: {is_actual})")

        try:
            # ✅ Создаем запись в `DrawingSheet`
            DrawingSheet.objects.create(
                drawing=drawing,
                file=os.path.join("archived_images", relative_path) if file_path else "",  # ✅ Сохраняем путь к файлу
                is_actual=is_actual,  # ✅ Сохраняем актуальность
            )

            print(
                f"✅ Чертеж сохранен: archived_images/{relative_path if relative_path else '❌ ФАЙЛ ОТСУТСТВУЕТ'} (Актуальность: {is_actual})")

        except Exception as e:
            print(f"❌ Ошибка при сохранении чертежа: {e}")

    # код корректно сохраняет в базу данных значения assembly_unit и ссылка на parent_id
    # def save_to_db(self):
    #     """Метод сохранения данных в базу данных с обработкой ошибок."""
    #     # Проверка наличия связанной вкладки
    #     if self.linked_tab is None:
    #         QMessageBox.warning(self, "Ошибка", "Связанная вкладка не выбрана. Проверьте корректность данных.")
    #         return
    #
    #     # Проверка наличия тегов
    #     tag_names = self.tags_tab_content.get_tag_list()
    #     if not tag_names:
    #         QMessageBox.warning(self, "Ошибка", "Необходимо добавить хотя бы один тег.")
    #         return
    #
    #     # Получение данных из интерфейса
    #     is_assembly_unit = self.linked_tab.is_assembly_unit
    #     main_name = self.label_main_name.text()
    #     comment = self.ui.textEditComments.toPlainText()
    #
    #     # Получение данных вкладок
    #     tabs_data = self.get_tabs_data()
    #
    #     try:
    #         # Создаем транзакцию, чтобы все изменения были выполнены атомарно
    #         with transaction.atomic():
    #             # Создание основного документа
    #             main_doc = MainDocument.objects.create(
    #                 main_name=main_name,
    #                 comment=comment,
    #             )
    #
    #             # Добавление тегов
    #             for tag_name in tag_names:
    #                 tag, created = Tag.objects.get_or_create(name=tag_name)
    #                 main_doc.tags.add(tag)
    #
    #             # Сохранение данных из tabs_data
    #             for tab_data in tabs_data:
    #                 # Проверяем, существует ли чертеж с таким именем
    #                 drawing = Drawing.objects.filter(doc_name=tab_data['doc_name']).first()
    #
    #                 if not drawing:
    #                     # Создаем родительский или дочерний чертеж
    #                     drawing = Drawing.objects.create(
    #                         main_document=main_doc,  # Связываем с основным документом
    #                         doc_name=tab_data['doc_name'],
    #                         mass=tab_data['mass'],  # Передаем массу
    #                         assembly_unit=tab_data['assembly_unit'],  # Сборочная единица
    #                         parent_id=tab_data['parent'],  # ID родительского чертежа
    #                     )
    #
    #                 # Создаем чертежный лист (если требуется)
    #                 if drawing and not drawing.parent:  # Только для родительских элементов
    #                     DrawingSheet.objects.create(
    #                         drawing=drawing,
    #                         file=self.file,  # Файл чертежа
    #                         sheet_number=self.sheet_number,  # Номер листа
    #                         is_actual=self.is_actual,  # Актуальность
    #                     )
    #
    #             QMessageBox.information(None, "Успех", "Документ и данные вкладок успешно сохранены в базе данных.")
    #             print(f"Основной документ '{main_name}' и связанные данные вкладок успешно сохранены.")
    #
    #     except IntegrityError as e:
    #         QMessageBox.critical(None, "Ошибка", f"Ошибка сохранения данных: {e}")
    #         print(f"Ошибка сохранения данных: {e}")
    #     except ValidationError as e:
    #         QMessageBox.critical(None, "Ошибка", f"Ошибка валидации данных: {e}")
    #         print(f"Ошибка валидации данных: {e}")
    #     except Exception as e:
    #         QMessageBox.critical(None, "Ошибка", f"Произошла ошибка при сохранении: {e}")
    #         print(f"Ошибка при сохранении: {e}")

    # Сохраняет всё, кроме значения assembly_unit и ссылка на parent_id
    # def save_to_db(self):
    #     """Сохраняет данные вкладок в базу данных"""
    #     if self.linked_tab is None:
    #         QMessageBox.warning(self, "Ошибка", "Связанная вкладка не выбрана. Проверьте корректность данных.")
    #         return
    #
    #     tag_names = self.tags_tab_content.get_tag_list()
    #     if not tag_names:
    #         QMessageBox.warning(self, "Ошибка", "Необходимо добавить хотя бы один тег.")
    #         return
    #
    #     # Получаем данные вкладок и имя главной сборки
    #     tabs_data, main_parent_name = self.get_tabs_data()
    #
    #     if not main_parent_name:
    #         QMessageBox.warning(self, "Ошибка", "Главная сборка не найдена.")
    #         return
    #
    #     try:
    #         with transaction.atomic():
    #             # **ШАГ 1: Создаем `MainDocument` один раз**
    #             main_doc, created = MainDocument.objects.get_or_create(
    #                 main_name=main_parent_name,
    #                 defaults={'comment': self.ui.textEditComments.toPlainText()}
    #             )
    #
    #             # **ШАГ 2: Добавляем теги**
    #             for tag_name in tag_names:
    #                 tag, created = Tag.objects.get_or_create(name=tag_name)
    #                 main_doc.tags.add(tag)
    #
    #             # **ШАГ 3: Разделяем родительские и дочерние элементы**
    #             parent_tabs = [tab for tab in tabs_data if tab['parent'] is None]
    #             child_tabs = [tab for tab in tabs_data if tab['parent'] is not None]
    #
    #             parent_drawings = {}
    #
    #             # **ШАГ 4: Сохраняем родительские элементы**
    #             for parent_tab in parent_tabs:
    #                 drawing, created = Drawing.objects.get_or_create(
    #                     doc_name=parent_tab['doc_name'],
    #                     defaults={
    #                         'main_document': main_doc,
    #                         'mass': parent_tab['mass'],
    #                         'assembly_unit': parent_tab['assembly_unit'],  # ✅ Теперь сборка сохраняется правильно
    #                         'parent': None
    #                     }
    #                 )
    #                 parent_drawings[drawing.doc_name] = drawing  # **Используем `doc_name` как ключ!**
    #
    #             # **ШАГ 5: Сохраняем дочерние элементы**
    #             for child_tab in child_tabs:
    #                 parent_name = child_tab['parent']  # Имя родителя (документ)
    #                 parent_drawing = parent_drawings.get(parent_name)  # Теперь ищем по имени
    #
    #                 if not parent_drawing:
    #                     raise ValueError(f"❌ Ошибка: Не найден родительский документ для {child_tab['doc_name']}")
    #
    #                 Drawing.objects.create(
    #                     main_document=main_doc,  # Привязываем к тому же `MainDocument`
    #                     doc_name=child_tab['doc_name'],
    #                     mass=child_tab['mass'],
    #                     assembly_unit=child_tab['assembly_unit'],  # ✅ Теперь у потомка остается его `assembly_unit`
    #                     parent=parent_drawing  # ✅ Теперь `parent` будет правильным!
    #                 )
    #
    #             QMessageBox.information(None, "Успех", "Документ и данные вкладок успешно сохранены в базе данных.")
    #             print(f"✅ Основной документ '{main_parent_name}' и связанные данные вкладок успешно сохранены.")
    #
    #     except IntegrityError as e:
    #         QMessageBox.critical(None, "Ошибка", f"Ошибка сохранения данных: {e}")
    #         print(f"Ошибка сохранения данных: {e}")
    #     except ValidationError as e:
    #         QMessageBox.critical(None, "Ошибка", f"Ошибка валидации данных: {e}")
    #         print(f"Ошибка валидации данных: {e}")
    #     except Exception as e:
    #         QMessageBox.critical(None, "Ошибка", f"Произошла ошибка при сохранении: {e}")
    #         print(f"Ошибка при сохранении: {e}")

    # def save_tabs_data_to_db(self):
    #     try:
    #         with transaction.atomic():
    #             # Шаг 1: Сохранить родительский документ
    #             parent_document = Drawing(
    #                 doc_name=self.main_name,  # Основное имя из интерфейса
    #                 mass=None,  # Если масса у родителя не задается, оставляем None
    #                 is_assembly_unit=True  # Указываем, что это сборочная единица
    #             )
    #             parent_document.save()
    #             parent_id = parent_document.id
    #             print(f"Родитель сохранен с ID: {parent_id}")
    #
    #             # Шаг 2: Обойти вкладки и сохранить данные дочерних документов
    #             for tab_data in self.get_tabs_data():
    #                 if tab_data['doc_name'] != "Теги":  # Пропускаем вкладку "Теги"
    #                     child_document = Drawing(
    #                         doc_name=tab_data['doc_name'],
    #                         mass=tab_data['mass'],
    #                         is_assembly_unit=tab_data['assembly_unit'],
    #                         parent_id=parent_id  # Связь с родителем
    #                     )
    #                     child_document.save()
    #                     print(f"Сохранен дочерний документ '{child_document.doc_name}' с ID {child_document.id}")
    #
    #         QMessageBox.information(self, "Успешно", "Данные успешно сохранены в базу данных.")
    #     except (IntegrityError, ValidationError) as e:
    #         print(f"Ошибка сохранения: {e}")
    #         QMessageBox.critical(self, "Ошибка", "Произошла ошибка при сохранении данных.")

    # def save_tabs_data_to_db(self):
    #     """Распаковывает список словарей и добавляет данные в соответствующие таблицы базы данных."""
    #
    #     """Выводит данные всех вкладок в консоль."""
    #     tabs_data = self.get_tabs_data()  # Получаем список словарей
    #     for tab_data in tabs_data:  # Проходим по всем данным вкладок
    #         print(tab_data)  # Выводим каждую запись
    #
    #     # Диагностика: выводим данные для проверки
    #     print("Данные для сохранения:", tabs_data)
    #
    #     # Проверка на пустые данные
    #     if not tabs_data:
    #         QMessageBox.warning(self, "Ошибка", "Нет данных для сохранения.")
    #         print("Отсутствуют корректные данные для сохранения.")
    #         return
    #
    #     # Процесс добавления данных
    #     for tab_data in tabs_data:
    #         doc_name = tab_data.get('doc_name')
    #         mass = tab_data.get('mass')
    #         assembly_unit = tab_data.get('assembly_unit')
    #         parent = tab_data.get('parent')
    #
    #         # Печать данных для диагностики
    #         print(f"Проверка записи: doc_name={doc_name}, mass={mass}, assembly_unit={assembly_unit}, parent={parent}")
    #
    #         # Проверка на наличие обязательных полей
    #         if not doc_name or mass is None or assembly_unit is None:
    #             print(f"Пропущена запись с некорректными данными (отсутствуют обязательные поля): {tab_data}")
    #             continue  # Пропускаем записи с некорректными данными
    #
    #         # Очищаем данные от пробелов (если они присутствуют)
    #         mass = mass.strip() if isinstance(mass, str) else str(mass).strip()
    #
    #         # Преобразуем массу в числовой формат
    #         try:
    #             mass = float(mass)  # Преобразуем в float
    #         except ValueError:
    #             print(f"Некорректная масса для записи (не удалось преобразовать): {tab_data}")
    #             mass = 0.0  # Если не удается преобразовать, ставим значение по умолчанию
    #
    #         # Печать после преобразования массы
    #         print(f"Масса после преобразования: {mass}")
    #
    #         # Дополнительная проверка после преобразования массы
    #         if mass <= 0:
    #             print(f"Масса должна быть положительным числом. Пропущена запись: {tab_data}")
    #             continue
    #
    #         # Создание или получение основного документа
    #         main_doc, created = MainDocument.objects.get_or_create(main_name=self.main_name)
    #
    #         # Добавление тегов
    #         tag_names = self.tags_tab_content.get_tag_list()  # Получаем теги из интерфейса
    #         for tag_name in tag_names:
    #             tag, created_tag = Tag.objects.get_or_create(name=tag_name)
    #             main_doc.tags.add(tag)
    #
    #         # Создание чертежа, связанного с основным документом
    #         drawing = Drawing.objects.create(
    #             main_document=main_doc,
    #             doc_name=doc_name,
    #             mass=mass,
    #             assembly_unit=assembly_unit,
    #             parent=parent  # Если есть родительский чертеж, связываем его
    #         )
    #
    #         # Создание листа чертежа, связанного с чертежом
    #         drawing_sheet = DrawingSheet.objects.create(
    #             drawing=drawing,
    #             file=self.file,
    #             sheet_number=self.sheet_number,
    #             is_actual=self.is_actual,
    #         )
    #
    #         print(f"Чертеж '{doc_name}' успешно сохранён.")
    #
    #     QMessageBox.information(None, "Успех", "Документы и чертежи успешно сохранены в базе данных.")

    def print_tabs_data(self):
        """Выводит данные всех вкладок в консоль."""
        tabs_data = self.get_tabs_data()  # Получаем список словарей
        for tab_data in tabs_data:  # Проходим по всем данным вкладок
            print(tab_data)  # Выводим каждую запись


    