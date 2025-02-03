from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QScrollArea, QStackedWidget, QMessageBox
)
from products.models import MainDocument, Drawing, DrawingSheet
import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class DocumentHierarchy(QWidget):
    """Экран с иерархией документов."""

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(QLabel("<b>Иерархия документов</b>"))

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll.setWidget(self.scroll_content)
        self.layout.addWidget(self.scroll)

    def load_hierarchy(self, document):
        """Загружает и отображает иерархию документа."""
        try:
            print(f"Загружаем иерархию для документа: {document.main_name}")
            drawings = Drawing.objects.filter(main_document=document)

            for drawing in drawings:
                print(f"Чертеж: {drawing.doc_name}")

        except Exception as e:
            print(f"Ошибка при загрузке иерархии: {e}")
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить иерархию: {e}")

    def add_document_button(self, doc, level=0):
        """Добавляет кнопки для документов в иерархии."""
        document_name = doc.main_name if isinstance(doc, MainDocument) else doc.doc_name

        button = QPushButton(f"{' ' * (level * 4)}📄 {document_name}")
        button.setStyleSheet(f"padding-left: {level * 20}px; text-align: left;")
        button.clicked.connect(lambda: self.parent.show_drawing_screen(doc))
        self.scroll_layout.addWidget(button)

        if isinstance(doc, MainDocument):
            child_drawings = Drawing.objects.filter(main_document=doc)
            if child_drawings.exists():
                for drawing in child_drawings:
                    self.add_document_button(drawing, level=level + 1)
        else:
            child_drawings = doc.children.all()
            if child_drawings.exists():
                for drawing in child_drawings:
                    self.add_document_button(drawing, level=level + 1)


class DocumentEditor(QWidget):
    """Экран просмотра чертежа."""

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.current_document = None

        layout = QVBoxLayout(self)

        self.label = QLabel("")
        layout.addWidget(self.label)

        self.drawing_label = QLabel("📂 Чертёж отсутствует")
        layout.addWidget(self.drawing_label)

        self.print_button = QPushButton("🖨 Печать")
        self.print_button.clicked.connect(self.open_printer_window)
        layout.addWidget(self.print_button)

        self.comment_edit = QTextEdit()
        layout.addWidget(self.comment_edit)

        self.save_button = QPushButton("Сохранить")
        self.save_button.clicked.connect(self.save_document)
        layout.addWidget(self.save_button)

        self.back_button = QPushButton("Назад")
        self.back_button.clicked.connect(self.parent.show_hierarchy_screen)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def load_document(self, doc):
        """Загружает документ и чертёж."""
        self.current_document = doc
        self.label.setText(f"<b>Документ:</b> {doc.main_name}")
        self.comment_edit.setText(doc.comment or "")

        drawing_sheet = DrawingSheet.objects.filter(drawing__main_document=doc, is_actual=True).first()
        if drawing_sheet and drawing_sheet.file:
            file_path = os.path.join("E:/Programming/production_orders/windows/design_filling",
                                     drawing_sheet.file.name)
            if os.path.exists(file_path):
                try:
                    self.drawing_label.setPixmap(QPixmap(file_path).scaled(500, 500, Qt.KeepAspectRatio))
                except Exception as e:
                    print(f"Ошибка при загрузке изображения: {e}")
                    self.drawing_label.setText("❌ Ошибка при загрузке изображения")
            else:
                print("Ошибка: Файл не найден")
                self.drawing_label.setText("❌ Файл не найден")
        else:
            self.drawing_label.setText("📂 Чертёж отсутствует")

    def open_printer_window(self):
        """Открывает окно печати чертежа."""
        QMessageBox.information(self, "Печать", "Функция печати пока не реализована!")

    def save_document(self):
        """Сохраняет комментарий."""
        if self.current_document:
            self.current_document.comment = self.comment_edit.toPlainText()
            self.current_document.save()
            QMessageBox.information(self, "Успех", "Комментарий сохранён!")


class DocumentViewer(QWidget):
    """Основной стек-виджет для переключения страниц."""

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.btn_back_to_search = QPushButton("← Назад")
        self.btn_back_to_search.clicked.connect(self.go_back_to_search_screen)

        layout = QVBoxLayout(self)
        layout.addWidget(self.btn_back_to_search)

        self.stack = QStackedWidget(self)
        self.hierarchy_screen = DocumentHierarchy(self)
        self.editor_screen = DocumentEditor(self)

        self.stack.addWidget(self.hierarchy_screen)
        self.stack.addWidget(self.editor_screen)

        layout.addWidget(self.stack)
        self.setLayout(layout)

    def show_hierarchy_screen(self):
        """Показывает экран иерархии документов."""
        self.hierarchy_screen.load_hierarchy(None)
        self.stack.setCurrentWidget(self.hierarchy_screen)

    def show_drawing_screen(self, doc):
        """Показывает экран с чертежом."""
        self.editor_screen.load_document(doc)
        self.stack.setCurrentWidget(self.editor_screen)

    def go_back_to_search_screen(self):
        """Возвращение на экран поиска."""
        self.parent().stack.setCurrentIndex(0)
        self.parent().update_navigation_buttons()




