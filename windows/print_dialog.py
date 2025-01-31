from PyQt5.QtWidgets import QDialog, QMessageBox, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtCore import Qt


class PrintDialog(QDialog):
    """Диалоговое окно для печати изображения"""

    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.image_path = image_path
        self.setWindowTitle("Печать чертежа")

        # Основной layout
        layout = QVBoxLayout(self)

        # Кнопка печати
        self.print_button = QPushButton("Распечатать чертёж")
        self.print_button.clicked.connect(self.print_image)
        layout.addWidget(self.print_button)

        self.setLayout(layout)

    def print_image(self):
        """Открывает диалог печати и отправляет изображение на принтер."""
        printer = QPrinter()
        print_dialog = QPrintDialog(printer, self)

        if print_dialog.exec_() == QPrintDialog.Accepted:
            pixmap = QPixmap(self.image_path)
            if pixmap.isNull():
                QMessageBox.critical(self, "Ошибка", "Невозможно загрузить изображение для печати.")
                return

            painter = QPainter(printer)
            rect = printer.pageRect()

            # Масштабируем изображение, чтобы сохранить пропорции
            scaled_pixmap = pixmap.scaled(rect.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

            # Вычисляем центр страницы
            x_offset = (rect.width() - scaled_pixmap.width()) // 2
            y_offset = (rect.height() - scaled_pixmap.height()) // 2

            # Рисуем изображение на странице
            painter.drawPixmap(x_offset, y_offset, scaled_pixmap)
            painter.end()

            QMessageBox.information(self, "Успех", "Чертёж отправлен на печать.")
