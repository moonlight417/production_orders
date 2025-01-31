from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QTextEdit, QMessageBox, QListWidget
from PyQt5.QtGui import QPixmap
import os
from PyQt5.QtCore import Qt

from products.models import MainDocument, Drawing, DrawingSheet
from .print_dialog import PrintDialog  # Импортируем окно печати


class DocumentEditor(QDialog):
    """Окно редактирования конструкторского документа."""

    def __init__(self, doc_id, parent=None):
        super().__init__(parent)
        self.doc_id = doc_id
        self.setWindowTitle(f"Редактирование документа (ID: {self.doc_id})")
        self.setModal(True)

        # 📄 Загружаем документ из базы данных
        try:
            self.document = MainDocument.objects.get(id=self.doc_id)
        except MainDocument.DoesNotExist:
            QMessageBox.critical(self, "Ошибка", f"Документ с ID {self.doc_id} не найден!")
            return

        layout = QVBoxLayout()

        # Заголовок документа
        self.label = QLabel(f"<b>Документ:</b> {self.document.main_name}")
        layout.addWidget(self.label)

        # Поле для отображения чертежа
        self.drawing_label = QLabel("📂 Чертёж отсутствует")
        layout.addWidget(self.drawing_label)

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

        # Кнопки "Сохранить" и "Закрыть"
        self.save_button = QPushButton("Сохранить")
        self.save_button.clicked.connect(self.save_document)
        layout.addWidget(self.save_button)

        self.close_button = QPushButton("Закрыть")
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)

        self.setLayout(layout)

    def load_drawing_image(self):
        """Загружает изображение чертежа, если оно есть в базе данных, и возвращает его путь."""
        try:
            drawing_sheet = DrawingSheet.objects.filter(drawing__main_document=self.document, is_actual=True).first()

            if drawing_sheet and drawing_sheet.file:
                file_path = os.path.join("E:/Programming/production_orders/windows/design_filling",
                                         drawing_sheet.file.name)

                if os.path.exists(file_path):
                    pixmap = QPixmap(file_path)
                    if not pixmap.isNull():
                        self.drawing_label.setPixmap(pixmap.scaled(500, 500, Qt.KeepAspectRatio))
                        return file_path
                    else:
                        self.drawing_label.setText("⚠️ Ошибка загрузки изображения")
                else:
                    self.drawing_label.setText("❌ Файл не найден")

        except Exception as e:
            self.drawing_label.setText("❌ Ошибка загрузки чертежа")
            print(f"❌ Ошибка загрузки чертежа: {e}")

        return None

    def open_printer_window(self):
        """Открывает окно печати чертежа."""
        if not self.current_image_path:
            QMessageBox.warning(self, "Ошибка", "Нет изображения для печати.")
            return
        self.printer_window = PrintDialog(self.current_image_path)
        self.printer_window.exec_()  # Открываем модально

    def save_document(self):
        """Сохраняет изменения в документе."""
        try:
            self.document.comment = self.comment_edit.toPlainText()
            self.document.save()
            QMessageBox.information(self, "Успех", "Комментарий обновлён!")
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить документ: {e}")

