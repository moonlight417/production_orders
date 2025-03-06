import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QMessageBox, QDialog, \
    QScrollArea, QLayout, QSpacerItem, QSizePolicy, QStackedWidget
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt
from print_dialog import PrintDialog
import importlib
from products.models import DrawingSheet, MainDocument
import os
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QMessageBox, QDialog, QScrollArea, QFrame
)
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt
from print_dialog import PrintDialog
from products.models import DrawingSheet, MainDocument, Drawing, Tag
from windows.design_edit.design_document_edit_form import DesignDocumentEditForm


# from windows.design_edit.design_document_edit_form import DesignDocumentEditForm


class ZoomedDrawingWindow(QDialog):
    """Окно для отображения увеличенной версии чертежа с прокруткой."""

    def __init__(self, pixmap, parent=None):
        super().__init__(parent)
        self.setWindowTitle("🔍 Увеличенный чертёж")
        self.setFixedSize(800, 800)  # Увеличенный размер окна
        self.setWindowFlags(Qt.Window)

        # Создаём QScrollArea для добавления прокрутки
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)  # Разрешаем изменение размера области прокрутки
        layout = QVBoxLayout(self)
        layout.addWidget(scroll_area)

        # Создаём QLabel для отображения изображения
        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)

        # Устанавливаем QLabel в качестве содержимого для QScrollArea
        scroll_area.setWidget(self.image_label)

