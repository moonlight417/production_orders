import os

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QLineEdit, QCheckBox, QLabel, QPushButton, \
    QHBoxLayout, QWidget, QVBoxLayout, QScrollArea, QTabWidget, QTreeWidget, QTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from django.db import transaction
from products.models import MainDocument, Drawing, DrawingSheet, Tag
from windows.design_edit.tag_editor_widget import TagEditorWidget


class DesignDocumentEditForm(QMainWindow):
    def __init__(self, doc_id, parent=None):
        super().__init__(parent)
        self.doc_id = doc_id
        self.parent = parent
        self.document = MainDocument.objects.get(id=doc_id)
        self.setup_ui()
        self.load_data()

    def setup_ui(self):
        self.setWindowTitle(f"Редактирование документа: {self.document.main_name}")
        self.setGeometry(100, 100, 1200, 800)

        # Основной контейнер
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QHBoxLayout(self.main_widget)

        # Левая панель (редактирование структуры)
        self.left_panel = QWidget()
        self.left_layout = QVBoxLayout(self.left_panel)

        # Правая панель (редактирование чертежей)
        self.right_panel = QWidget()
        self.right_layout = QVBoxLayout(self.right_panel)

        # Инициализация компонентов
        self.init_metadata_section()
        self.init_structure_section()
        self.init_drawing_editor()

        self.layout.addWidget(self.left_panel, 1)
        self.layout.addWidget(self.right_panel, 2)

    def init_metadata_section(self):
        # Поля для основных данных
        self.name_edit = QLineEdit(self.document.main_name)
        self.comment_edit = QTextEdit(self.document.comment)
        self.tags_edit = TagEditorWidget(self.document)

        # Кнопки управления
        self.btn_save = QPushButton("Сохранить")
        self.btn_save.clicked.connect(self.save_changes)

        self.left_layout.addWidget(QLabel("Название документа:"))
        self.left_layout.addWidget(self.name_edit)
        self.left_layout.addWidget(QLabel("Комментарий:"))
        self.left_layout.addWidget(self.comment_edit)
        self.left_layout.addWidget(QLabel("Теги:"))
        self.left_layout.addWidget(self.tags_edit)
        self.left_layout.addWidget(self.btn_save)

    def init_structure_section(self):
        # Дерево структуры документа
        self.structure_tree = QTreeWidget()
        self.structure_tree.header().hide()
        self.populate_structure_tree()

        self.left_layout.addWidget(QLabel("Структура документа:"))
        self.left_layout.addWidget(self.structure_tree)

    def init_drawing_editor(self):
        # Редактор чертежей
        self.drawing_tabs = QTabWidget()
        self.right_layout.addWidget(self.drawing_tabs)

        # Кнопки управления чертежами
        self.btn_add_sheet = QPushButton("Добавить лист")
        self.btn_add_sheet.clicked.connect(self.add_sheet)
        self.right_layout.addWidget(self.btn_add_sheet)

    def load_data(self):
        # Загрузка связанных чертежей
        for drawing in self.document.drawings.all():
            self.add_drawing_tab(drawing)

    def add_drawing_tab(self, drawing):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        # Заголовок чертежа
        title = QLineEdit(drawing.doc_name)
        layout.addWidget(title)

        # Область для листов
        scroll = QScrollArea()
        sheets_widget = QWidget()
        self.sheets_layout = QVBoxLayout(sheets_widget)

        for sheet in drawing.sheets.all():
            self.add_sheet_editor(sheet)

        scroll.setWidget(sheets_widget)
        layout.addWidget(scroll)

        self.drawing_tabs.addTab(tab, drawing.doc_name)

    def add_sheet_editor(self, sheet):
        sheet_widget = QWidget()
        layout = QHBoxLayout(sheet_widget)

        # Изображение
        img_label = QLabel()
        if sheet.file:
            pixmap = QPixmap(sheet.file.path)
            img_label.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio))

        # Управление изображением
        btn_change = QPushButton("Изменить")
        btn_change.clicked.connect(lambda: self.change_image(sheet, img_label))

        # Поля данных
        mass_edit = QLineEdit(str(sheet.mass) if sheet.mass else "")
        actual_check = QCheckBox("Актуальный")
        actual_check.setChecked(sheet.is_actual)

        layout.addWidget(img_label)
        layout.addWidget(actual_check)
        layout.addWidget(QLabel("Масса:"))
        layout.addWidget(mass_edit)
        layout.addWidget(btn_change)

        self.sheets_layout.addWidget(sheet_widget)

    def change_image(self, sheet, label):
        file_path, _ = QFileDialog.getOpenFileName()
        if file_path:
            sheet.file.save(os.path.basename(file_path), open(file_path, 'rb'))
            label.setPixmap(QPixmap(file_path).scaled(400, 400, Qt.KeepAspectRatio))

    @transaction.atomic
    def save_changes(self):
        try:
            # Сохранение основных данных
            self.document.main_name = self.name_edit.text()
            self.document.comment = self.comment_edit.toPlainText()
            self.document.save()

            # Сохранение тегов
            self.tags_edit.save_tags()

            # Сохранение чертежей
            for i in range(self.drawing_tabs.count()):
                tab = self.drawing_tabs.widget(i)
                drawing = self.document.drawings.get(doc_name=tab.findChild(QLineEdit).text())

                # Обновление данных листов
                for j in range(self.sheets_layout.count()):
                    sheet_widget = self.sheets_layout.itemAt(j).widget()
                    sheet = drawing.sheets.all()[j]

                    sheet.mass = float(sheet_widget.findChild(QLineEdit).text())
                    sheet.is_actual = sheet_widget.findChild(QCheckBox).isChecked()
                    sheet.save()

            QMessageBox.information(self, "Сохранено", "Изменения успешно сохранены!")
            self.parent.update_document_data()
            self.close()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка сохранения: {str(e)}")
