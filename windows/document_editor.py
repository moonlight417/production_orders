import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QMessageBox, QDialog, \
    QScrollArea
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt
from print_dialog import PrintDialog

from products.models import DrawingSheet, MainDocument
import os
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QMessageBox, QDialog, QScrollArea, QFrame
)
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt
from print_dialog import PrintDialog
from products.models import DrawingSheet, MainDocument, Drawing, Tag


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

class DocumentEditor(QWidget):
    """Редактирование конструкторского документа с увеличением чертежа."""

    def __init__(self, doc_id, parent=None):
        super().__init__(parent)
        self.doc_id = doc_id
        self.parent = parent  # Сохраняем родительский `QStackedWidget`
        self.setWindowTitle(f"Редактирование документа (ID: {self.doc_id})")

        # 📄 Загружаем документ из базы
        try:
            self.document = MainDocument.objects.get(id=self.doc_id)
        except MainDocument.DoesNotExist:
            QMessageBox.critical(self, "Ошибка", f"Документ с ID {self.doc_id} не найден!")
            return

        # 🏗️ Основной layout
        main_layout = QHBoxLayout(self)

        # 📂 Левая часть (Чертёж)
        left_layout = QVBoxLayout()

        # Заголовок документа
        self.label = QLabel(f"<b>Документ:</b> {self.document.main_name}")
        self.label.setContentsMargins(0, 0, 0, 0)  # Убираем внешние отступы
        left_layout.addWidget(self.label)

        # Поле для отображения чертежа
        self.drawing_label = QLabel("📂 Чертёж отсутствует")
        self.drawing_label.setMouseTracking(True)  # Разрешаем отслеживание движения мыши
        self.drawing_label.setCursor(QCursor(Qt.PointingHandCursor))  # Меняем курсор на лупу
        left_layout.addWidget(self.drawing_label)

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

        self.save_button = QPushButton("Сохранить")
        self.save_button.clicked.connect(self.save_document)
        button_layout.addWidget(self.save_button)

        self.back_button = QPushButton("Назад")  # 🔹 Кнопка возврата
        self.back_button.clicked.connect(self.go_back)
        button_layout.addWidget(self.back_button)

        left_layout.addLayout(button_layout)
        main_layout.addLayout(left_layout, stretch=2)  # Левая часть занимает 2/3 экрана

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

    def load_drawing_image(self):
        """Загружает чертёж из базы и отображает его."""
        try:
            drawing_sheet = DrawingSheet.objects.filter(drawing__main_document=self.document, is_actual=True).first()
            if drawing_sheet and drawing_sheet.file:
                file_path = os.path.join("E:/Programming/production_orders/windows/design_filling", drawing_sheet.file.name)
                if os.path.exists(file_path):
                    self.pixmap = QPixmap(file_path)
                    if not self.pixmap.isNull():
                        self.drawing_label.setPixmap(self.pixmap.scaled(500, 500, Qt.KeepAspectRatio))
                        return file_path
                    else:
                        self.drawing_label.setText("⚠️ Ошибка загрузки изображения")
                else:
                    self.drawing_label.setText("❌ Файл не найден")
        except Exception as e:
            self.drawing_label.setText("❌ Ошибка загрузки чертежа")
            print(f"❌ Ошибка загрузки чертежа: {e}")

        return None

    def load_document_data(self):
        """Загружает и отображает данные документа в правой части."""
        self.scroll_layout.setAlignment(Qt.AlignTop)

        # 📌 Основная информация
        self.scroll_layout.addWidget(QLabel("<b>Информация о документе:</b>"))
        self.scroll_layout.addWidget(QLabel(f"📄 Название: {self.document.main_name}"))
        self.scroll_layout.addWidget(QLabel(f"🗒 Комментарий: {self.document.comment or '—'}"))

        # 🔖 Теги
        tags = self.document.tags.all()
        if tags:
            tag_names = ", ".join(tag.name for tag in tags)
        else:
            tag_names = "—"
        self.scroll_layout.addWidget(QLabel(f"🏷️ Теги: {tag_names}"))

        # 📌 Связанные чертежи
        self.scroll_layout.addWidget(QLabel("<b>Чертежи:</b>"))
        drawings = Drawing.objects.filter(main_document=self.document)
        if drawings.exists():
            for drawing in drawings:
                drawing_label = QLabel(f"📜 {drawing.doc_name}")
                self.scroll_layout.addWidget(drawing_label)
        else:
            self.scroll_layout.addWidget(QLabel("Нет чертежей"))

        # 📌 Листы чертежей
        self.scroll_layout.addWidget(QLabel("<b>Листы чертежей:</b>"))
        sheets = DrawingSheet.objects.filter(drawing__main_document=self.document)
        if sheets.exists():
            for sheet in sheets:
                sheet_label = QLabel(f"📄 Лист: {sheet.file.name} (Актуальность: {sheet.is_actual}, Масса: {sheet.mass or '—'} кг)")
                self.scroll_layout.addWidget(sheet_label)
        else:
            self.scroll_layout.addWidget(QLabel("Нет листов чертежей"))

        # 🔁 Обновляем макет
        self.scroll_content.setLayout(self.scroll_layout)

    def open_zoomed_window(self):
        """Открывает окно с увеличенным чертежом."""
        if not hasattr(self, 'pixmap') or self.pixmap.isNull():
            QMessageBox.warning(self, "Ошибка", "Нет изображения для увеличения.")
            return

        zoomed_window = ZoomedDrawingWindow(self.pixmap, self)
        zoomed_window.exec_()

    def open_printer_window(self):
        """Открывает окно печати чертежа."""
        if not self.current_image_path:
            QMessageBox.warning(self, "Ошибка", "Нет изображения для печати.")
            return
        self.printer_window = PrintDialog(self.current_image_path)
        self.printer_window.exec_()

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
        """Переключает `QStackedWidget` обратно на поиск документов."""
        self.parent.go_back_to_search()