class DocumentViewer(QWidget):
    """Редактирование конструкторского документа с увеличением чертежа."""

    def __init__(self, doc_id, parent=None):
        super().__init__(parent)
        self.doc_id = doc_id
        self.parent = parent  # Сохраняем родительский `QStackedWidget`
        self.setWindowTitle(f"Просмотр документа (ID: {self.doc_id})")

        # 📄 Загружаем документ из базы
        try:
            self.document = MainDocument.objects.get(id=self.doc_id)
        except MainDocument.DoesNotExist:
            QMessageBox.critical(self, "Ошибка", f"Документ с ID {self.doc_id} не найден!")
            return

        # 🏗️ Основной layout
        main_layout = QHBoxLayout(self)

        # 📂 Левая часть (Чертёж)
        self.left_layout = QVBoxLayout()  # ✅ Теперь `left_layout` сохранён в `self`

        # Заголовок документа
        self.label = QLabel(f"<b>Документ:</b> {self.document.main_name}")
        self.label.setContentsMargins(0, 0, 0, 0)  # Убираем внешние отступы
        self.label.setStyleSheet("margin: 0px; padding: 0px; font-size: 14pt;")  # Убираем внутренние отступы
        self.label.setFixedHeight(30)  # Фиксированная высота, чтобы не растягивался
        self.left_layout.addWidget(self.label)

        # Поле для отображения чертежа
        self.drawing_label = QLabel("📂 Чертёж отсутствует")
        self.drawing_label.setMouseTracking(True)  # Разрешаем отслеживание движения мыши
        self.drawing_label.setCursor(QCursor(Qt.PointingHandCursor))  # Меняем курсор на лупу
        self.left_layout.addWidget(self.drawing_label)

        button_layout = QHBoxLayout()

        # Загружаем чертёж
        self.current_image_path = self.load_drawing_image()

        # Кнопка "🔍 Увеличить"
        self.zoom_button = QPushButton("🔍 Увеличить чертёж")
        self.zoom_button.clicked.connect(self.open_zoomed_window)
        button_layout.addWidget(self.zoom_button)

        # Кнопка "Печать"
        self.print_button = QPushButton("🖨 Печать")
        self.print_button.clicked.connect(self.open_printer_window)
        button_layout.addWidget(self.print_button)

        # # Поле для комментария
        # self.comment_edit = QTextEdit()
        # self.comment_edit.setText(self.document.comment or "")
        # left_layout.addWidget(self.comment_edit)

        # Кнопки "Сохранить" и "Назад"

        self.edit_button = QPushButton("Редактировать")
        self.edit_button.clicked.connect(self.open_edit_window)
        button_layout.addWidget(self.edit_button)

        self.back_button = QPushButton("Назад")  # 🔹 Кнопка возврата
        self.back_button.clicked.connect(self.go_back)
        button_layout.addWidget(self.back_button)

        self.left_layout.addLayout(button_layout)
        main_layout.addLayout(self.left_layout, stretch=2)  # Левая часть занимает 2/3 экрана

        # 📜 Правая часть (Данные документа)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)

        # Загружаем данные документа
        self.load_document_data()

        self.scroll_area.setWidget(self.scroll_content)
        main_layout.addWidget(self.scroll_area, stretch=1)  # Правая часть занимает 1/3 экрана

        self.setLayout(main_layout)

    from PyQt5.QtWidgets import QLayout  # Убедитесь, что импортировали QLayout

    def load_drawing_image(self):
        """Загружает чертёж из базы и отображает его."""
        try:
            # 🔍 Загружаем чертёж, фильтруя по актуальности
            drawing_sheet = DrawingSheet.objects.filter(drawing__main_document=self.document, is_actual=True).first()

            # Проверка наличия листа чертежа и файла
            if drawing_sheet and drawing_sheet.file:
                # Новая логика с обновленным путем
                file_path = os.path.join("F:/AS_Folder/production_orders/windows/design_filling",
                                         drawing_sheet.file.name)

                # Проверим путь и выведем его для отладки
                print(f"📂 Загружаем чертёж из: {file_path}")

                # Убедитесь, что файл существует по новому пути
                if os.path.exists(file_path):
                    print("✅ Файл найден, пробуем загрузить в QPixmap")
                    self.pixmap = QPixmap(file_path)

                    if not self.pixmap.isNull():
                        print("✅ Чертёж успешно загружен в QPixmap")
                        self.drawing_label.setPixmap(self.pixmap.scaled(600, 600, Qt.KeepAspectRatio))
                        self.current_image_path = file_path  # Обновляем путь к файлу
                        print(f"🔄 Путь к изображению для печати: {self.current_image_path}")
                    else:
                        print("❌ Ошибка: QPixmap вернул пустое изображение")
                        self.drawing_label.setText("⚠️ Ошибка загрузки изображения")
                else:
                    print(f"❌ Ошибка: Файл не найден по пути: {file_path}")
                    self.drawing_label.setText("❌ Файл не найден")
            else:
                print("❌ Ошибка: Чертёж отсутствует или неактуален")
                self.drawing_label.setText("📂 Чертёж отсутствует")
        except Exception as e:
            print(f"❌ Ошибка загрузки чертежа: {e}")
            self.drawing_label.setText("❌ Ошибка загрузки чертежа")

        return None

    def load_document_data(self):
        """Загружает и отображает данные документа в правой части (QScrollArea)."""
        self.scroll_layout.setAlignment(Qt.AlignTop)

        # 📌 Основная информация
        self.scroll_layout.addWidget(QLabel("<b>Информация о документе:</b>"))
        self.scroll_layout.addWidget(QLabel(f"📄 Название: {self.document.main_name}"))
        self.scroll_layout.addWidget(QLabel(f"🗒 Комментарий: {self.document.comment or '—'}"))

        # 🔖 Теги
        tags = self.document.tags.all()
        tag_names = ", ".join(tag.name for tag in tags) if tags else "—"
        self.scroll_layout.addWidget(QLabel(f"🏷️ Теги: {tag_names}"))

        # 📜 Загружаем иерархию родитель-потомок
        self.load_hierarchy()

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.scroll_layout.addItem(spacer)

       #  # Поле для комментария
       #  self.comment_edit = QTextEdit()
       #  self.comment_edit.setMaximumHeight(50)
       #  self.comment_edit.setText(f"🗒 Комментарий: {self.document.comment or ""}")
       #  self.scroll_layout.addWidget(self.comment_edit)
       #
       # # Поле для тегов
       #  self.tag_edit = QTextEdit()
       #  self.tag_edit.setMaximumHeight(50)
       #  self.tag_edit.setText(f"🏷️ Теги: {tag_names}")
       #  self.scroll_layout.addWidget(self.tag_edit)

        # 🔁 Обновляем макет
        self.scroll_content.setLayout(self.scroll_layout)

    def open_zoomed_window(self):
        """Открывает окно с увеличенным чертежом."""
        if not hasattr(self, 'pixmap') or self.pixmap.isNull():
            QMessageBox.warning(self, "Ошибка", "Нет изображения для увеличения.")
            return

        zoomed_window = ZoomedDrawingWindow(self.pixmap, self)
        zoomed_window.exec_()

    def load_hierarchy(self):
        """Загружает иерархию документов, добавляя кнопки с отступами для родительских и дочерних чертежей."""
        self.scroll_layout.setAlignment(Qt.AlignTop)

        self.scroll_layout.addWidget(QLabel("<b>Иерархия чертежей:</b>"))

        # 🔍 Получаем ВСЕ корневые чертежи (без родителя)
        root_drawings = Drawing.objects.filter(main_document=self.document, parent=None)

        for drawing in root_drawings:
            self.add_drawing_button(drawing, 0)  # Родители идут с уровнем 0

    def add_drawing_button(self, drawing, level):
        """Создаёт кнопку чертежа в иерархии с отступами для дочерних элементов."""

        # 🔍 Определяем цвет кнопки
        sheet = DrawingSheet.objects.filter(drawing=drawing, is_actual=True).first()
        if sheet and sheet.mass is not None:
            color = "green"  # ✅ Актуальный с массой
            mass_text = f" ⚖️ {sheet.mass} кг"
        elif sheet:
            color = "yellow"  # ⚠️ Актуальный, но без массы
            mass_text = " ❌ Без массы"
        else:
            color = "red"  # ⛔ Неактуальный
            mass_text = " ⛔ Неактуальный"

        # 🔹 Создаём кнопку
        button = QPushButton(f"{' ' * (level * 4)}📄 {drawing.doc_name}{mass_text}")
        button.clicked.connect(lambda: self.load_new_drawing(drawing))

        # 🎨 Применяем цвет кнопки
        if color == "green":
            button.setStyleSheet(f"background-color: #DFFFD6; color: black; padding-left: {level * 20}px;")
        elif color == "yellow":
            button.setStyleSheet(f"background-color: #FFFFCC; color: black; padding-left: {level * 20}px;")
        elif color == "red":
            button.setStyleSheet(f"background-color: #FFC0CB; color: black; padding-left: {level * 20}px;")

        self.scroll_layout.addWidget(button)

        # 🔽 Добавляем дочерние чертежи с увеличенным уровнем отступа
        child_drawings = Drawing.objects.filter(parent=drawing)
        for child in child_drawings:
            self.add_drawing_button(child, level + 1)  # Увеличиваем уровень вложенности

    def load_new_drawing(self, drawing):
        """Загружает новый чертёж в левую часть экрана."""
        self.label.setText(f"<b>Документ:</b> {drawing.doc_name}")

        drawing_sheet = DrawingSheet.objects.filter(drawing=drawing, is_actual=True).first()
        if drawing_sheet and drawing_sheet.file:
            file_path = os.path.join("F:/AS_Folder/production_orders/windows/design_filling", drawing_sheet.file.name)
            if os.path.exists(file_path):
                self.pixmap = QPixmap(file_path)
                if not self.pixmap.isNull():
                    self.drawing_label.setPixmap(self.pixmap.scaled(600, 600, Qt.KeepAspectRatio))
                else:
                    self.drawing_label.setText("⚠️ Ошибка загрузки изображения")
            else:
                self.drawing_label.setText("❌ Файл не найден")
        else:
            self.drawing_label.setText("📂 Чертёж отсутствует")

    def load_new_document(self, doc_id):
        """Переключает текущий документ и загружает новый чертёж."""
        print(f"🔄 Загружаем новый документ ID: {doc_id}")

        try:
            self.document = MainDocument.objects.get(id=doc_id)
            self.label.setText(f"<b>Документ:</b> {self.document.main_name}")

            # ✅ Загружаем чертёж и обновляем иерархию
            self.load_drawing_image()
            self.load_hierarchy()

            print(f"✅ Документ {self.document.main_name} загружен!")

        except MainDocument.DoesNotExist:
            QMessageBox.critical(self, "Ошибка", f"Документ с ID {doc_id} не найден!")
            print(f"❌ Документ с ID {doc_id} не найден!")

    def open_printer_window(self):
        """Открывает окно печати чертежа."""
        print(f"🔄 Текущий путь к изображению перед печатью: {self.current_image_path}")

        if not self.current_image_path:
            QMessageBox.warning(self, "Ошибка", "Нет изображения для печати.")
            print("❌ Нет изображения для печати (путь не задан).")
            return

        # Дополнительная проверка существования файла
        if not os.path.exists(self.current_image_path):
            QMessageBox.warning(self, "Ошибка", "Файл не найден для печати.")
            print(f"❌ Файл не найден для печати по пути: {self.current_image_path}")
            return

        # Если путь к файлу существует, то открываем окно печати
        print(f"✅ Печать будет выполняться для файла: {self.current_image_path}")
        self.printer_window = PrintDialog(self.current_image_path)
        self.printer_window.exec_()

    def open_edit_window(self):
        """Открывает окно редактирования документа в `QStackedWidget`, предотвращая дублирование."""
        try:
            main_id = self.document.id
            print(f"📝 Открываем редактирование документа ID: {main_id}")

            if not hasattr(self.parent, "stack"):
                print("❌ Ошибка: `QStackedWidget` не найден, открываю как отдельное окно.")
                self.edit_window = DesignDocumentEditForm(main_id)
                self.edit_window.show()
                print("✅ Открыто отдельное окно.")
                return

            # Поиск существующего окна
            existing_window = None
            for i in range(self.parent.stack.count()):
                widget = self.parent.stack.widget(i)
                if isinstance(widget, DesignDocumentEditForm) and widget.main_id == main_id:
                    existing_window = widget
                    break

            if existing_window:
                print("⚠️ Окно редактирования уже существует! Просто переключаемся на него.")
                self.parent.stack.setCurrentWidget(existing_window)
            else:
                print("➕ Создаём новое окно редактирования.")
                self.edit_window = DesignDocumentEditForm(main_id)
                self.parent.stack.addWidget(self.edit_window)
                self.parent.stack.setCurrentWidget(self.edit_window)
                print("✅ Окно добавлено в QStackedWidget.")
        except Exception as e:
            print(f"❌ Ошибка при открытии окна редактирования: {e}")
            QMessageBox.critical(self, "Ошибка", f"Не удалось открыть редактор: {e}")

    def save_document(self):
        """Сохраняет изменения в документе."""
        try:
            self.document.comment = self.comment_edit.toPlainText()
            self.document.save()
            QMessageBox.information(self, "Успех", "Комментарий обновлён!")
            self.go_back()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить документ: {e}")

    def go_back(self):
        """🏳 Переключает `QStackedWidget` обратно на поиск документов."""
        self.parent.go_back_to_search()




