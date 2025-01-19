import sys
import requests
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QPushButton,
    QLabel, QScrollArea, QFrame, QMessageBox, QInputDialog, QRadioButton, QCheckBox, QGridLayout
)
from PyQt5.QtCore import Qt
from functools import partial

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "e:/Programming/production_orders/")))
from windows.design_filling.tags_tab_content import TagsTabContent
from windows.design_filling.inner_tab_widget import InnerTabWidget
from windows.design_filling.rename_tab_dialog import RenameTabDialog
from windows.design_filling.drawing_widget import DrawingWidget
# from .tags_tab_content import TagsTabContent
# from .inner_tab_widget import InnerTabWidget
# from .rename_tab_dialog import RenameTabDialog


class MainTabWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Основной виджет с вкладками
        self.main_tab_widget = QTabWidget()

        self.main_name = ""
        self.linked_tab = None  # Вкладка, от которой зависит main_name

        self.label_main_name = QtWidgets.QLabel(self.main_name)
        self.label_main_name.setStyleSheet("font-size: 16pt; font-family: Arial;")

        # Кнопки для управления вкладками
        button_layout = QHBoxLayout()
        add_assembly_button = QPushButton("+ СБ")
        add_assembly_button.clicked.connect(self.add_assembly_unit_tab)

        add_detail_button = QPushButton("+ Деталь")
        add_detail_button.clicked.connect(self.add_detail_tab)

        rename_tab_button = QPushButton("Назвать элемент")
        rename_tab_button.clicked.connect(self.rename_current_tab)

        close_tab_button = QPushButton("Закрыть текущую вкладку")
        close_tab_button.clicked.connect(self.close_current_tab)

        # update_name_button = QPushButton("Обновить название")
        # update_name_button.clicked.connect(self.update_main_name)

        button_layout.addWidget(self.label_main_name)
        button_layout.addWidget(add_assembly_button)
        button_layout.addWidget(add_detail_button)
        button_layout.addWidget(rename_tab_button)
        button_layout.addWidget(close_tab_button)
        # button_layout.addWidget(update_name_button)  # Добавляем кнопку "Обновить название"

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
        self.linked_tab = self.main_tab_widget.currentWidget()
        self.main_name = "Сборочная единица"
        self.update_main_name()

    def add_detail_tab(self):
        """Добавляет новую вкладку с названием 'Деталь'."""
        self._add_tab("Деталь")
        self.linked_tab = self.main_tab_widget.currentWidget()
        self.main_name = "Деталь"
        self.update_main_name()

    def _add_tab(self, tab_name):
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

    def save_all_tabs_to_database(self):
        """Сохраняет данные всех вкладок в базу данных через API."""
        total_tabs = self.main_tab_widget.count()

        if total_tabs == 0:
            QMessageBox.warning(self, "Предупреждение", "Нет вкладок для сохранения данных.")
            return

        tab_data_list = []

        for index in range(total_tabs):
            tab_name = self.main_tab_widget.tabText(index)
            # Пропускаем защищённые вкладки
            if self.main_tab_widget.widget(index) in self.protected_tabs:
                continue

            # Получаем содержимое для поля 'comment' и 'main_name'
            comment = self.ui.textEditComment.toPlainText()  # Содержимое комментария
            main_name = self.main_name  # Название главной сборочной единицы

            # Пропуск вкладок с неактуальными данными
            if not main_name or not comment:
                continue

            # Дополнительные данные для каждой вкладки
            parent_id = None
            if self.ui.comboBoxParentDrawing.currentIndex() != -1:
                parent_id = self.ui.comboBoxParentDrawing.currentData()

            # Для получения файла, листа и актуальности
            file = None  # Получить файл чертежа
            sheet_number = 1  # Используйте данные из UI, если они есть
            is_actual = True  # Можно использовать чекбокс для актуальности

            # Сформировать данные для вкладки
            tab_data = {
                "main_name": main_name,
                "doc_name": tab_name,
                "parent": parent_id,
                "mass": float(self.ui.lineEditMass.text()),  # Масса
                "assembly_unit": self.ui.checkBoxAssemblyUnit.isChecked(),
                "comment": comment,
                "sheet_number": sheet_number,
                "file": file,  # Укажите путь к файлу или файл
                "is_actual": is_actual
            }

            # Сбор данных для тегов
            tags = []  # Список тегов для вкладки
            for tag in self.ui.comboBoxTags.selectedItems():  # Пример для получения выбранных тегов
                tags.append(tag.text())

            # Добавляем теги к данным
            tab_data["tags"] = tags

            tab_data_list.append(tab_data)

        # Отправляем данные через API
        try:
            response = requests.post("http://127.0.0.1:8000/products/add_drawings/", json=tab_data_list)
            if response.status_code == 201:
                QMessageBox.information(self, "Успех", "Все вкладки успешно сохранены в базу.")
            else:
                QMessageBox.critical(self, "Ошибка", f"Ошибка при сохранении данных: {response.text}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Ошибка", f"Сбой при подключении к серверу: {str(e)}")

    #
    #     # Проверка, что все поля задания заполнены
    #     if not all(design_document_data.values()):
    #         QtWidgets.QMessageBox.warning(self, "Ошибка", "Заполните все поля корректно.")
    #         return
    #
    #     # Проверка, что добавлен хотя бы один продукт
    #     product_data_list = self.collect_product_data(None)  # Передаем None, так как task_id пока неизвестен
    #     if not product_data_list:
    #         QtWidgets.QMessageBox.warning(self, "Ошибка", "Добавьте хотя бы один продукт и заполните все поля.")
    #         return
    #
    #     try:
    #         # Сначала отправляем задание и получаем task_id
    #         response = requests.post(
    #             "http://127.0.0.1:8000/orders/add_customer_and_task/",
    #             json=design_document_data
    #         )
    #         if response.status_code == 201:
    #             task_id = response.json().get("task_id")
    #             if not task_id:
    #                 QtWidgets.QMessageBox.warning(self, "Ошибка", "Не удалось получить ID задания.")
    #                 return
    #
    #             # Теперь добавляем task_id к каждому продукту
    #             for product_data in product_data_list:
    #                 product_data["task_id"] = task_id
    #
    #             # Отправляем данные о продуктах
    #             for product_data in product_data_list:
    #                 response = requests.post("http://127.0.0.1:8000/products/add_product/", json=product_data)
    #                 if response.status_code != 201:
    #                     QtWidgets.QMessageBox.warning(
    #                         self,
    #                         "Ошибка",
    #                         f"Ошибка при добавлении продукта: {response.text}"
    #                     )
    #                     return
    #
    #             QtWidgets.QMessageBox.information(self, "Успех", "Данные успешно добавлены!")
    #             self.clear_products()
    #             self.ui.lineEditCustomer.clear()
    #             check_number = self.get_max_value_from_database("orders_task", "invoice_number")
    #             self.ui.lineEditCheckNumber.setText(str(check_number + 1))
    #         else:
    #             QtWidgets.QMessageBox.warning(self, "Ошибка", f"Ошибка сервера: {response.text}")
    #     except Exception as e:
    #         QtWidgets.QMessageBox.critical(self, "Ошибка", f"Не удалось отправить данные: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainTabWidget()
    window.show()
    sys.exit(app.exec_())

