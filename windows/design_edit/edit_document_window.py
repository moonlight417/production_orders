from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem, QMessageBox, QDialog
from products.models import MainDocument, Drawing, DrawingSheet, Tag
from django.db import transaction

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem, QMessageBox, QDialog
from products.models import MainDocument, Drawing, DrawingSheet, Tag
from django.db import transaction

class EditDocumentWindow(QDialog):
    def __init__(self, doc_id, parent=None):
        super().__init__(parent)
        self.doc_id = doc_id
        self.parent_window = parent
        self.setWindowTitle("Редактирование документа")
        self.setGeometry(100, 100, 800, 600)

        self.main_layout = QVBoxLayout(self)

        # Основная информация о документе
        self.main_info_layout = QVBoxLayout()
        self.main_info_layout.addWidget(QLabel("Основная информация:"))

        self.name_edit = QLineEdit()
        self.main_info_layout.addWidget(QLabel("Название:"))
        self.main_info_layout.addWidget(self.name_edit)

        self.comment_edit = QTextEdit()
        self.main_info_layout.addWidget(QLabel("Комментарий:"))
        self.main_info_layout.addWidget(self.comment_edit)

        self.main_layout.addLayout(self.main_info_layout)

        # Теги
        self.tags_layout = QVBoxLayout()
        self.tags_layout.addWidget(QLabel("Теги:"))
        self.tags_edit = QLineEdit()
        self.tags_layout.addWidget(self.tags_edit)
        self.main_layout.addLayout(self.tags_layout)

        # Чертежи
        self.drawings_layout = QVBoxLayout()
        self.drawings_layout.addWidget(QLabel("Чертежи:"))
        self.drawings_table = QTableWidget()
        self.drawings_table.setColumnCount(4)
        self.drawings_table.setHorizontalHeaderLabels(["ID", "Название", "Актуальность", "Масса"])
        self.drawings_layout.addWidget(self.drawings_table)
        self.main_layout.addLayout(self.drawings_layout)

        # Кнопки
        self.button_layout = QHBoxLayout()
        self.save_button = QPushButton("Сохранить")
        self.save_button.clicked.connect(self.save_changes)
        self.button_layout.addWidget(self.save_button)

        self.back_button = QPushButton("Назад")
        self.back_button.clicked.connect(self.close)
        self.button_layout.addWidget(self.back_button)

        self.main_layout.addLayout(self.button_layout)

        self.load_data()

    def load_data(self):
        try:
            self.document = MainDocument.objects.get(id=self.doc_id)
            self.name_edit.setText(self.document.main_name)
            self.comment_edit.setText(self.document.comment)

            tags = self.document.tags.all()
            tag_names = ", ".join(tag.name for tag in tags)
            self.tags_edit.setText(tag_names)

            drawings = self.document.drawings.all()
            self.drawings_table.setRowCount(len(drawings))
            for i, drawing in enumerate(drawings):
                self.drawings_table.setItem(i, 0, QTableWidgetItem(str(drawing.id)))
                self.drawings_table.setItem(i, 1, QTableWidgetItem(drawing.doc_name))
                self.drawings_table.setItem(i, 2, QTableWidgetItem(str(drawing.sheets.filter(is_actual=True).count())))
                sheet = drawing.sheets.first()
                mass = sheet.mass if sheet else "—"
                self.drawings_table.setItem(i, 3, QTableWidgetItem(str(mass)))
        except MainDocument.DoesNotExist:
            QMessageBox.critical(self, "Ошибка", f"Документ с ID {self.doc_id} не найден!")
            self.close()

    @transaction.atomic
    def save_changes(self):
        try:
            self.document.main_name = self.name_edit.text()
            self.document.comment = self.comment_edit.toPlainText()
            self.document.save()

            # Обработка тегов
            tag_names = [tag.strip() for tag in self.tags_edit.text().split(",")]
            tags = [Tag.objects.get_or_create(name=name)[0] for name in tag_names]
            self.document.tags.set(tags)

            QMessageBox.information(self, "Успех", "Данные сохранены!")
            self.parent_window.update_document_data()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка сохранения: {str(e)}")