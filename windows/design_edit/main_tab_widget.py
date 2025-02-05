import sys
import os
from django.db import transaction, IntegrityError
from functools import partial
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QPushButton,
    QLabel, QScrollArea, QFrame, QMessageBox, QInputDialog, QRadioButton, QCheckBox, QGridLayout, QLineEdit)
from PyQt5.QtCore import Qt
from django.core.exceptions import ValidationError
from products.models import MainDocument, Tag, Drawing, DrawingSheet
from windows.design_edit.tags_tab_content import TagsTabContent
from windows.design_edit.drawing_tab_widget import UnifiedDrawingTabWidget

class MainTabWidget(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui  # Сохраняем ссылку на интерфейс
        self.initialize_ui()

        self.current_image_path = None  # ✅ Добавляем переменную для хранения пути к файлу

        self.linked_tab = None  # Вкладка, связанная с главным именем
        self.selected_radio_button = None

        # Данные по умолчанию
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

        # ✅ Безопасное создание UnifiedDrawingTabWidget
        try:
            tab.drawing_tab_widget = UnifiedDrawingTabWidget()
        except Exception as e:
            print(f"❌ Ошибка создания drawing_tab_widget: {e}")
            return  # ❌ Если ошибка — выходим, не добавляя вкладку

        # Создаём область прокрутки
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedWidth(200)
        scroll_frame = QFrame()
        scroll_layout = QVBoxLayout(scroll_frame)
        scroll_layout.setAlignment(Qt.AlignTop)
        scroll_area.setWidget(scroll_frame)

        # Чекбокс
        check_box = QCheckBox("Добавить в СБ", self)
        check_box.stateChanged.connect(partial(self.on_check_box_state_changed, tab))

        # ✅ Создаём макет вкладки
        tab_layout = QGridLayout(tab)

        tab_layout.addWidget(check_box, 0, 0)
        tab_layout.addWidget(scroll_area, 1, 0, 1, 1)
        tab_layout.addWidget(tab.drawing_tab_widget, 0, 1, 2, 1)  # ✅ Теперь точно есть drawing_tab_widget

        # ✅ Добавляем вкладку в `main_tab_widget`
        self.main_tab_widget.addTab(tab, tab_name)
        new_index = self.main_tab_widget.count() - 1
        self.main_tab_widget.setCurrentIndex(new_index)

        # Сохраняем ссылки на элементы
        self.scroll_areas[tab] = scroll_layout
        self.tab_types[tab] = tab_name
        self.check_boxes[tab] = check_box
        self.radio_buttons[tab] = []

        tab.is_assembly_unit = is_assembly_unit

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
                    # mass_input = self._find_mass_input(tab)
                    # mass = float(mass_input.text()) if mass_input and mass_input.text() else None

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
                        # 'mass': mass,
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

    # def _find_mass_input(self, parent_widget):
    #     """
    #     Рекурсивно ищет self.lineEditMass в дочерних виджетах.
    #     :param parent_widget: Родительский виджет, в котором искать.
    #     :return: Найденный QLineEdit или None.
    #     """
    #     # Если текущий виджет имеет атрибут lineEditMass, возвращаем его
    #     if hasattr(parent_widget, 'lineEditMass'):
    #         return parent_widget.lineEditMass
    #
    #     # Если у виджета есть дочерние элементы, ищем среди них
    #     for child in parent_widget.children():
    #         result = self._find_mass_input(child)
    #         if result:
    #             return result
    #
    #     return None

    def save_to_db(self):
        """Сохраняет данные вкладок в базу данных."""
        if self.linked_tab is None:
            QMessageBox.warning(self, "Ошибка", "Связанная вкладка не выбрана. Проверьте корректность данных.")
            return

        tag_names = self.tags_tab_content.get_tag_list()
        if not tag_names:
            QMessageBox.warning(self, "Ошибка", "Необходимо добавить хотя бы один тег.")
            return

        tabs_data, main_parent_name = self.get_tabs_data()
        if not main_parent_name:
            QMessageBox.warning(self, "Ошибка", "Главная сборка не найдена.")
            return

        try:
            with transaction.atomic():
                main_doc, _ = MainDocument.objects.get_or_create(
                    main_name=main_parent_name,
                    defaults={'comment': self.ui.textEditComments.toPlainText()}
                )

                for tag_name in tag_names:
                    tag, _ = Tag.objects.get_or_create(name=tag_name)
                    main_doc.tags.add(tag)

                parent_tabs = [tab for tab in tabs_data if tab['parent'] is None]
                child_tabs = [tab for tab in tabs_data if tab['parent'] is not None]
                parent_drawings = {}

                # ✅ Создаём родительские документы
                for parent_tab in parent_tabs:
                    drawing, _ = Drawing.objects.get_or_create(
                        doc_name=parent_tab['doc_name'],
                        defaults={'main_document': main_doc, 'parent': None}
                    )
                    parent_drawings[drawing.doc_name] = drawing

                # ✅ Создаём дочерние документы
                for child_tab in child_tabs:
                    parent_name = child_tab['parent']
                    parent_drawing = parent_drawings.get(parent_name)

                    if not parent_drawing:
                        print(f"❌ Ошибка: Не найден родительский документ для {child_tab['doc_name']}")
                        continue  # ❌ Пропускаем некорректные данные

                    drawing, _ = Drawing.objects.get_or_create(
                        doc_name=child_tab['doc_name'],
                        defaults={'main_document': main_doc, 'parent': parent_drawing}
                    )

                    parent_drawings[drawing.doc_name] = drawing  # ✅ Добавляем дочерний `Drawing` в parent_drawings

                # ✅ Обрабатываем чертежные листы
                for tab_data in tabs_data:
                    tab_widget = self.get_tab_by_name(tab_data['doc_name'])

                    if not tab_widget or not hasattr(tab_widget, "drawing_tab_widget"):
                        print(f"⚠️ Ошибка: Вкладка '{tab_data['doc_name']}' не содержит `drawing_tab_widget`!")
                        continue  # ❌ Пропускаем вкладку

                    # ✅ Проверяем, содержит ли `drawing_tab_widget` нужный метод
                    if not hasattr(tab_widget.drawing_tab_widget, "get_inner_tabs_data"):
                        print(
                            f"⚠️ Ошибка: `{tab_data['doc_name']}.drawing_tab_widget` не содержит `get_inner_tabs_data()`!")
                        continue

                    # ✅ Получаем данные чертежей
                    inner_tabs_data = tab_widget.drawing_tab_widget.get_inner_tabs_data()


                    for sheet_data in inner_tabs_data:
                        file_path = sheet_data.get("file")
                        is_actual = sheet_data.get("is_actual", False)
                        mass = sheet_data.get("mass", None)

                        if file_path:
                            drawing = parent_drawings.get(tab_data['doc_name'])  # Проверяем связь!
                            if not drawing:
                                print(f"⚠️ Ошибка: Не найден объект `Drawing` для '{tab_data['doc_name']}'!")
                                continue

                            print(f"📄 Сохраняем чертеж: {file_path} (Актуальность: {is_actual})")
                            DrawingSheet.objects.create(
                                drawing=drawing,
                                file=file_path,
                                is_actual=is_actual,
                                mass=mass
                            )

            QMessageBox.information(None, "Успех", "Документ и данные вкладок успешно сохранены в базе данных.")
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

    def print_tabs_data(self):
        """Выводит данные всех вкладок в консоль."""
        tabs_data = self.get_tabs_data()  # Получаем список словарей
        for tab_data in tabs_data:  # Проходим по всем данным вкладок
            print(tab_data)  # Выводим каждую запись

    def get_tab_by_name(self, doc_name):
        """Поиск вкладки по её имени"""
        for i in range(self.main_tab_widget.count()):
            tab = self.main_tab_widget.widget(i)
            if self.main_tab_widget.tabText(i) == doc_name:
                return tab
        return None  # ❌ Если вкладка не найдена







    