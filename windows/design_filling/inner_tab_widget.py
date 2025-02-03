from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMessageBox
from .custom_tab_widget import CustomTabWidget
from .drawing_widget import DrawingWidget

class InnerTabWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        self.inner_tab_widget = CustomTabWidget()

        add_button = QPushButton("Добавить лист")
        add_button.clicked.connect(self.add_inner_tab)

        layout.addWidget(add_button)
        layout.addWidget(self.inner_tab_widget)
        self.setLayout(layout)

    def add_inner_tab(self):
        tab = QWidget()
        tab_layout = QVBoxLayout(tab)
        drawing_widget = DrawingWidget()

        # Подключаем сигнал к методу удаления вкладки
        drawing_widget.tabCloseRequested.connect(self.delete_current_inner_tab)

        tab_layout.addWidget(drawing_widget)

        self.sheet_number = self.inner_tab_widget.count() + 1

        tab_name = f"Лист {self.sheet_number}"
        self.inner_tab_widget.addTab(tab, tab_name)

    def delete_current_inner_tab(self):
        """
        Удаляет текущую вкладку (лист).
        """
        current_index = self.inner_tab_widget.currentIndex()

        if current_index != -1:
            print(f"Удаляем вкладку с индексом: {current_index}")
            self.inner_tab_widget.removeTab(current_index)
            QMessageBox.information(self, "Удаление", "Текущий лист был удалён.")
        else:
            QMessageBox.warning(self, "Ошибка", "Нет вкладки для удаления.")

    def get_inner_tabs_data(self, parent_tab):
        """Собирает данные о чертежах из внутренних вкладок."""
        inner_tabs_data = []

        #  Проверяем, есть ли `inner_tab_widget` у `parent_tab`
        if not hasattr(parent_tab, "inner_tab_widget") or not parent_tab.inner_tab_widget:
            print(
                f"⚠️ Ошибка: `inner_tab_widget` отсутствует в `{getattr(parent_tab, 'doc_name', 'Неизвестная вкладка')}`!")
            return []

        inner_tab_widget = parent_tab.inner_tab_widget

        #  Проверяем, содержит ли `inner_tab_widget` нужный объект
        if not hasattr(inner_tab_widget, "inner_tab_widget") or not inner_tab_widget.inner_tab_widget:
            print(
                f"⚠️ Ошибка: `inner_tab_widget.inner_tab_widget` отсутствует в `{getattr(parent_tab, 'doc_name', 'Неизвестная вкладка')}`!")
            return []

        inner_tab_widget = inner_tab_widget.inner_tab_widget  # Теперь это точно `QTabWidget`

        #  Проверяем, поддерживает ли `inner_tab_widget` метод `count()`
        if not hasattr(inner_tab_widget, "count"):
            print(
                f"⚠️ Ошибка: `inner_tab_widget` не поддерживает `count()` в `{getattr(parent_tab, 'doc_name', 'Неизвестная вкладка')}`!")
            return []

        #  Перебираем все внутренние вкладки
        for i in range(inner_tab_widget.count()):
            inner_tab = inner_tab_widget.widget(i)

            #  Проверяем, содержит ли вкладка `drawing_widget`
            if hasattr(inner_tab, "drawing_widget"):
                drawing_widget = inner_tab.drawing_widget

                #  Получаем путь к файлу и актуальность
                file_path = getattr(drawing_widget, "current_image_path", None)
                is_actual = getattr(drawing_widget, "check_box_is_actual", None)
                is_actual = is_actual.isChecked() if is_actual else False

                #  Добавляем данные в список
                inner_tabs_data.append({
                    "file": file_path,
                    "is_actual": is_actual
                })

                print(f"📄 Собран чертеж: {file_path} (Актуальность: {is_actual})")

        return inner_tabs_data


