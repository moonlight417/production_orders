import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QMessageBox, QDialog, \
    QScrollArea
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt
from print_dialog import PrintDialog

from products.models import DrawingSheet, MainDocument


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
        print("Initializing DocumentEditor")

        # 📄 Загружаем документ из базы
        try:
            self.document = MainDocument.objects.get(id=self.doc_id)
            print(f"Document loaded: {self.document.main_name}")
        except MainDocument.DoesNotExist:
            QMessageBox.critical(self, "Ошибка", f"Документ с ID {self.doc_id} не найден!")
            print(f"Document with ID {self.doc_id} not found")
            return

        # Основной layout
        layout = QVBoxLayout(self)

        # Заголовок документа
        self.label = QLabel(f"<b>Документ:</b> {self.document.main_name}")
        layout.addWidget(self.label)

        # Поле для отображения чертежа
        self.drawing_label = QLabel("📂 Чертёж отсутствует")
        self.drawing_label.setMouseTracking(True)  # Разрешаем отслеживание движения мыши
        self.drawing_label.setCursor(QCursor(Qt.PointingHandCursor))  # Меняем курсор на лупу
        layout.addWidget(self.drawing_label)

        # Кнопка увеличения
        self.zoom_button = QPushButton("🔍 Увеличить чертёж")
        self.zoom_button.clicked.connect(self.open_zoomed_window)
        layout.addWidget(self.zoom_button)

        # Загружаем чертёж
        self.current_image_path = self.load_drawing_image()

        # Кнопка "Печать"
        self.print_button = QPushButton("🖨 Печать")
        self.print_button.clicked.connect(self.open_printer_window)
        layout.addWidget(self.print_button)

        # Поле для комментария
        self.comment_edit = QTextEdit()
        self.comment_edit.setText(self.document.comment or "")
        layout.addWidget(self.comment_edit)

        # Кнопки "Сохранить" и "Назад"
        button_layout = QVBoxLayout()

        self.save_button = QPushButton("Сохранить")
        self.save_button.clicked.connect(self.save_document)
        button_layout.addWidget(self.save_button)

        self.back_button = QPushButton("Назад")  # 🔹 Кнопка возврата
        self.back_button.clicked.connect(self.go_back)
        button_layout.addWidget(self.back_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def load_drawing_image(self):
        """Загружает чертёж из базы и отображает его."""
        print(f"🔄 Загрузка чертежа для документа {self.document.main_name}")

        try:
            drawing_sheet = DrawingSheet.objects.filter(drawing__main_document=self.document, is_actual=True).first()

            if drawing_sheet and drawing_sheet.file:
                file_path = os.path.join("E:/Programming/production_orders/windows/design_filling",
                                         drawing_sheet.file.name)
                print(f"📂 Пытаемся загрузить файл: {file_path}")

                if os.path.exists(file_path):
                    print("✅ Файл существует, загружаем QPixmap")
                    self.pixmap = QPixmap(file_path)

                    if not self.pixmap.isNull():
                        self.drawing_label.setPixmap(self.pixmap.scaled(500, 500, Qt.KeepAspectRatio))
                        return file_path
                    else:
                        print("❌ Ошибка: QPixmap вернул пустое изображение")
                        self.drawing_label.setText("⚠️ Ошибка загрузки изображения")
                else:
                    print("❌ Ошибка: Файл не найден")
                    self.drawing_label.setText("❌ Файл не найден")

        except Exception as e:
            print(f"❌ Ошибка загрузки чертежа: {e}")
            self.drawing_label.setText("❌ Ошибка загрузки чертежа")

        return None

    def open_zoomed_window(self):
        """Открывает окно с увеличенной версией чертежа с прокруткой."""
        if not hasattr(self, 'pixmap') or self.pixmap.isNull():
            QMessageBox.warning(self, "Ошибка", "Нет изображения для увеличения.")
            print("No image available for zooming.")
            return

        zoomed_window = ZoomedDrawingWindow(self.pixmap, self)
        zoomed_window.exec_()
    def add_hierarchy_buttons(self):
        """Добавляет кнопки для родительского и дочернего документов."""
        # Родительский документ
        if self.document.parent_document:
            self.parent_button = QPushButton(f"👨‍👩‍👧‍👦 Родитель: {self.document.parent_document.main_name}")
            self.parent_button.clicked.connect(self.show_parent_document)
            self.side_panel.addWidget(self.parent_button)

        # Дочерние документы
        children = MainDocument.objects.filter(parent_document=self.document)
        if children.exists():
            self.children_label = QLabel("👶 Дочерние документы:")
            self.side_panel.addWidget(self.children_label)
            for child in children:
                child_button = QPushButton(child.main_name)
                child_button.clicked.connect(lambda checked, child_id=child.id: self.show_child_document(child_id))
                self.side_panel.addWidget(child_button)

    def show_parent_document(self):
        """Загружает и отображает родительский документ."""
        if self.document.parent_document:
            self.load_document(self.document.parent_document.id)

    def show_child_document(self, child_id):
        """Загружает и отображает дочерний документ."""
        self.load_document(child_id)

    def load_document(self, doc_id):
        """Загружает новый документ по его ID."""
        self.document = MainDocument.objects.get(id=doc_id)
        self.label.setText(f"<b>Документ:</b> {self.document.main_name}")

        # Очистка старого изображения
        self.drawing_label.clear()
        self.drawing_label.setText("📂 Чертёж отсутствует")
        self.current_image_path = None

        # Загружаем новый чертёж
        self.load_drawing_image()

        # Обновляем кнопки для иерархии
        for i in reversed(range(self.side_panel.count())):
            widget = self.side_panel.itemAt(i).widget()
            if widget != self.label:
                widget.deleteLater()
        self.add_hierarchy_buttons()

    # def load_drawing_image(self):
    #     """Загружает чертёж из базы и отображает его."""
    #     try:
    #         drawing_sheet = DrawingSheet.objects.filter(drawing__main_document=self.document, is_actual=True).first()
    #
    #         if drawing_sheet and drawing_sheet.file:
    #             file_path = os.path.join("E:/Programming/production_orders/windows/design_filling",
    #                                      drawing_sheet.file.name)
    #
    #             if os.path.exists(file_path):
    #                 self.pixmap = QPixmap(file_path)
    #                 if not self.pixmap.isNull():
    #                     self.drawing_label.setPixmap(self.pixmap.scaled(500, 500, Qt.KeepAspectRatio))
    #                     self.drawing_label.setMouseTracking(True)
    #                     self.drawing_label.setCursor(QCursor(Qt.PointingHandCursor))  # Меняем курсор на лупу
    #                     return file_path
    #                 else:
    #                     self.drawing_label.setText("⚠️ Ошибка загрузки изображения")
    #             else:
    #                 self.drawing_label.setText("❌ Файл не найден")
    #
    #     except Exception as e:
    #         self.drawing_label.setText("❌ Ошибка загрузки чертежа")
    #         print(f"❌ Ошибка загрузки чертежа: {e}")
    #
    #     return None
    #
    # def open_zoomed_window(self):
    #     """Открывает окно с увеличенной версией чертежа с прокруткой."""
    #     if not hasattr(self, 'pixmap') or self.pixmap.isNull():
    #         QMessageBox.warning(self, "Ошибка", "Нет изображения для увеличения.")
    #         return
    #
    #     zoomed_window = ZoomedDrawingWindow(self.pixmap, self)
    #     zoomed_window.exec_()

    def open_printer_window(self):
        """Открывает окно печати чертежа."""
        if not hasattr(self, 'current_image_path') or not self.current_image_path:
            QMessageBox.warning(self, "Ошибка", "Нет изображения для печати.")
            print("⚠️ Печать отменена: Нет изображения")
            return

        print(f"🖨 Открываем окно печати для {self.current_image_path}")
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



